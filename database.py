"""
database.py — Seekho.io Supabase integration layer.

Fixes over v1:
- get_supabase_client() uses @st.cache_resource (true singleton, one connection per app process)
- seed_syllabus() batch inserts 50 rows per request instead of 1 (500+ → ~10 HTTP calls)
- get_district() no longer double-nests cached calls — iterates local list directly
- All query functions have explicit try/except with fallback to pctb_syllabus.py
- All exported functions have clear docstrings
"""

import os
from typing import Optional
import streamlit as st

# ── Supabase client ──────────────────────────────────────────────────────────
try:
    from supabase import create_client, Client
    _SUPABASE_AVAILABLE = True
except ImportError:
    _SUPABASE_AVAILABLE = False


@st.cache_resource
def get_supabase_client() -> Optional["Client"]:
    """
    Returns a cached Supabase client singleton.

    Uses @st.cache_resource so the client is created ONCE per app process,
    not on every function call. This avoids opening a new HTTP connection
    on every query.

    Priority: st.secrets → environment variables → None (local fallback mode).
    """
    if not _SUPABASE_AVAILABLE:
        return None

    url = key = None

    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_ANON_KEY"]
    except Exception:
        pass

    if not url:
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_ANON_KEY")

    if not (url and key):
        return None

    try:
        return create_client(url, key)
    except Exception:
        return None


def _db_available() -> bool:
    return get_supabase_client() is not None


# ── Syllabus queries ─────────────────────────────────────────────────────────

@st.cache_data(ttl=3600)
def get_subjects(class_num: int) -> list[str]:
    """
    Return alphabetically sorted list of subjects for a given class.
    Source: Supabase → pctb_syllabus.py fallback.
    """
    client = get_supabase_client()
    if client:
        try:
            resp = (
                client.table("syllabus")
                .select("subject")
                .eq("class_num", class_num)
                .execute()
            )
            subjects = sorted({row["subject"] for row in resp.data})
            if subjects:
                return subjects
        except Exception:
            pass

    from pctb_syllabus import PCTB_SYLLABUS
    return list(PCTB_SYLLABUS.get(class_num, {}).keys())


@st.cache_data(ttl=3600)
def get_chapters(class_num: int, subject: str) -> list[str]:
    """
    Return ordered list of chapter titles for a class+subject pair.
    Ordered by chapter_num if available.
    """
    client = get_supabase_client()
    if client:
        try:
            resp = (
                client.table("syllabus")
                .select("chapter, chapter_num")
                .eq("class_num", class_num)
                .eq("subject", subject)
                .order("chapter_num")
                .execute()
            )
            chapters = [row["chapter"] for row in resp.data]
            if chapters:
                return chapters
        except Exception:
            pass

    from pctb_syllabus import get_chapters_for_subject
    return get_chapters_for_subject(class_num, subject)


@st.cache_data(ttl=3600)
def get_topics(class_num: int, subject: str, chapter: str) -> list[str]:
    """Return list of specific topics for a given chapter."""
    client = get_supabase_client()
    if client:
        try:
            resp = (
                client.table("syllabus")
                .select("topics")
                .eq("class_num", class_num)
                .eq("subject", subject)
                .eq("chapter", chapter)
                .execute()
            )
            if resp.data and resp.data[0].get("topics"):
                return resp.data[0]["topics"]
        except Exception:
            pass

    from pctb_syllabus import get_topics_for_chapter
    return get_topics_for_chapter(class_num, subject, chapter)


# ── District queries ─────────────────────────────────────────────────────────

@st.cache_data(ttl=7200)
def get_all_districts() -> list[dict]:
    """
    Return all district records with full context data.
    Used to populate the district dropdown and for AI prompt enrichment.
    """
    client = get_supabase_client()
    if client:
        try:
            resp = (
                client.table("districts")
                .select("*")
                .order("name")
                .execute()
            )
            if resp.data:
                return resp.data
        except Exception:
            pass

    return _local_districts()


def get_district_names() -> list[str]:
    """Return just the names for the dropdown widget."""
    return [d["name"] for d in get_all_districts()]


def get_district(name: str) -> dict:
    """
    Return full context dict for a district name.

    Falls back to a generic dict if the district is not in the DB.
    Does NOT use @st.cache_data here — iterates the already-cached
    get_all_districts() list to avoid double-nesting cached functions.
    """
    name_lower = name.lower()
    for d in get_all_districts():
        if d["name"].lower() == name_lower:
            return d

    # Generic fallback for custom/unknown districts
    return {
        "name": name,
        "province": "Pakistan",
        "economy": "agriculture, small trade, government services",
        "landmarks": f"{name} city centre, local bazaar",
        "transport": "motorcycles, rickshaws, wagons",
        "food": "roti, daal, sabzi, rice, chai",
        "occupations": "farmers, shopkeepers, teachers, government workers",
        "nature": "agricultural plains, seasonal weather patterns",
        "local_names": "Muhammad, Ali, Fatima, Ayesha, Ahmed, Sara",
        "school_type": "government schools dominant",
        "connectivity": "variable mobile data, load-shedding common",
        "board": "local BISE",
    }


# ── Analytics and persistence ────────────────────────────────────────────────

def save_lesson(
    school_name: str,
    district: str,
    class_num: int,
    subject: str,
    chapter: str,
    topic: str,
    language: str,
    output_mode: str,
    class_profile: str,
    content: str,
) -> Optional[str]:
    """
    Persist a generated lesson to Supabase.
    Returns the share_token string on success, None on failure.
    The share_token is auto-generated by Postgres (pgcrypto must be enabled).
    """
    client = get_supabase_client()
    if not client:
        return None

    try:
        resp = (
            client.table("generated_lessons")
            .insert({
                "school_name": school_name,
                "district": district,
                "class_num": class_num,
                "subject": subject,
                "chapter": chapter,
                "topic": topic,
                "language": language,
                "output_mode": output_mode,
                "class_profile": class_profile,
                "content": content,
                "word_count": len(content.split()),
            })
            .execute()
        )
        if resp.data:
            return resp.data[0].get("share_token")
    except Exception:
        pass
    return None


def get_lesson_by_token(token: str) -> Optional[dict]:
    """Retrieve a shared lesson by its share token. Used for ?share= URL param."""
    client = get_supabase_client()
    if not client:
        return None
    try:
        resp = (
            client.table("generated_lessons")
            .select("*")
            .eq("share_token", token)
            .limit(1)
            .execute()
        )
        if resp.data:
            return resp.data[0]
    except Exception:
        pass
    return None


def save_waitlist_entry(phone: str, school: str, district: str) -> bool:
    """Add a phone number to the Pro waitlist table."""
    client = get_supabase_client()
    if not client:
        return False
    try:
        client.table("waitlist").insert({
            "phone": phone,
            "school": school,
            "district": district,
        }).execute()
        return True
    except Exception:
        return False


def get_analytics_summary() -> dict:
    """Return basic usage stats for the admin view."""
    client = get_supabase_client()
    if not client:
        return {"total_lessons": 0, "db_connected": False}
    try:
        total_resp = (
            client.table("generated_lessons")
            .select("id", count="exact")
            .execute()
        )
        district_resp = (
            client.table("generated_lessons")
            .select("district")
            .order("created_at", desc=True)
            .limit(200)
            .execute()
        )
        # Count per district
        from collections import Counter
        district_counts = Counter(
            r["district"] for r in district_resp.data if r.get("district")
        )
        return {
            "total_lessons": total_resp.count or 0,
            "top_districts": district_counts.most_common(5),
            "db_connected": True,
        }
    except Exception:
        return {"total_lessons": 0, "db_connected": False}


# ── Database seeding ─────────────────────────────────────────────────────────

def seed_syllabus(batch_size: int = 50) -> tuple[int, int]:
    """
    Batch-insert all PCTB chapters into Supabase.

    v1 inserted one row per HTTP request (~500 requests).
    This version batches rows into groups of `batch_size` (default 50),
    reducing network calls from ~500 to ~10.

    Safe to re-run — uses UPSERT with conflict resolution on (class_num, subject, chapter).

    Returns: (success_count, error_count)
    """
    from pctb_syllabus import PCTB_SYLLABUS

    client = get_supabase_client()
    if not client:
        print("ERROR: No Supabase client. Check SUPABASE_URL and SUPABASE_ANON_KEY.")
        return 0, 0

    # Build the full list of rows to insert
    rows = []
    for class_num, subjects in PCTB_SYLLABUS.items():
        for subject, chapters in subjects.items():
            for i, ch in enumerate(chapters, 1):
                rows.append({
                    "class_num": class_num,
                    "subject": subject,
                    "chapter_num": i,
                    "chapter": ch["chapter"],
                    "topics": ch["topics"],
                    "pctb_ref": f"PCTB Class {class_num} {subject}",
                })

    success = errors = 0
    for i in range(0, len(rows), batch_size):
        batch = rows[i : i + batch_size]
        try:
            client.table("syllabus").upsert(
                batch,
                on_conflict="class_num,subject,chapter"
            ).execute()
            success += len(batch)
            print(f"  Seeded rows {i + 1}–{i + len(batch)} of {len(rows)}")
        except Exception as e:
            errors += len(batch)
            print(f"  ERROR on batch {i}–{i + batch_size}: {e}")

    return success, errors


# ── Local fallback district data ─────────────────────────────────────────────

def _local_districts() -> list[dict]:
    """
    Minimal district context data used when Supabase is unreachable.
    This ensures the app is fully functional offline / before DB setup.
    """
    return [
        {
            "name": "Fateh Jang / Attock", "province": "Punjab",
            "economy": "Sugarcane farming, brick kiln labour, wheat, Attock Oil Refinery",
            "landmarks": "GT Road Attock, Attock Fort, Indus River, Haro River",
            "transport": "Tractor-trolleys, Suzuki pickups, motorbikes, donkey carts",
            "food": "Makki ki roti with saag, gur, lassi, daal chawal",
            "occupations": "Sugarcane farmers, bhatta mazdoor, military families, dukandaar",
            "nature": "Mustard fields, Indus floods, keekar trees, canal irrigation, winter fog",
            "local_names": "Akbar, Bashir, Zainab, Nazia, Farhan, Gulnaz",
            "school_type": "Government Urdu-medium, 40-50 students per class",
            "connectivity": "3G mostly, load-shedding 8-12 hours",
            "board": "BISE Rawalpindi",
        },
        {
            "name": "Lahore", "province": "Punjab",
            "economy": "Garment factories, IT sector, trade, services",
            "landmarks": "Lahore Fort, Badshahi Mosque, Mall Road, Anarkali Bazaar",
            "transport": "Orange Line Metro, rickshaws, motorcycles, Careem",
            "food": "Halwa puri, nihari, Lahori chargha, lassi",
            "occupations": "Factory workers, traders, IT professionals, teachers",
            "nature": "Canal walks, mango season June, smog November",
            "local_names": "Hamza, Ayesha, Bilal, Sana, Usman, Nimra",
            "school_type": "Mix of private chains (Beaconhouse, LGS) and government",
            "connectivity": "4G widely available",
            "board": "BISE Lahore",
        },
        {
            "name": "Multan", "province": "Punjab",
            "economy": "Cotton farming, mango orchards, blue pottery, carpet weaving",
            "landmarks": "Shah Rukn-e-Alam shrine, Multan Fort, Hussain Agahi Bazaar",
            "transport": "Qingqi rickshaws, motorcycles, wagons, tractor-trolleys",
            "food": "Sohan halwa, Multani lassi, mangoes, daal mash",
            "occupations": "Cotton farmers, mango growers, handicraft artisans, traders",
            "nature": "Extreme heat 50°C, cotton fields, Chenab river",
            "local_names": "Pervaiz, Rukhsana, Sajid, Rabia, Shafiq, Bushra",
            "school_type": "Government dominant, shrine madrassas prominent",
            "connectivity": "Moderate 4G in city",
            "board": "BISE Multan",
        },
        {
            "name": "Peshawar", "province": "Khyber Pakhtunkhwa",
            "economy": "Afghan transit trade, Karkhano Market, dry fruit trade, handicrafts",
            "landmarks": "Qissa Khwani Bazaar, Bala Hisar Fort, Khyber Pass",
            "transport": "Datsun pickups, rickshaws, horse-drawn tongas",
            "food": "Chapli kebab, Peshawari ice cream, Kabuli pulao, dry fruits",
            "occupations": "Dry fruit traders, Karkhano shop owners, government employees",
            "nature": "Khyber hills, River Kabul, walnut trees, cold winters",
            "local_names": "Noor, Palwasha, Junaid, Hina, Rashid, Gul Meena",
            "school_type": "Government, KP Education Foundation schools, Pashto-Urdu bilingual",
            "connectivity": "Variable, improving",
            "board": "BISE Peshawar",
        },
        {
            "name": "Karachi", "province": "Sindh",
            "economy": "Textile mills, port logistics, finance, fisheries, IT",
            "landmarks": "Clifton Beach, Empress Market, Burns Road, Port Qasim",
            "transport": "K-Electric buses, rickshaws, motorcycles, InDrive, heavy traffic",
            "food": "Biryani, bun kebab, nihari, sea fish (pomfret, jhinga)",
            "occupations": "Factory workers, fishermen, traders, corporate workers",
            "nature": "Arabian Sea, mangroves, hot humid summers, cyclone risk",
            "local_names": "Zubair, Nida, Asif, Shirin, Kamran, Fahmida",
            "school_type": "Large variation: elite private to community schools",
            "connectivity": "Good 4G in urban areas, poor in Lyari, Orangi, Baldia",
            "board": "BISE Karachi",
        },
        {
            "name": "Rawalpindi / Islamabad", "province": "Punjab / Federal",
            "economy": "Government services, military, Murree tourism, construction",
            "landmarks": "Murree Hills, Rawal Lake, Faisal Mosque, Raja Bazaar",
            "transport": "Metro Bus, Suzuki vans, motorcycles, government cars",
            "food": "Potohari daal, sajji on Murree Road, kulfi, Pothohari bread",
            "occupations": "Government servants, military, teachers, IT professionals",
            "nature": "Margalla Hills, Rawal Lake, pine forests, cold winters",
            "local_names": "Shahid, Mehwish, Tariq, Rubab, Waqar, Aisha",
            "school_type": "FBISE schools, mix of private and government",
            "connectivity": "Good 4G and fiber in Islamabad, variable in Potohar villages",
            "board": "FBISE / BISE Rawalpindi",
        },
        {
            "name": "Faisalabad", "province": "Punjab",
            "economy": "Textile capital: weaving, dyeing, garments, grain trade",
            "landmarks": "Clock Tower (Ghanta Ghar) 8 bazaars, Lyallpur Museum",
            "transport": "Qingqi rickshaws, motorcycles, Suzuki wagons, textile trucks",
            "food": "Dhodha, fresh milk products, saag roti, bhutta, jalebi",
            "occupations": "Textile mill workers, grain merchants, machinery mechanics",
            "nature": "Flat plains, Chenab River proximity, winter fog",
            "local_names": "Asghar, Razia, Imran, Shaheena, Khalid, Nasima",
            "school_type": "Government dominant, growing private sector",
            "connectivity": "Moderate 4G, load-shedding common",
            "board": "BISE Faisalabad",
        },
        {
            "name": "Gujranwala", "province": "Punjab",
            "economy": "Steel industry, basmati rice export, ceramics, food processing",
            "landmarks": "Ranjit Singh haveli, grain market, Gujranwala Sports Complex",
            "transport": "Motorcycles, wagons, steel and rice trucks, rickshaws",
            "food": "Basmati rice, white chickpea curry, lassi, fried fish",
            "occupations": "Steel workers, rice millers, ceramic factory workers, traders",
            "nature": "Flat Punjab plains, rice paddies, winter fog",
            "local_names": "Usman, Kiran, Imtiaz, Shabana, Rasheed, Ghazala",
            "school_type": "Mix of government and private, relatively better infrastructure",
            "connectivity": "Moderate to good 4G",
            "board": "BISE Gujranwala",
        },
        {
            "name": "Quetta", "province": "Balochistan",
            "economy": "Fruit growing, coal mining, Afghan transit trade, livestock",
            "landmarks": "Quetta Fruit Market, Hanna Lake, Ziarat juniper forest",
            "transport": "Motorcycles, pickup trucks, inter-city coaches, donkeys in villages",
            "food": "Sajji, bolani, Afghan naan, pomegranate, dried fruits",
            "occupations": "Fruit farmers, coal miners, Afghan traders, government servants",
            "nature": "Dry mountainous terrain, juniper forests, snow in winters",
            "local_names": "Nasrullah, Zarghona, Daud, Gul Bibi, Waheed, Malika",
            "school_type": "Government schools, Balochi-Brahui-Pashto-Urdu multilingual",
            "connectivity": "3G variable, severe load-shedding",
            "board": "BISE Quetta",
        },
        {
            "name": "Sialkot", "province": "Punjab",
            "economy": "Sports goods (footballs, cricket bats), surgical instruments, leather export",
            "landmarks": "Allama Iqbal birthplace museum, Sialkot Fort, export factories",
            "transport": "Motorcycles, rickshaws, factory worker vans, export trucks",
            "food": "Sialkoti paye, white chickpeas, lassi, puri channay",
            "occupations": "Sports goods workers, surgical instrument makers, leather tanners, exporters",
            "nature": "Flat plains, Chenab river proximity, winter fog, muggy summers",
            "local_names": "Shahbaz, Amina, Zahid, Saima, Inam, Robina",
            "school_type": "Good private sector education, government schools present",
            "connectivity": "Good 4G due to export industry",
            "board": "BISE Gujranwala",
        },
    ]
