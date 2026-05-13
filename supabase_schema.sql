-- ============================================================
-- SEEKHO.IO — SUPABASE DATABASE SCHEMA v2 (FIXED)
-- Paste this ENTIRE file into:
--   Supabase Dashboard → SQL Editor → New Query → Run
-- ============================================================

-- ── STEP 1: Enable pgcrypto ──────────────────────────────────────────────────
-- THIS IS REQUIRED. gen_random_bytes() used for share_token DEFAULT will
-- silently fail without this extension, breaking every lesson save.
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- ── TABLE 1: DISTRICTS ───────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS districts (
    id           SERIAL PRIMARY KEY,
    name         TEXT    NOT NULL UNIQUE,
    province     TEXT    NOT NULL,
    economy      TEXT,
    landmarks    TEXT,
    transport    TEXT,
    food         TEXT,
    occupations  TEXT,
    nature       TEXT,
    local_names  TEXT,
    school_type  TEXT,
    connectivity TEXT,
    board        TEXT,
    created_at   TIMESTAMPTZ DEFAULT NOW(),
    updated_at   TIMESTAMPTZ DEFAULT NOW()
);

-- ── TABLE 2: SYLLABUS ────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS syllabus (
    id          SERIAL  PRIMARY KEY,
    class_num   INTEGER NOT NULL CHECK (class_num BETWEEN 1 AND 12),
    subject     TEXT    NOT NULL,
    chapter_num INTEGER,
    chapter     TEXT    NOT NULL,
    topics      TEXT[]  NOT NULL DEFAULT '{}',
    pctb_ref    TEXT,
    created_at  TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE (class_num, subject, chapter)
);

-- ── TABLE 3: GENERATED LESSONS ───────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS generated_lessons (
    id            SERIAL PRIMARY KEY,
    school_name   TEXT,
    district      TEXT,
    class_num     INTEGER,
    subject       TEXT,
    chapter       TEXT,
    topic         TEXT,
    language      TEXT,
    output_mode   TEXT,
    class_profile TEXT,
    content       TEXT,
    word_count    INTEGER,
    share_token   TEXT UNIQUE DEFAULT encode(gen_random_bytes(8), 'hex'),
    created_at    TIMESTAMPTZ DEFAULT NOW()
);

-- ── TABLE 4: SCHOOLS ─────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS schools (
    id         SERIAL PRIMARY KEY,
    name       TEXT NOT NULL,
    district   TEXT,
    type       TEXT CHECK (type IN ('government', 'private', 'madrassa', 'other')),
    board      TEXT,
    phone      TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ── TABLE 5: WAITLIST ────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS waitlist (
    id         SERIAL PRIMARY KEY,
    phone      TEXT,
    school     TEXT,
    district   TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ── INDEXES ──────────────────────────────────────────────────────────────────
CREATE INDEX IF NOT EXISTS idx_syllabus_class_subject ON syllabus          (class_num, subject);
CREATE INDEX IF NOT EXISTS idx_lessons_district       ON generated_lessons (district);
CREATE INDEX IF NOT EXISTS idx_lessons_created        ON generated_lessons (created_at DESC);
CREATE INDEX IF NOT EXISTS idx_districts_name         ON districts         (name);
-- Share token lookups must be O(1):
CREATE UNIQUE INDEX IF NOT EXISTS idx_lessons_token   ON generated_lessons (share_token);

-- ── AUTO-UPDATE updated_at ───────────────────────────────────────────────────
CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$;
DROP TRIGGER IF EXISTS trg_districts_updated_at ON districts;
CREATE TRIGGER trg_districts_updated_at
    BEFORE UPDATE ON districts
    FOR EACH ROW EXECUTE FUNCTION set_updated_at();

-- ── ROW LEVEL SECURITY ───────────────────────────────────────────────────────
ALTER TABLE districts         ENABLE ROW LEVEL SECURITY;
ALTER TABLE syllabus          ENABLE ROW LEVEL SECURITY;
ALTER TABLE generated_lessons ENABLE ROW LEVEL SECURITY;
ALTER TABLE waitlist          ENABLE ROW LEVEL SECURITY;

-- Districts: public read (anon key), write via service_role only
CREATE POLICY "anon_read_districts" ON districts
    FOR SELECT USING (true);

-- Syllabus: public read
CREATE POLICY "anon_read_syllabus" ON syllabus
    FOR SELECT USING (true);

-- Lessons: public insert + public read (share links need SELECT)
CREATE POLICY "anon_insert_lessons" ON generated_lessons
    FOR INSERT WITH CHECK (true);
CREATE POLICY "anon_read_lessons" ON generated_lessons
    FOR SELECT USING (true);

-- Waitlist: public insert
CREATE POLICY "anon_insert_waitlist" ON waitlist
    FOR INSERT WITH CHECK (true);

-- ── SEED: DISTRICT DATA ──────────────────────────────────────────────────────
INSERT INTO districts
    (name, province, economy, landmarks, transport, food,
     occupations, nature, local_names, school_type, connectivity, board)
VALUES

('Fateh Jang / Attock', 'Punjab',
 'Sugarcane farming, brick kiln labour (bhatta), wheat, Attock Oil Refinery workers',
 'GT Road Attock, Attock Fort, Indus River, Haro River, Campbellpur Chowk',
 'Tractor-trolleys on GT Road, Suzuki pickups, motorbikes on kachha roads, donkey carts',
 'Makki ki roti with saag, gur from sugarcane, lassi, daal chawal, sugarcane juice from thelas',
 'Sugarcane farmers, bhatta mazdoor (brick kiln workers), military families (Attock Cantonment), dukandaar',
 'Mustard fields February, Indus floods July-August, keekar and shisham trees, canal irrigation, winter fog',
 'Akbar, Bashir, Zainab, Nazia, Farhan, Gulnaz, Muhammad Aslam, Rukhsana',
 'Government Urdu-medium dominant, 40-50 students per class, few private schools',
 'Mostly 3G, rural areas often no data, load-shedding 8-12 hours daily',
 'BISE Rawalpindi'),

('Lahore', 'Punjab',
 'Garment factories, IT sector, trade, services, Lahore Canal industrial area, dairy farms on outskirts',
 'Lahore Fort, Badshahi Mosque, Mall Road, Anarkali Bazaar, Data Darbar, Liberty Chowk, Orange Line Metro',
 'Rickshaws, Orange Line Metro, motorcycles, Careem/InDrive, traffic jams on Ferozepur Road and Canal Road',
 'Halwa puri from Anarkali, nihari, Lahori chargha, lassi, parathay from dhabas, paye',
 'Factory workers, traders, IT professionals, teachers, rickshaw drivers, tailors, bank employees',
 'Ravi River (mostly dry), canal walks, mango season June, smog November-December',
 'Hamza, Ayesha, Bilal, Sana, Usman, Nimra, Ali Raza, Fatima',
 'Mix of private chains (Beaconhouse, LGS, LACAS) and government schools',
 '4G widely available, mostly stable electricity in main city',
 'BISE Lahore'),

('Multan', 'Punjab',
 'Cotton farming and ginning, mango orchards, blue pottery handicrafts, carpet weaving, food processing',
 'Shah Rukn-e-Alam shrine, Multan Fort, Hussain Agahi Bazaar, mango orchards on Muzaffargarh Road',
 'Qingqi rickshaws, motorcycles, wagons to villages, tractor-trolleys, inter-city buses',
 'Sohan halwa, Multani lassi, mangoes (Chaunsa, Anwar Ratol), daal mash, saag, kheer',
 'Cotton farmers, mango growers, handicraft artisans, shrine caretakers, traders, fertilizer dealers',
 'Chenab River nearby, extreme heat 50°C summers, cotton picking October, sandstorms in summer',
 'Pervaiz, Rukhsana, Sajid, Rabia, Shafiq, Bushra, Ghulam Rasool, Nasreen',
 'Government Urdu-medium dominant, shrine-associated madrassas prominent',
 'Moderate 4G in city, variable in surrounding villages',
 'BISE Multan'),

('Peshawar', 'Khyber Pakhtunkhwa',
 'Afghan transit trade, Karkhano Market, dry fruit trade, handicrafts, agriculture in Charsadda and Mardan',
 'Qissa Khwani Bazaar, Bala Hisar Fort, Peshawar Museum, Namak Mandi, Khyber Pass',
 'Datsun pickup trucks to villages, rickshaws, Peshawari chappal shops, horse-drawn tongas',
 'Chapli kebab, Peshawari ice cream, Kabuli pulao, dry fruits from Karkhano, teemar roti',
 'Dry fruit traders, Karkhano shop owners, government employees, Pashtun tribal farmers, transporters',
 'Khyber hills, River Kabul, walnut and apricot trees, cold winters, occasional snow',
 'Noor, Palwasha, Junaid, Hina, Rashid, Gul Meena, Asad, Rubina',
 'Government schools, KP Education Foundation schools, Pashto-Urdu bilingual classroom reality',
 'Variable, improving under KP government programs',
 'BISE Peshawar'),

('Karachi', 'Sindh',
 'Pakistan commercial hub: textile mills, port logistics, finance, fisheries, IT, informal economy',
 'Clifton Beach, Empress Market, Burns Road, Korangi Industrial Area, Port Qasim, Manora Island',
 'K-Electric buses, rickshaws, motorcycles, InDrive/Careem, extreme traffic on Shahrah-e-Faisal',
 'Biryani, nihari, bun kebab from Burns Road, pani puri, sea fish (pomfret, jhinga)',
 'Factory workers, fishermen, traders, corporate workers, port workers, street vendors, domestic workers',
 'Arabian Sea coast, mangroves at Indus delta, hot humid summers, cyclone risk, heat waves',
 'Zubair, Nida, Asif, Shirin, Kamran, Fahmida, Junaid, Sajida',
 'Large variation: elite private to community schools; multi-ethnic (Urdu, Sindhi, Balochi, Pashto)',
 'Good 4G in urban areas, poor in Lyari, Orangi, Baldia, Malir outskirts',
 'BISE Karachi'),

('Rawalpindi / Islamabad', 'Punjab / Federal',
 'Government services, military, Murree tourism, construction, federal institutions',
 'Murree Hills, Rawal Lake, Faisal Mosque, Raja Bazaar, Lal Kurti Bazaar, Pakistan Monument',
 'Metro Bus Islamabad-Rawalpindi, Potohari village culture, Suzuki vans, motorcycles, government cars',
 'Potohari daal, sajji on Murree Road, Islamabad F-7 Jinnah Supermarket kulfi, Pothohari bread',
 'Government servants, military personnel, teachers, shopkeepers, construction workers, IT professionals',
 'Margalla Hills, Rawal Lake, pine forests, moderate climate, cold winters with occasional snow',
 'Shahid, Mehwish, Tariq, Rubab, Waqar, Aisha, Zubair, Hafsa',
 'FBISE schools, mix of private and government, slightly higher literacy than rural Punjab',
 'Good 4G and fiber in Islamabad, variable in Rawalpindi tehsils and Potohar villages',
 'FBISE (Federal) / BISE Rawalpindi'),

('Faisalabad', 'Punjab',
 'Textile capital: weaving, dyeing, garment manufacturing, grain trade, agricultural machinery',
 'Clock Tower (Ghanta Ghar) 8 bazaars, Lyallpur Museum, D-Ground textile mills, grain mandi',
 'Qingqi rickshaws, motorcycles, Suzuki wagons, trucks loaded with textile bales and grain sacks',
 'Dhodha (special sweet), fresh milk products, saag and roti, bhutta from thelas, jalebi',
 'Textile mill workers, traders, grain merchants, agricultural laborers, machinery mechanics',
 'Chenab River proximity, flat agricultural plains, winter fog, hot summers',
 'Asghar, Razia, Imran, Shaheena, Khalid, Nasima, Sarfraz, Gulshan',
 'Government schools dominant, growing private sector, industrial worker families',
 'Moderate 4G, load-shedding common in residential areas',
 'BISE Faisalabad'),

('Gujranwala', 'Punjab',
 'Steel and metal industry, basmati rice export, ceramics (tiles, sanitary ware), food processing',
 'Ranjit Singh''s haveli, grain market, ceramics industry area, Gujranwala Sports Complex',
 'Motorcycles, wagons, trucks carrying steel and rice, rickshaws',
 'Basmati rice dishes, white chickpea curry, lassi, fried fish, doodh patti chai',
 'Steel workers, rice millers, ceramic factory workers, small traders, rice farmers',
 'Flat Punjab plains, rice paddies, Chenab and Ravi tributaries, winter fog',
 'Usman, Kiran, Imtiaz, Shabana, Rasheed, Ghazala, Babar, Naila',
 'Mix of government and private schools, relatively better education infrastructure',
 'Moderate to good 4G',
 'BISE Gujranwala'),

('Quetta', 'Balochistan',
 'Fruit growing (apples, grapes, pomegranate), coal mining, Afghan transit trade, livestock farming',
 'Quetta Fruit Market, Hanna Lake, Urak Valley, Ziarat juniper forest, Chiltan National Park',
 'Motorcycles, pickup trucks, inter-city coaches to Karachi and Kandahar, donkeys in villages',
 'Sajji (whole roasted lamb/chicken), bolani, Afghan naan, pomegranate and grapes, dried fruits',
 'Fruit farmers and sellers, coal miners, Afghan traders, government servants, livestock herders',
 'Dry mountainous terrain, juniper forests, cold winters with snow, hot dry summers, high altitude',
 'Nasrullah, Zarghona, Daud, Gul Bibi, Waheed, Malika, Habib, Shaista',
 'Government schools, some private, Balochi-Brahui-Pashto-Urdu multilingual reality',
 'Limited connectivity, 3G variable, severe load-shedding',
 'BISE Quetta'),

('Sialkot', 'Punjab',
 'Sports goods capital (footballs, cricket bats, hockey sticks), surgical instruments, leather goods export',
 'Allama Iqbal birthplace museum, Sialkot Fort, export factories district, Pasrur town',
 'Motorcycles, rickshaws, factory worker vans, trucks carrying export goods to Lahore airport',
 'Sialkoti paye, white chickpeas, lassi, fresh milk, puri channay from breakfast thelas',
 'Sports goods factory workers, surgical instrument makers, leather tanners, exporters, farmers',
 'Flat plains, Chenab river proximity, winter fog, muggy summers, tubewells everywhere',
 'Shahbaz, Amina, Zahid, Saima, Inam, Robina, Yasir, Kalsoom',
 'Good private schools due to export wealth, government schools also present',
 'Good 4G due to export industry requirements',
 'BISE Gujranwala')

ON CONFLICT (name) DO NOTHING;
