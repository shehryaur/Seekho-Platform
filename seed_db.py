"""
seed_db.py — One-time database seeding script for Seekho.io

Run this ONCE after setting up Supabase to populate the syllabus table.
Do NOT run this from inside the Streamlit app.

Usage:
    python seed_db.py

Requirements:
    - SUPABASE_URL and SUPABASE_SERVICE_KEY set in .env file (NOT anon key — use service role key for seeding)
    - pctb_syllabus.py in the same folder
    - supabase Python package installed
"""

import os
import sys

# ── Load .env if present ─────────────────────────────────────────────────────
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ Loaded .env file")
except ImportError:
    print("ℹ️  python-dotenv not installed. Reading env vars directly.")

# ── Check credentials ─────────────────────────────────────────────────────────
SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
# For seeding use the SERVICE ROLE key (not anon key) — it bypasses RLS
SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_KEY", os.environ.get("SUPABASE_ANON_KEY", ""))

if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ ERROR: SUPABASE_URL and SUPABASE_SERVICE_KEY must be set.")
    print()
    print("Create a .env file in your project folder with:")
    print("  SUPABASE_URL=https://your-project.supabase.co")
    print("  SUPABASE_SERVICE_KEY=your-service-role-key-here")
    print()
    print("Find your service role key at:")
    print("  Supabase Dashboard → Settings → API → service_role (secret)")
    sys.exit(1)

# ── Connect ───────────────────────────────────────────────────────────────────
try:
    from supabase import create_client
except ImportError:
    print("❌ ERROR: supabase package not installed.")
    print("Run: pip install supabase")
    sys.exit(1)

try:
    from pctb_syllabus import PCTB_SYLLABUS
except ImportError:
    print("❌ ERROR: pctb_syllabus.py not found in current folder.")
    sys.exit(1)

print(f"\n🔌 Connecting to Supabase: {SUPABASE_URL}")
client = create_client(SUPABASE_URL, SUPABASE_KEY)
print("✅ Connected\n")


def seed_syllabus(batch_size: int = 50) -> None:
    """Batch-insert all PCTB chapters into the syllabus table."""

    # Build all rows first
    rows = []
    for class_num, subjects in PCTB_SYLLABUS.items():
        for subject, chapters in subjects.items():
            for i, ch in enumerate(chapters, 1):
                rows.append({
                    "class_num":   class_num,
                    "subject":     subject,
                    "chapter_num": i,
                    "chapter":     ch["chapter"],
                    "topics":      ch["topics"],
                    "pctb_ref":    f"PCTB Class {class_num} {subject}",
                })

    total  = len(rows)
    done   = 0
    errors = 0

    print(f"📚 Seeding {total} chapter rows in batches of {batch_size}...")
    print()

    for i in range(0, total, batch_size):
        batch = rows[i : i + batch_size]
        batch_end = min(i + batch_size, total)
        try:
            client.table("syllabus").upsert(
                batch,
                on_conflict="class_num,subject,chapter"
            ).execute()
            done += len(batch)
            pct = int(done / total * 100)
            print(f"  ✅ Rows {i+1:>4}–{batch_end:>4} of {total}  [{pct:>3}%]")
        except Exception as e:
            errors += len(batch)
            print(f"  ❌ ERROR on rows {i+1}–{batch_end}: {e}")

    print()
    print(f"{'='*50}")
    print(f"  Syllabus seeding complete")
    print(f"  ✅ Success : {done} rows")
    print(f"  ❌ Errors  : {errors} rows")
    print(f"{'='*50}\n")


def verify_seed() -> None:
    """Quick verification that data landed correctly."""
    print("🔍 Verifying seed data...\n")

    for class_num in [1, 5, 9, 12]:
        try:
            resp = (
                client.table("syllabus")
                .select("subject, chapter", count="exact")
                .eq("class_num", class_num)
                .execute()
            )
            count = resp.count or len(resp.data)
            subjects = {r["subject"] for r in resp.data}
            print(f"  Class {class_num:>2}: {count:>3} chapters | Subjects: {', '.join(sorted(subjects))}")
        except Exception as e:
            print(f"  Class {class_num}: ERROR — {e}")

    print()
    try:
        resp = client.table("districts").select("name").execute()
        print(f"  Districts: {len(resp.data)} loaded → {', '.join(d['name'] for d in resp.data[:4])}...")
    except Exception as e:
        print(f"  Districts: ERROR — {e}")

    print()
    print("✅ Verification done. If counts look correct, your DB is ready.\n")


# ── Run ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("  SEEKHO.IO — DATABASE SEEDER")
    print("=" * 50)
    print()

    answer = input("This will upsert all PCTB chapters into Supabase. Continue? (y/n): ").strip().lower()
    if answer != "y":
        print("Cancelled.")
        sys.exit(0)

    print()
    seed_syllabus()
    verify_seed()

    print("🎉 Done! You can now run: streamlit run seekho_v3.py")
