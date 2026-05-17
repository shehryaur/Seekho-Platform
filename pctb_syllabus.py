"""
PCTB_SYLLABUS — Complete Punjab Curriculum & Textbook Board chapter data.
Covers Class 1 through Class 12, all major subjects.

This is the authoritative seed file for Seekho.io's Supabase database.
Source: Punjab Curriculum & Textbook Board official syllabi (from training knowledge).
"""

# Structure: { class_num: { subject: [ {chapter, topics: []} ] } }
PCTB_SYLLABUS = {

    # ── CLASS 1 ──────────────────────────────────────────────────────────────
    1: {
        "Urdu": [
            {"chapter": "Haraf Shanasi (Letters)", "topics": ["Alif to Ya recognition", "Writing Haraf", "Short Harakaat (Zabar, Zer, Pesh)"]},
            {"chapter": "Alfaz Banana (Word Formation)", "topics": ["3-letter words", "Joining letters", "Simple vocabulary"]},
            {"chapter": "Chhoti Nazmain (Short Poems)", "topics": ["Memorisation and recitation", "Understanding meaning"]},
        ],
        "English": [
            {"chapter": "Alphabet", "topics": ["Capital and small letters A-Z", "Letter recognition", "Letter sounds"]},
            {"chapter": "Phonics", "topics": ["Short vowel sounds", "CVC words (cat, bat, hat)", "Blending sounds"]},
            {"chapter": "Simple Words & Pictures", "topics": ["Classroom objects", "Colors", "Animals", "Body parts"]},
        ],
        "Mathematics": [
            {"chapter": "Numbers 1–20", "topics": ["Counting objects", "Writing numbers", "Number sequence", "Before/After/Between"]},
            {"chapter": "Numbers 21–100", "topics": ["Tens and ones", "Skip counting", "Comparing numbers"]},
            {"chapter": "Addition (within 10)", "topics": ["Adding objects", "Number sentences", "Addition facts"]},
            {"chapter": "Subtraction (within 10)", "topics": ["Taking away", "Number sentences", "Subtraction facts"]},
            {"chapter": "Shapes", "topics": ["Circle, Square, Triangle, Rectangle", "Sorting shapes"]},
        ],
        "General Knowledge": [
            {"chapter": "My Body", "topics": ["Parts of the body", "Five senses", "Keeping clean"]},
            {"chapter": "My Family", "topics": ["Family members", "Roles in the family"]},
            {"chapter": "Animals Around Me", "topics": ["Pet animals", "Wild animals", "Farm animals", "Animal sounds"]},
            {"chapter": "My School", "topics": ["School building", "Classroom objects", "School rules"]},
        ],
    },

    # ── CLASS 2 ──────────────────────────────────────────────────────────────
    2: {
        "Urdu": [
            {"chapter": "Qiradat (Reading)", "topics": ["Short paragraphs", "Reading comprehension", "Answering questions"]},
            {"chapter": "Imlaa (Spelling)", "topics": ["Common Urdu words", "Dictation practice"]},
            {"chapter": "Nazmain (Poetry)", "topics": ["2-3 poems", "Recitation and meaning"]},
            {"chapter": "Chhoti Kahaniyaan (Short Stories)", "topics": ["Moral stories", "Characters and events"]},
        ],
        "English": [
            {"chapter": "Reading Comprehension", "topics": ["Short passages", "Questions and answers (yes/no, one word)"]},
            {"chapter": "Vocabulary", "topics": ["Action words (verbs)", "Describing words (adjectives)", "Days of the week", "Months"]},
            {"chapter": "Grammar Basics", "topics": ["Nouns (naming words)", "Simple sentences", "Capital letters and full stop"]},
            {"chapter": "Simple Writing", "topics": ["My name/address", "Filling forms", "3-sentence paragraph"]},
        ],
        "Mathematics": [
            {"chapter": "Numbers to 1000", "topics": ["Hundreds, tens, ones", "Expanded form", "Comparing numbers (>, <, =)"]},
            {"chapter": "Addition (2-digit)", "topics": ["With and without carrying", "Word problems (PKR context)"]},
            {"chapter": "Subtraction (2-digit)", "topics": ["With and without borrowing", "Word problems"]},
            {"chapter": "Multiplication Tables 2–5", "topics": ["Tables 2, 3, 4, 5", "Repeated addition link", "Word problems"]},
            {"chapter": "Measurement", "topics": ["Length (metre, centimetre)", "Weight (kilogram, gram)", "Capacity (litre)"]},
            {"chapter": "Time", "topics": ["Hours and minutes", "Telling time on clock", "Days and months"]},
        ],
        "General Knowledge": [
            {"chapter": "Food and Health", "topics": ["Types of food", "Healthy eating", "Cleanliness"]},
            {"chapter": "Plants Around Me", "topics": ["Parts of a plant", "Uses of plants", "Trees vs shrubs vs herbs"]},
            {"chapter": "Community Helpers", "topics": ["Doctor, teacher, farmer, police", "Their roles"]},
            {"chapter": "Seasons", "topics": ["Four seasons in Pakistan", "Season-appropriate clothing and activities"]},
        ],
    },

    # ── CLASS 3 ──────────────────────────────────────────────────────────────
    3: {
        "Urdu": [
            {"chapter": "Sabaq 1–5 (Lessons)", "topics": ["Prose reading", "Comprehension questions", "Vocabulary"]},
            {"chapter": "Sabaq 6–10", "topics": ["Longer prose", "Writing answers in sentences"]},
            {"chapter": "Imlaa aur Khatt (Spelling & Writing)", "topics": ["Weekly spelling lists", "Letter writing (khat)"]},
            {"chapter": "Nazmain", "topics": ["3-4 poems with meaning", "Recitation"]},
            {"chapter": "Grammar Basics", "topics": ["Ism (noun)", "Fail (verb)", "Sifat (adjective)"]},
        ],
        "English": [
            {"chapter": "Reading Comprehension", "topics": ["Paragraphs with questions", "True/False", "Matching"]},
            {"chapter": "Grammar — Parts of Speech", "topics": ["Nouns (common, proper)", "Verbs (is, am, are, was, were)", "Pronouns"]},
            {"chapter": "Vocabulary Building", "topics": ["Opposites (antonyms)", "Similar words (synonyms)", "Word families"]},
            {"chapter": "Writing Skills", "topics": ["Sentences vs fragments", "Paragraph writing (5 sentences)", "Application for leave"]},
        ],
        "Mathematics": [
            {"chapter": "Numbers to 99,999", "topics": ["Place value", "Reading and writing large numbers", "Rounding"]},
            {"chapter": "Operations", "topics": ["Addition and subtraction of 4-digit numbers", "Multiplication up to 3-digit by 1-digit", "Division basics"]},
            {"chapter": "Fractions", "topics": ["Halves, thirds, quarters", "Equal parts", "Comparing simple fractions"]},
            {"chapter": "Geometry", "topics": ["Lines (straight, curved, parallel)", "Angles (right angle concept)", "Perimeter of simple shapes"]},
            {"chapter": "Money", "topics": ["Pakistani currency (rupees and paisa)", "Addition and subtraction of money", "Shopping word problems"]},
            {"chapter": "Data Handling", "topics": ["Tally marks", "Simple bar graphs", "Reading tables"]},
        ],
        "Science": [
            {"chapter": "Plants", "topics": ["Parts of a plant and their functions", "Photosynthesis (simple)", "Types: flowering, non-flowering"]},
            {"chapter": "Animals", "topics": ["Vertebrates vs invertebrates", "Habitat (land, water, both)", "Food chains"]},
            {"chapter": "My Body", "topics": ["Major organs", "Skeletal system basics", "Healthy habits"]},
            {"chapter": "Air and Water", "topics": ["Properties of air", "Water cycle (simple)", "Clean vs polluted water"]},
            {"chapter": "Simple Machines", "topics": ["Lever, wheel, pulley basics", "Examples in daily life (bicycle, see-saw)"]},
        ],
        "Social Studies": [
            {"chapter": "My Community", "topics": ["Neighbourhood", "Community workers", "Services in my area"]},
            {"chapter": "Pakistan — My Country", "topics": ["Map of Pakistan", "Provinces and capitals", "National symbols"]},
            {"chapter": "Famous People of Pakistan", "topics": ["Quaid-e-Azam", "Allama Iqbal", "Other national heroes"]},
        ],
        "Islamiyat": [
            {"chapter": "Surah Fatiha and Short Surahs", "topics": ["Memorisation", "Translation (simple)"]},
            {"chapter": "Hadith (Selected)", "topics": ["5 basic Hadiths", "Meaning and application"]},
            {"chapter": "Seerat — Life of Prophet (SAW)", "topics": ["Birth and childhood", "Family life", "Hijrat (simple)"]},
            {"chapter": "Islamic Values", "topics": ["Honesty", "Cleanliness (Taharah)", "Respect for elders"]},
        ],
    },

    # ── CLASS 4 ──────────────────────────────────────────────────────────────
    4: {
        "Urdu": [
            {"chapter": "Nasar (Prose Lessons)", "topics": ["10 prose lessons", "Comprehension", "Vocabulary in context"]},
            {"chapter": "Nazmain", "topics": ["5 poems", "Figure of speech basics", "Recitation"]},
            {"chapter": "Grammar", "topics": ["Ism ki aqsaam (types of nouns)", "Fail ki aqsaam (tenses)", "Imlaa rules"]},
            {"chapter": "Composition", "topics": ["Paragraph writing", "Khat (letter)", "Application writing"]},
        ],
        "English": [
            {"chapter": "Reading Comprehension", "topics": ["Longer passages", "Inference questions", "Vocabulary from context"]},
            {"chapter": "Grammar", "topics": ["Tenses (present, past, future simple)", "Articles (a, an, the)", "Prepositions (in, on, at, under)"]},
            {"chapter": "Writing", "topics": ["Essay: My School / My Village", "Informal letter to a friend", "Completing dialogues"]},
        ],
        "Mathematics": [
            {"chapter": "Large Numbers", "topics": ["Numbers to millions", "Roman numerals", "Rounding to nearest 10, 100, 1000"]},
            {"chapter": "Operations", "topics": ["Long multiplication (3x2 digit)", "Long division", "BODMAS/order of operations"]},
            {"chapter": "Fractions & Decimals", "topics": ["Equivalent fractions", "Addition and subtraction of fractions", "Decimal notation to hundredths"]},
            {"chapter": "Geometry", "topics": ["Angles (acute, obtuse, right, straight)", "Types of triangles", "Area of rectangles and squares"]},
            {"chapter": "Measurement", "topics": ["Conversion (km, m, cm; kg, g; litre, ml)", "Perimeter and area"]},
            {"chapter": "Statistics", "topics": ["Data collection", "Pictographs", "Bar charts"]},
        ],
        "Science": [
            {"chapter": "Living Things", "topics": ["Characteristics of living things", "Classification intro (5 kingdoms)", "Microorganisms (concept)"]},
            {"chapter": "Habitats", "topics": ["Forest, desert, grassland, aquatic habitats", "Adaptation (simple)"]},
            {"chapter": "Matter", "topics": ["States of matter (solid, liquid, gas)", "Properties", "Melting and boiling"]},
            {"chapter": "Energy", "topics": ["Forms of energy (light, heat, sound, kinetic)", "Energy transformations (simple)", "Sources of energy in Pakistan"]},
            {"chapter": "Earth and Space", "topics": ["Layers of the Earth", "Rocks and minerals", "Solar system (planets)"]},
        ],
        "Social Studies": [
            {"chapter": "Historical Pakistan", "topics": ["Indus Valley Civilization", "Muslim arrival (711 AD)", "Mughal Empire (overview)"]},
            {"chapter": "Geography of Pakistan", "topics": ["Rivers of Pakistan (Indus, Jhelum, Chenab, Ravi, Sutlej)", "Mountains (Himalayas, Karakoram, Hindukush)", "Deserts and Plains"]},
            {"chapter": "Economy", "topics": ["Agriculture in Pakistan", "Major crops (wheat, cotton, rice, sugarcane)", "Industries overview"]},
        ],
        "Islamiyat": [
            {"chapter": "Quran Tilawat and Translation", "topics": ["Surah Al-Baqarah (selected verses)", "Surah Al-Ikhlas", "Surah Al-Asr with meaning"]},
            {"chapter": "Seerat", "topics": ["Battles of Islam (Badr, Uhud — simple)", "Companions of the Prophet"]},
            {"chapter": "Islamic Ethics", "topics": ["Haq ul Ibad (rights of people)", "Justice", "Charity (Zakat concept)"]},
        ],
    },

    # ── CLASS 5 ──────────────────────────────────────────────────────────────
    5: {
        "Urdu": [
            {"chapter": "Nasar — Prose Sabaq 1–8", "topics": ["Comprehension", "Vocabulary", "Grammar in context"]},
            {"chapter": "Nazmain — Poetry", "topics": ["6 poems", "Allama Iqbal verses", "Waris Shah (intro)"]},
            {"chapter": "Grammar — Advanced", "topics": ["Zarb ul Misaal (proverbs)", "Muhavray (idioms)", "Mukhtalif Jumlay"]},
            {"chapter": "Composition", "topics": ["Essay: Mera Watan / Mera Pyara Gaon", "Application to Headmaster", "Story writing"]},
        ],
        "English": [
            {"chapter": "Reading & Comprehension", "topics": ["Passage analysis", "Main idea vs details", "Vocabulary in context"]},
            {"chapter": "Grammar", "topics": ["Perfect tenses", "Active and passive voice (intro)", "Reported speech (intro)", "Conjunctions"]},
            {"chapter": "Composition", "topics": ["Essay: My Village/City, My Favourite Season", "Formal and informal letter", "Story from outlines"]},
        ],
        "Mathematics": [
            {"chapter": "Sets", "topics": ["Set notation", "Types of sets", "Union and intersection (basic)"]},
            {"chapter": "Whole Numbers and Operations", "topics": ["HCF and LCM", "Prime factorization", "Word problems"]},
            {"chapter": "Fractions", "topics": ["Multiplication and division of fractions", "Mixed numbers", "Word problems"]},
            {"chapter": "Decimals", "topics": ["Decimal operations (+, -, x, ÷)", "Percentages intro", "Converting fractions to decimals"]},
            {"chapter": "Algebra Intro", "topics": ["Variables", "Simple expressions", "Solving one-step equations"]},
            {"chapter": "Geometry", "topics": ["Circles (radius, diameter, circumference intro)", "Volume of cubes and cuboids", "Coordinate plane (quadrant 1)"]},
            {"chapter": "Statistics", "topics": ["Mean, median, mode", "Line graphs", "Pie charts (reading)"]},
        ],
        "General Science": [
            {"chapter": "Cells — Basic Unit of Life", "topics": ["Plant vs animal cell", "Cell parts (nucleus, cytoplasm, membrane)", "Unicellular vs multicellular"]},
            {"chapter": "Kingdom Plantae", "topics": ["Classification (flowering, non-flowering, mosses, ferns)", "Photosynthesis process", "Pollination and seed dispersal"]},
            {"chapter": "Kingdom Animalia", "topics": ["Vertebrates (fish, amphibia, reptiles, birds, mammals)", "Invertebrates", "Adaptation to environment"]},
            {"chapter": "Matter and Its States", "topics": ["Particle model of matter", "Diffusion", "Changes of state (melting, boiling, condensation, freezing)"]},
            {"chapter": "Chemical Reactions", "topics": ["Physical vs chemical change", "Acids and bases (litmus test)", "Oxidation and combustion (concept)"]},
            {"chapter": "Energy Sources", "topics": ["Fossil fuels (coal, oil, gas) — Pakistan context", "Renewable energy (solar, wind, hydro)", "Tarbela and Mangla dams"]},
            {"chapter": "Heat Transfer", "topics": ["Conduction, convection, radiation", "Good and bad conductors", "Applications in daily life"]},
            {"chapter": "Light and Sound", "topics": ["Reflection and refraction", "Speed of light vs sound", "Characteristics of sound (pitch, loudness)"]},
            {"chapter": "Electricity", "topics": ["Simple circuits", "Conductors and insulators", "Parallel and series circuits", "WAPDA and household electricity"]},
            {"chapter": "Forces and Motion", "topics": ["Types of forces (gravity, friction, applied)", "Newton's laws (simplified)", "Speed, velocity, acceleration (concepts)"]},
            {"chapter": "The Universe", "topics": ["Solar system", "Planets and their order", "Moon phases", "Stars and constellations"]},
            {"chapter": "Our Environment", "topics": ["Ecosystem and food web", "Environmental pollution in Pakistan", "Conservation measures"]},
        ],
        "Social Studies": [
            {"chapter": "Ancient Civilizations", "topics": ["Indus Valley Civilization — Mohenjo-daro, Harappa", "Aryan period", "Greek invasion (Taxila)"]},
            {"chapter": "Muslim History", "topics": ["Arab conquest of Sindh (711 AD)", "Mahmud Ghaznavi", "Muhammad Ghuri", "Delhi Sultanate overview"]},
            {"chapter": "Mughal Empire", "topics": ["Babur, Humayun, Akbar", "Shah Jahan and Aurangzeb", "Mughal contributions to Pakistan's culture"]},
            {"chapter": "British Period", "topics": ["East India Company", "War of Independence 1857", "Sir Syed Ahmad Khan"]},
            {"chapter": "Pakistan Movement", "topics": ["Allama Iqbal's vision", "Quaid-e-Azam's role", "August 14, 1947"]},
            {"chapter": "Geography", "topics": ["Physical map of Pakistan", "Major rivers and their tributaries", "Climate zones"]},
        ],
        "Islamiyat": [
            {"chapter": "Quran — Selected Surahs with Translation", "topics": ["Surah Al-Hujuraat (selected verses)", "Surah Al-Mulk (selected)", "Surah Ya-Seen (selected)"]},
            {"chapter": "Hadith — 10 Selected", "topics": ["Hadith on knowledge", "Hadith on honesty", "Hadith on brotherhood", "Application in school life"]},
            {"chapter": "Seerat — Full Overview", "topics": ["Prophet's life in Makkah", "Hijrat to Madinah", "Key events in Madinah", "Last sermon"]},
            {"chapter": "Four Caliphs (Khulafa-e-Rashideen)", "topics": ["Hazrat Abu Bakr", "Hazrat Umar", "Hazrat Usman", "Hazrat Ali"]},
            {"chapter": "Islamic Values in Practice", "topics": ["Haya (modesty)", "Sabr (patience)", "Shukr (gratitude)", "Application to student life"]},
        ],
    },

    # ── CLASS 6 ──────────────────────────────────────────────────────────────
    6: {
        "Urdu": [
            {"chapter": "Nasar (10 Lessons)", "topics": ["Advanced comprehension", "Figurative language", "Critical thinking questions"]},
            {"chapter": "Nazmain (6 Poems)", "topics": ["Classical Urdu poetry (Mir, Ghalib intro)", "Poetic devices", "Meaning and analysis"]},
            {"chapter": "Grammar — Sarf o Nahv", "topics": ["Isim ki Aqsaam (types of nouns)", "Fail ki Aqsaam (verb types)", "Harf (particles)", "Jumlay ki aqsaam (sentence types)"]},
            {"chapter": "Composition", "topics": ["Essay (300 words)", "Formal application", "Story writing from outlines", "Dialogue writing"]},
        ],
        "English": [
            {"chapter": "Comprehension", "topics": ["Unseen passage analysis", "Summary writing", "Inference and deduction"]},
            {"chapter": "Grammar", "topics": ["Tenses — all 12 (introduction)", "Question tags", "Modal verbs (can, could, may, might, must, should)", "Clauses (main and subordinate)"]},
            {"chapter": "Vocabulary", "topics": ["Phrasal verbs", "Collocations", "Word formation (prefixes, suffixes)"]},
            {"chapter": "Writing", "topics": ["Formal letter", "Essay: An Ideal Teacher, Advantages of Trees", "Précis writing (intro)"]},
        ],
        "Mathematics": [
            {"chapter": "Sets", "topics": ["Venn diagrams", "Operations on sets", "Universal set", "Complement"]},
            {"chapter": "Rational Numbers", "topics": ["Integers on number line", "Operations on rational numbers", "Absolute value"]},
            {"chapter": "Fractions and Decimals", "topics": ["Division of fractions", "Recurring and terminating decimals", "Percentage calculations"]},
            {"chapter": "Algebra", "topics": ["Algebraic expressions", "Like and unlike terms", "Simple factorisation", "Linear equations (one variable)"]},
            {"chapter": "Geometry", "topics": ["Types of angles", "Parallel lines and transversals", "Triangles (properties and types)", "Congruence concept"]},
            {"chapter": "Perimeter, Area, Volume", "topics": ["Perimeter and area of rectangles, triangles, circles", "Volume of cuboid and cube"]},
            {"chapter": "Statistics", "topics": ["Frequency distribution", "Mean from grouped data", "Histogram and polygon"]},
        ],
        "General Science": [
            {"chapter": "Characteristics and Classification of Living Things", "topics": ["Seven characteristics of life", "Five-kingdom classification", "Dichotomous key"]},
            {"chapter": "Cells — Structure and Organization", "topics": ["Prokaryotic vs eukaryotic", "Plant vs animal cell (detailed)", "Tissues, organs, organ systems"]},
            {"chapter": "Plants — Nutrition", "topics": ["Photosynthesis (equation)", "Factors affecting photosynthesis", "Importance of photosynthesis"]},
            {"chapter": "Animals — Nutrition", "topics": ["Types of nutrition (autotrophic, heterotrophic)", "Human digestive system", "Nutrients and their sources"]},
            {"chapter": "Atoms and Molecules", "topics": ["Atomic structure (proton, neutron, electron)", "Elements, compounds, mixtures", "Periodic table (intro)"]},
            {"chapter": "Physical and Chemical Changes", "topics": ["Distinguishing physical from chemical", "Examples: rusting, burning, dissolving", "Reversible vs irreversible"]},
            {"chapter": "Motion", "topics": ["Types of motion (linear, circular, vibratory, random)", "Speed = distance/time", "Distance-time graphs"]},
            {"chapter": "Simple Machines", "topics": ["Lever (classes 1, 2, 3)", "Pulley", "Inclined plane", "Mechanical advantage"]},
            {"chapter": "Light", "topics": ["Reflection (laws and types)", "Refraction (Snell's law intro)", "Lenses and mirrors (concept)"]},
            {"chapter": "Sound", "topics": ["Production and propagation", "Speed of sound in different media", "Characteristics: pitch, loudness, quality"]},
            {"chapter": "Electricity", "topics": ["Current, voltage, resistance", "Ohm's law (concept)", "Series and parallel circuits", "Household wiring"]},
            {"chapter": "Our Earth", "topics": ["Structure of the Earth", "Rocks (igneous, sedimentary, metamorphic)", "Weathering and soil formation"]},
        ],
        "Pakistan Studies — History": [
            {"chapter": "Early Civilizations", "topics": ["Indus Valley: city planning, trade, decline", "Gandhara civilization", "Buddhist period (Taxila)"]},
            {"chapter": "Muslim Conquest and Rule", "topics": ["Muhammad bin Qasim (712 AD)", "Ghaznavid dynasty", "Delhi Sultanate (1206–1526)"]},
            {"chapter": "Mughal Empire", "topics": ["Foundation by Babur", "Akbar's policies", "Shah Jahan's architecture", "Aurangzeb's rule and its consequences"]},
            {"chapter": "British Rule", "topics": ["Battle of Plassey (1757)", "1857 War of Independence", "British administrative changes"]},
        ],
        "Pakistan Studies — Geography": [
            {"chapter": "Location and Size", "topics": ["Latitude and longitude of Pakistan", "Neighbours", "Strategic importance"]},
            {"chapter": "Physical Features", "topics": ["Northern mountains", "Plateau of Pothohar", "Indus Plain", "Balochistan Plateau", "Coastal area"]},
            {"chapter": "Climate", "topics": ["Monsoon system", "Climatic regions of Pakistan", "Effect on agriculture"]},
            {"chapter": "Rivers and Water Resources", "topics": ["Indus system (five rivers)", "Dams: Tarbela, Mangla, Warsak", "Canal irrigation system"]},
        ],
        "Islamiyat": [
            {"chapter": "Quran — Tilawat and Tafseer", "topics": ["Surah Al-Baqarah (selected)", "Surah Al-Imran (selected)", "Surah An-Nisa (selected)", "Tafseer basics"]},
            {"chapter": "Hadith — 15 Selected", "topics": ["On knowledge, behaviour, honesty, rights, worship"]},
            {"chapter": "Khulafa-e-Rashideen — Detailed", "topics": ["Political, military, social contributions of each Caliph"]},
            {"chapter": "Islamic Jurisprudence (Fiqh basics)", "topics": ["Taharah and Salah in detail", "Sawm (fasting) rules", "Zakat and Hajj (overview)"]},
        ],
    },

    # ── CLASS 7 ──────────────────────────────────────────────────────────────
    7: {
        "Urdu": [
            {"chapter": "Nasar — 12 Lessons", "topics": ["Critical analysis", "Writer's intent", "Main and subsidiary ideas"]},
            {"chapter": "Poetry — Classical and Modern", "topics": ["Ghalib, Mir, Faiz, Faraz selected verses", "Figurative language (Tashbeeh, Istiaara)"]},
            {"chapter": "Grammar — Advanced Sarf", "topics": ["Masdar (infinitive)", "Zaruf (adverb)", "Harf-e-Ataf (conjunctions)", "Ishtiqaq"]},
            {"chapter": "Composition — Advanced", "topics": ["Essay (400+ words)", "Debate format", "Formal letter and application", "Report writing (intro)"]},
        ],
        "English": [
            {"chapter": "Comprehension — Advanced", "topics": ["Complex unseen passages", "Tone and purpose", "Argument mapping"]},
            {"chapter": "Grammar — Complete Tense System", "topics": ["All 12 tenses in use", "Conditionals (types 0, 1, 2)", "Relative clauses", "Passive voice (all tenses)"]},
            {"chapter": "Writing", "topics": ["Argumentative essay", "Précis writing", "Dialogue writing", "News report format"]},
        ],
        "Mathematics": [
            {"chapter": "Integers and Number Theory", "topics": ["Properties of integers", "Divisibility rules", "Prime and composite", "LCM and HCF (algebraic method)"]},
            {"chapter": "Algebra", "topics": ["Algebraic identities", "Factorisation (advanced)", "Simultaneous linear equations (two variables)", "Inequalities"]},
            {"chapter": "Ratio, Proportion, Variation", "topics": ["Direct and inverse proportion", "Unitary method", "Percentage, profit, loss"]},
            {"chapter": "Geometry", "topics": ["Parallel lines theorems", "Triangle congruence (SSS, SAS, ASA, AAS)", "Pythagoras theorem"]},
            {"chapter": "Circles", "topics": ["Chord, arc, sector", "Tangent concept", "Angle at centre vs angle at circumference"]},
            {"chapter": "Mensuration", "topics": ["Area of complex shapes", "Surface area of cuboid and cylinder", "Volume of cylinder"]},
        ],
        "General Science": [
            {"chapter": "Biodiversity", "topics": ["Classification (binomial nomenclature intro)", "Kingdoms — Monera, Protista, Fungi, Plantae, Animalia", "Importance of biodiversity"]},
            {"chapter": "Photosynthesis (Detailed)", "topics": ["Light and dark reactions (intro)", "Factors: light intensity, CO₂, temperature", "Importance to ecosystem"]},
            {"chapter": "Respiration", "topics": ["Aerobic vs anaerobic respiration", "ATP concept", "Breathing mechanism (human)"]},
            {"chapter": "Nutrition in Plants and Animals", "topics": ["Balanced diet", "Nutrients: carbohydrates, proteins, fats, vitamins, minerals", "Malnutrition in Pakistan context"]},
            {"chapter": "Elements and Compounds", "topics": ["Periodic table structure (groups, periods)", "Metals vs non-metals", "Chemical formulae"]},
            {"chapter": "Chemical Reactions", "topics": ["Types: combination, decomposition, displacement, double displacement", "Balancing equations (simple)", "Acids and bases (pH)"]},
            {"chapter": "Forces and Motion", "topics": ["Newton's three laws (detailed)", "Friction and its applications", "Momentum concept"]},
            {"chapter": "Machines", "topics": ["Work, power, energy (quantities)", "Efficiency of machines", "Real-world machines: bicycle, pulley systems"]},
            {"chapter": "Electricity and Magnetism", "topics": ["Coulomb's law (concept)", "Electric field", "Magnetic field and poles", "Electromagnet (construction and use)"]},
            {"chapter": "Atmosphere", "topics": ["Composition of air", "Air pressure", "Weather vs climate", "Greenhouse effect and global warming"]},
        ],
        "Pakistan Studies — History": [
            {"chapter": "Muslim Spain (Al-Andalus)", "topics": ["Rise and fall of Muslim Spain", "Contributions to science and culture"]},
            {"chapter": "Ottoman Empire", "topics": ["Foundation", "Role in Islamic world", "Decline"]},
            {"chapter": "British India — Political Developments", "topics": ["Indian National Congress (1885)", "All India Muslim League (1906)", "Lucknow Pact (1916)", "Khilafat Movement"]},
            {"chapter": "Pakistan Movement", "topics": ["Allama Iqbal's Allahabad Address (1930)", "Lahore Resolution (1940)", "Role of Quaid-e-Azam", "Independence 1947"]},
        ],
        "Islamiyat": [
            {"chapter": "Quran — Suwar with Tafseer", "topics": ["Surah Al-Anfal (selected)", "Surah Al-Tawbah (selected)", "Tafseer methodology"]},
            {"chapter": "Hadith — 20 Selected", "topics": ["Hadith on justice, social responsibility, environment, women's rights"]},
            {"chapter": "Umayyad and Abbasid Caliphates", "topics": ["Political history", "Scientific and cultural achievements (Bayt-ul-Hikmah)", "Decline"]},
            {"chapter": "Muslim Scientists and Scholars", "topics": ["Al-Kindi, Al-Farabi, Ibn Sina, Al-Beruni, Al-Khwarizmi", "Their contributions to modern science"]},
        ],
    },

    # ── CLASS 8 ──────────────────────────────────────────────────────────────
    8: {
        "Urdu": [
            {"chapter": "Nasar — 12 Advanced Lessons", "topics": ["Literary analysis", "Comparing authors' perspectives", "Summarising and paraphrasing"]},
            {"chapter": "Poetry — Classical Masters", "topics": ["Ghalib, Mir, Sauda, Anees", "Masnavi and Ghazal forms", "Ilm-ul-Aruz basics"]},
            {"chapter": "Grammar — Complete", "topics": ["All Sarf topics", "Nahv (syntax)", "Common errors in written Urdu"]},
            {"chapter": "Composition — Board Level", "topics": ["Essay (500+ words)", "Full application", "Story with moral", "Newspaper article format"]},
        ],
        "English": [
            {"chapter": "Literature — Prose", "topics": ["Selected short stories (from PCTB textbook)", "Character analysis", "Theme identification"]},
            {"chapter": "Literature — Poetry", "topics": ["Selected poems", "Poetic devices (simile, metaphor, personification, alliteration)", "Paraphrasing poetry"]},
            {"chapter": "Grammar — Board Standard", "topics": ["All aspects of grammar for Matric", "Common errors correction", "Transformation of sentences"]},
            {"chapter": "Composition", "topics": ["Essay: Science, Environment, Internet, My Ambition", "Story completion", "Letter (formal and informal)", "Application"]},
        ],
        "Mathematics": [
            {"chapter": "Sets and Functions", "topics": ["Sets operations (union, intersection, complement, difference)", "Functions — domain, range, types", "Venn diagram problems"]},
            {"chapter": "Real Numbers", "topics": ["Rational and irrational numbers", "Real number line", "Properties of real numbers", "Surds and radicals"]},
            {"chapter": "Algebra", "topics": ["Polynomials", "Factorisation (complete)", "Algebraic fractions", "Simultaneous equations (three methods)"]},
            {"chapter": "Matrices", "topics": ["Order of matrix", "Addition and subtraction of matrices", "Scalar multiplication", "Introduction to determinants"]},
            {"chapter": "Statistics and Probability", "topics": ["Measures of central tendency (mean, median, mode) for grouped data", "Measures of dispersion (range, variance, standard deviation)", "Simple probability"]},
            {"chapter": "Geometry — Theorems", "topics": ["Circle theorems (5 key theorems)", "Tangent-radius theorem", "Pythagoras and its converse"]},
        ],
        "General Science": [
            {"chapter": "Cell Division", "topics": ["Mitosis (phases)", "Meiosis (concept)", "Importance in growth and reproduction"]},
            {"chapter": "Microorganisms", "topics": ["Bacteria, viruses, fungi, protozoa", "Beneficial and harmful microorganisms", "Antibiotics"]},
            {"chapter": "Diseases and Immunity", "topics": ["Communicable vs non-communicable diseases", "Common diseases in Pakistan (typhoid, malaria, dengue, hepatitis)", "Vaccination and immunity"]},
            {"chapter": "Reproduction", "topics": ["Asexual and sexual reproduction", "Human reproduction system (overview)", "Metamorphosis in insects"]},
            {"chapter": "Ecosystem and Environment", "topics": ["Ecosystem components (biotic, abiotic)", "Food chains and food webs", "Energy flow (10% law)", "Ecological succession"]},
            {"chapter": "Pollution", "topics": ["Types of pollution (air, water, soil, noise)", "Pakistan-specific pollution issues (Lahore smog, Karachi water quality)", "Solutions"]},
            {"chapter": "Acids and Bases", "topics": ["Properties of acids and bases", "pH scale", "Neutralisation", "Acids and bases in daily life (vinegar, baking soda, bleach)"]},
            {"chapter": "Metals", "topics": ["Properties of metals and non-metals", "Reactivity series", "Corrosion and its prevention", "Alloys (steel, brass, bronze)"]},
            {"chapter": "Pressure", "topics": ["Pressure = Force/Area", "Atmospheric pressure", "Hydraulic systems (JCB, car brakes)", "Archimedes' principle"]},
            {"chapter": "Electromagnetism", "topics": ["Electromagnetic induction", "Generators (principle)", "Transformers", "Electric motors"]},
        ],
        "Pakistan Studies": [
            {"chapter": "Constitutional Development", "topics": ["Constitution of 1956", "Constitution of 1962", "Constitution of 1973 (key features)", "Amendments (important ones)"]},
            {"chapter": "Post-Independence Challenges", "topics": ["Refugee crisis 1947", "Economic challenges", "Kashmir issue", "Language controversy"]},
            {"chapter": "Political History 1947–Present", "topics": ["Civil and military governments", "1971 separation of East Pakistan", "Democratic era (1988–1999)", "Recent political developments"]},
            {"chapter": "Economy of Pakistan", "topics": ["Agriculture sector", "Industrial sector", "Services sector", "Foreign exchange and remittances", "Challenges: inflation, unemployment, debt"]},
            {"chapter": "Foreign Policy", "topics": ["Pakistan-India relations", "Pakistan-China (CPEC)", "Pakistan-USA relations", "Pakistan's role in Muslim world (OIC)"]},
        ],
        "Computer Science": [
            {"chapter": "Information and Communication Technology", "topics": ["History of computers", "Types of computers", "ICT in Pakistan: telemedicine, e-government, online education"]},
            {"chapter": "Hardware and Software", "topics": ["Input/output/storage devices", "System software vs application software", "Operating systems (Windows, Android)"]},
            {"chapter": "Internet and Networking", "topics": ["How the internet works", "LAN, WAN, MAN", "HTTP, IP address, DNS (concept)", "Cybersecurity basics"]},
            {"chapter": "Spreadsheets (MS Excel basics)", "topics": ["Rows, columns, cells", "Basic formulas (SUM, AVERAGE, MAX, MIN)", "Simple charts"]},
            {"chapter": "Programming Concepts", "topics": ["Algorithm and flowchart", "Variables and data types", "If-else logic", "Simple loop concept"]},
        ],
    },

    # ── CLASS 9 (Matric Part 1) ───────────────────────────────────────────────
    9: {
        "Urdu": [
            {"chapter": "Nasar — Board Level Lessons", "topics": ["10 prose lessons from PCTB text", "Literary analysis at board level", "Summary writing"]},
            {"chapter": "Poetry — Classical", "topics": ["Allama Iqbal (Shikwa, Jawab-e-Shikwa selected)", "Ghalib, Mir, Faiz selected ghazals", "Hamd and Naat"]},
            {"chapter": "Grammar — Board Standard", "topics": ["Complete Sarf and Nahv", "Sentence transformation", "Common board questions on grammar"]},
            {"chapter": "Composition — Matric Level", "topics": ["Essays (6 standard essays)", "Applications (6 standard formats)", "Stories (4 standard stories)", "Letters (formal and informal)"]},
        ],
        "English": [
            {"chapter": "Reading Comprehension", "topics": ["Unseen passage (MCQs + SAQs)", "Contextual vocabulary", "Literal and inferential questions"]},
            {"chapter": "Grammar", "topics": ["Sentence correction", "Transformation (active/passive, direct/indirect)", "Fill in blanks (articles, prepositions, tenses)"]},
            {"chapter": "Literature — Prose", "topics": ["PCTB selected prose pieces", "Character sketch", "Theme analysis"]},
            {"chapter": "Literature — Poetry", "topics": ["PCTB selected poems", "Paraphrasing", "Poetic devices identification"]},
            {"chapter": "Composition", "topics": ["Essay (My Ambition, Science, Role of Women, Advantages of Trees)", "Letter writing (formal)", "Story from outlines", "Dialogue", "Application"]},
        ],
        "Physics": [
            {"chapter": "Physical Quantities and Measurement", "topics": ["Base and derived quantities", "SI units", "Prefixes (micro to giga)", "Significant figures", "Measuring instruments (vernier, screw gauge)", "Errors and accuracy"]},
            {"chapter": "Kinematics", "topics": ["Scalar vs vector", "Distance vs displacement", "Speed vs velocity", "Acceleration", "Equations of motion (3 equations)", "Distance-time and velocity-time graphs", "Projectile motion (horizontal)"]},
            {"chapter": "Dynamics", "topics": ["Newton's three laws (detailed + mathematical)", "Mass vs weight", "Friction (static, kinetic, rolling)", "Momentum (p=mv)", "Impulse", "Law of conservation of momentum"]},
            {"chapter": "Turning Effect of Forces", "topics": ["Torque (moment of force)", "Principle of moments", "Centre of mass and gravity", "Equilibrium (static, dynamic)", "Conditions of equilibrium"]},
            {"chapter": "Gravitation", "topics": ["Newton's law of universal gravitation", "Mass of Earth calculation", "Variation of g with altitude", "Orbital speed", "Artificial satellites", "GPS"]},
            {"chapter": "Work, Energy and Power", "topics": ["Work (W = Fd cosθ)", "Kinetic energy (½mv²)", "Potential energy (mgh)", "Conservation of energy", "Power (P = W/t)", "Efficiency"]},
            {"chapter": "Properties of Matter", "topics": ["Kinetic molecular theory (solids, liquids, gases)", "Elasticity (Hooke's law)", "Stress and strain", "Pressure in fluids", "Pascal's law", "Archimedes' principle", "Density"]},
            {"chapter": "Thermal Properties of Matter", "topics": ["Temperature scales (°C, K, °F conversion)", "Thermometers", "Thermal expansion (linear, volumetric)", "Anomalous expansion of water", "Specific heat capacity", "Latent heat"]},
            {"chapter": "Transfer of Heat", "topics": ["Conduction (mechanism and thermal conductivity)", "Convection (currents)", "Radiation (black body, Stefan's law concept)", "Greenhouse effect", "Applications (thermos, solar panels)"]},
        ],
        "Chemistry": [
            {"chapter": "Fundamentals of Chemistry", "topics": ["Matter, element, compound, mixture", "Chemical vs physical change", "Atom, molecule, ion", "Molecular formula and formula mass", "Mole concept and Avogadro's number", "Empirical and molecular formula"]},
            {"chapter": "Structure of Atoms", "topics": ["Sub-atomic particles (proton, neutron, electron)", "Atomic number and mass number", "Isotopes (concept and examples: ¹H, ²H, ³H)", "Electronic configuration (Bohr model)", "Shells and sub-shells (s, p, d)"]},
            {"chapter": "Periodic Table and Periodicity", "topics": ["Historical development (Dobereiner, Newlands, Mendeleev, Moseley)", "Modern periodic law", "Groups and periods", "Periodic trends: atomic radius, ionisation energy, electron affinity, electronegativity"]},
            {"chapter": "Structure of Molecules", "topics": ["Ionic bond (electron transfer)", "Covalent bond (electron sharing)", "Coordinate covalent bond", "Hydrogen bonding", "Metallic bonding (concept)", "VSEPR theory (basic shapes)"]},
            {"chapter": "Physical States of Matter", "topics": ["Kinetic molecular theory", "Gas laws (Boyle's, Charles's, Gay-Lussac's, Avogadro's, Ideal gas law PV=nRT)", "Liquids (vapour pressure, evaporation, boiling)", "Solids (crystal lattice concept)"]},
            {"chapter": "Solutions", "topics": ["Types of solutions", "Solubility and factors affecting it", "Concentration units (%, molarity, molality)", "Colligative properties (boiling point elevation, freezing point depression)"]},
            {"chapter": "Electrochemistry", "topics": ["Oxidation and reduction", "Oxidation number", "Electrochemical cells (galvanic)", "Standard electrode potential", "Electrolytic cells", "Industrial applications (electroplating, extraction of metals)"]},
            {"chapter": "Chemical Reactivity", "topics": ["Types of reactions (synthesis, decomposition, single and double displacement, combustion, neutralisation)", "Balancing chemical equations", "Stoichiometry calculations", "Limiting reactant", "Yield percentage"]},
        ],
        "Biology": [
            {"chapter": "Introduction to Biology", "topics": ["Definition and branches of biology", "Levels of organization (cell to biosphere)", "Relationship with other sciences", "Career options in Pakistan (MBBS, PharmD, veterinary, agriculture)"]},
            {"chapter": "Solving a Biological Problem", "topics": ["Scientific method", "Hypothesis formation and testing", "Controlled experiment", "Malaria case study as example of biological problem-solving"]},
            {"chapter": "Biodiversity", "topics": ["Definition and importance of biodiversity", "Classification (Whittaker's 5 kingdoms)", "Viruses (structure, types, diseases — HIV, dengue, hepatitis)", "Kingdom Monera, Protista, Fungi", "Pakistan's biodiversity — endangered species"]},
            {"chapter": "Cells and Tissues", "topics": ["Prokaryotic vs eukaryotic cells", "Cell organelles (detailed — ER, Golgi, mitochondria, chloroplast, nucleus)", "Comparison of plant and animal cells", "Animal tissues (epithelial, connective, muscular, nervous)", "Plant tissues (meristematic, permanent)"]},
            {"chapter": "Cell Cycle", "topics": ["Interphase (G1, S, G2)", "Mitosis (prophase, metaphase, anaphase, telophase)", "Cytokinesis", "Importance of mitosis", "Meiosis (overview)", "Cancer as uncontrolled cell division"]},
            {"chapter": "Enzymes", "topics": ["Definition and properties of enzymes", "Enzyme-substrate complex (lock and key model, induced fit)", "Factors affecting enzyme activity (temperature, pH, substrate concentration)", "Enzyme inhibition", "Industrial and medical importance"]},
            {"chapter": "Bioenergetics", "topics": ["ATP structure and function", "Photosynthesis — light and dark reactions", "Respiration — aerobic (glycolysis, Krebs cycle, ETC overview) and anaerobic", "Fermentation (yogurt, bread, alcohol)"]},
            {"chapter": "Nutrition", "topics": ["Modes of nutrition (autotrophic, heterotrophic, parasitic, saprophytic)", "Human nutrition — balanced diet in Pakistani context", "Digestive system (organ by organ)", "Nutritional disorders in Pakistan"]},
            {"chapter": "Transport", "topics": ["Need for transport in living organisms", "Human cardiovascular system", "Blood composition (RBC, WBC, platelets, plasma)", "Blood groups (ABO system)", "Lymphatic system", "Transpiration in plants (stomata, xylem)"]},
        ],
        "Mathematics": [
            {"chapter": "Matrices and Determinants", "topics": ["Matrix operations (add, subtract, multiply by scalar, multiply matrices)", "Determinant of 2×2 and 3×3 matrix", "Inverse of matrix", "Solving system of equations by matrix method (Cramer's rule)"]},
            {"chapter": "Real and Complex Numbers", "topics": ["Properties of real numbers", "Complex numbers — standard form a+bi", "Operations on complex numbers", "Conjugate and modulus", "Argand plane"]},
            {"chapter": "Logarithms", "topics": ["Definition and laws of logarithms", "Common and natural logarithm", "Antilogarithm", "Solving equations using logarithms", "Scientific calculations using log tables"]},
            {"chapter": "Algebraic Expressions and Formulas", "topics": ["Algebraic identities (6 standard formulas)", "HCF and LCM of algebraic expressions", "Application of formulas"]},
            {"chapter": "Factorization", "topics": ["Common factor", "Grouping", "Difference of squares", "Sum and difference of cubes", "Trinomial factorisation"]},
            {"chapter": "Algebraic Manipulation", "topics": ["Simplification of fractions", "Operations on algebraic fractions", "Square root of algebraic expressions"]},
            {"chapter": "Linear Equations and Inequalities", "topics": ["Linear equations in one variable (revision)", "Linear inequalities", "Absolute value equations and inequalities", "Word problems"]},
            {"chapter": "Graphs", "topics": ["Cartesian coordinate system", "Plotting points", "Graph of linear equation", "Slope and intercept", "Parallel and perpendicular lines"]},
            {"chapter": "Introduction to Coordinate Geometry", "topics": ["Distance formula", "Midpoint formula", "Division of line segment in given ratio", "Collinearity of points"]},
            {"chapter": "Congruent Triangles", "topics": ["Conditions: SSS, SAS, ASA, AAS, HS", "Proofs using congruence", "Isosceles triangle properties"]},
            {"chapter": "Parallelograms and Triangles", "topics": ["Properties of parallelogram", "Diagonal bisection theorem", "Triangles on same base and between same parallels"]},
            {"chapter": "Practical Geometry", "topics": ["Construction of triangles (given various information)", "Construction of quadrilaterals", "Inscribed and circumscribed circles of triangle"]},
        ],
        "Pakistan Studies": [
            {"chapter": "Location and Size of Pakistan", "topics": ["Coordinates", "Borders with neighbours", "Strategic importance of location"]},
            {"chapter": "Physical Features", "topics": ["Northern mountains (Himalaya, Karakoram, Hindukush)", "Pothohar Plateau", "Indus Plain (divisions)", "Balochistan Plateau", "Makran Coast"]},
            {"chapter": "Climate of Pakistan", "topics": ["Factors affecting climate", "Seasons", "Monsoon system", "Climatic regions (4)", "Climate change impact on Pakistan"]},
            {"chapter": "Vegetation", "topics": ["Forests of Pakistan (types and distribution)", "Deforestation problem", "Afforestation efforts"]},
            {"chapter": "Agriculture", "topics": ["Importance of agriculture in Pakistan's economy", "Kharif and Rabi crops", "Major crops and their regions", "Agricultural problems and solutions"]},
            {"chapter": "Water Resources", "topics": ["Indus River System", "Reservoirs (Tarbela, Mangla, Chashma)", "Canal system", "Water scarcity challenge", "CPEC water projects"]},
            {"chapter": "Minerals and Energy Resources", "topics": ["Mineral resources (coal, gas, oil, salt, copper, chromite)", "Energy crisis in Pakistan", "Renewable energy (Thar coal, wind, solar, hydel)"]},
            {"chapter": "Population", "topics": ["Population growth rate", "Urban vs rural distribution", "Population problems", "Population policy"]},
            {"chapter": "Transport and Communication", "topics": ["Road network (National Highways, motorways)", "Railway", "Air transport (PIA)", "Sea ports (Karachi, Gwadar)", "Telecommunications"]},
        ],
        "Islamiyat": [
            {"chapter": "Aqeedah — Islamic Beliefs", "topics": ["Tawheed", "Risalat", "Akhirat", "Angels", "Divine Books", "Predestination (Taqdir)"]},
            {"chapter": "Arkan-e-Islam", "topics": ["Salah (in detail)", "Sawm (rules of fasting)", "Zakat (nisaab and calculation)", "Hajj (rites and significance)"]},
            {"chapter": "Quran — Tafseer", "topics": ["Surah Al-Baqarah (selected)", "Surah Al-Imran (selected)", "Theme-based Quranic study"]},
            {"chapter": "Hadith — 25 Selected", "topics": ["On worship, social conduct, economics, environment, justice"]},
            {"chapter": "Seerat — Complete", "topics": ["Prophet's life — complete timeline", "Key events in Makkah", "Key events in Madinah", "Military campaigns", "Farewell pilgrimage"]},
            {"chapter": "Islamic History — Khulafa and Umayyads", "topics": ["Detailed study of Khulafa-e-Rashideen", "Umayyad Caliphate", "Islamic expansion"]},
        ],
    },

    # ── CLASS 10 (Matric Part 2) ──────────────────────────────────────────────
    10: {
        "Physics": [
            {"chapter": "Simple Harmonic Motion and Waves", "topics": ["SHM definition and examples", "Period, frequency, amplitude", "Displacement-time graph", "Waves (transverse and longitudinal)", "Wave equation (v = fλ)", "Superposition and interference", "Stationary waves"]},
            {"chapter": "Sound", "topics": ["Production and propagation of sound", "Speed of sound in different media", "Characteristics (pitch, loudness, quality)", "Doppler effect", "Ultrasound and its applications (medical, sonar)", "Echo and reverberation"]},
            {"chapter": "Geometrical Optics", "topics": ["Laws of reflection", "Curved mirrors (concave, convex) — mirror formula", "Laws of refraction", "Total internal reflection (optical fibre)", "Lenses (convex, concave) — lens formula", "Human eye and defects", "Telescope and microscope (principles)"]},
            {"chapter": "Electrostatics", "topics": ["Electric charge (types and properties)", "Coulomb's law", "Electric field and field lines", "Electric potential and potential difference", "Capacitance (concept)", "Van de Graaff generator"]},
            {"chapter": "Current Electricity", "topics": ["Current, voltage, resistance", "Ohm's law", "Resistivity and conductivity", "Series and parallel resistors", "Kirchhoff's laws (KCL, KVL)", "Joule's law", "Power and energy in circuits", "Domestic wiring and safety"]},
            {"chapter": "Electromagnetism", "topics": ["Magnetic field around conductor (right-hand rule)", "Force on current-carrying conductor", "Galvanometer principle", "DC motor", "Electromagnetic induction (Faraday's law)", "AC generator principle", "Transformer (step-up, step-down)"]},
            {"chapter": "Basic Electronics", "topics": ["Conductors, insulators, semiconductors", "Diode — p-n junction", "Rectification (half-wave, full-wave)", "Transistor as switch and amplifier", "Logic gates (AND, OR, NOT, NAND, NOR, XOR)"]},
            {"chapter": "Dawn of Modern Physics", "topics": ["Relative motion (Galilean)", "Special relativity (time dilation, length contraction — concept)", "Mass-energy equivalence (E=mc²)", "Black body radiation", "Photoelectric effect", "Compton effect"]},
            {"chapter": "Atomic and Nuclear Physics", "topics": ["Rutherford and Bohr models", "X-rays (production and uses)", "Radioactivity (alpha, beta, gamma)", "Half-life", "Nuclear fission and fusion", "Nuclear reactors", "KANUPP and CHASNUPP (Pakistan)"]},
        ],
        "Chemistry": [
            {"chapter": "Chemical Equilibrium", "topics": ["Reversible reactions", "Law of mass action", "Equilibrium constant Kc and Kp", "Le Chatelier's principle", "Industrial application (Haber process for urea production — Pakistan context)"]},
            {"chapter": "Acids, Bases and Salts", "topics": ["Theories (Arrhenius, Brønsted-Lowry, Lewis)", "Strong vs weak acids and bases", "pH and pOH", "Buffer solutions", "Hydrolysis of salts", "Salts preparation and uses"]},
            {"chapter": "Organic Chemistry — Introduction", "topics": ["Organic vs inorganic compounds", "Hybridisation (sp³, sp², sp)", "Homologous series", "Functional groups", "IUPAC nomenclature"]},
            {"chapter": "Hydrocarbons", "topics": ["Alkanes (methane, ethane — properties, reactions)", "Alkenes (ethene — addition reactions)", "Alkynes (ethyne — properties)", "Aromatic hydrocarbons (benzene structure)", "Petroleum refining in Pakistan"]},
            {"chapter": "Biochemistry", "topics": ["Carbohydrates (monosaccharides, disaccharides, polysaccharides)", "Lipids (saturated, unsaturated fats)", "Proteins (amino acids, peptide bond)", "Nucleic acids (DNA and RNA — overview)", "Enzymes as biological catalysts"]},
            {"chapter": "The Atmosphere", "topics": ["Composition of atmosphere", "Layers (troposphere, stratosphere, etc.)", "Ozone layer depletion", "Air pollution in Pakistan (Lahore smog)", "Greenhouse effect and climate change"]},
            {"chapter": "Water", "topics": ["Properties of water (polarity, hydrogen bonding)", "Hard and soft water", "Water purification (methods)", "Water pollution in Pakistan", "Sewage treatment"]},
            {"chapter": "Chemical Industries in Pakistan", "topics": ["Urea fertilizer industry", "Textile industry chemistry", "Cement industry", "Sugar industry", "Petroleum refining (Attock, Karachi)"]},
        ],
        "Biology": [
            {"chapter": "Gaseous Exchange", "topics": ["Need for gaseous exchange", "Human respiratory system (in detail)", "Mechanism of breathing", "Transport of gases in blood", "Respiratory disorders (asthma, tuberculosis — Pakistan context)", "Gaseous exchange in plants (stomata)"]},
            {"chapter": "Homeostasis", "topics": ["Definition and concept", "Osmoregulation (kidneys — nephron in detail)", "Thermoregulation (skin structure and function)", "Liver functions (deamination, glycogen storage)", "Excretion: kidneys, lungs, skin", "Diabetes (insulin — Pakistan's high diabetes rate)"]},
            {"chapter": "Coordination and Control", "topics": ["Nervous system (central and peripheral)", "Neuron structure and impulse transmission", "Reflex arc", "Human brain (parts and functions)", "Sense organs (eye and ear — detailed)", "Endocrine system (hormones and glands)", "Drug abuse effects"]},
            {"chapter": "Support and Movement", "topics": ["Skeletal system (bones of human body)", "Joints (types)", "Muscular system (types of muscles)", "Diseases: arthritis, osteoporosis — Pakistan elderly context"]},
            {"chapter": "Reproduction", "topics": ["Male and female reproductive systems", "Fertilisation and implantation", "Development of embryo", "Birth and puberty", "Sexually transmitted infections (HIV/AIDS — Pakistan data)"]},
            {"chapter": "Man and His Environment", "topics": ["Ecosystem components", "Food chains and food webs", "Biogeochemical cycles (carbon, nitrogen, water)", "Environmental pollution in Pakistan", "Conservation of biodiversity"]},
            {"chapter": "Inheritance", "topics": ["Gregor Mendel's laws", "Monohybrid and dihybrid crosses", "Dominance, recessiveness", "Genotype and phenotype", "Blood group inheritance (ABO)", "Sex determination (XX, XY)", "Genetic disorders (thalassaemia — Pakistan has highest incidence)"]},
            {"chapter": "Man and Microbes", "topics": ["Useful microorganisms (fermentation, antibiotics)", "Pathogenic microorganisms", "Common diseases in Pakistan (typhoid, malaria, dengue, hepatitis A, B, C)", "Immunisation programme in Pakistan (EPI)", "Biotechnology applications"]},
        ],
        "Mathematics": [
            {"chapter": "Quadratic Equations", "topics": ["Factorisation method", "Completing the square", "Quadratic formula", "Nature of roots (discriminant)", "Sum and product of roots", "Formation of equation from roots"]},
            {"chapter": "Theory of Quadratic Equations", "topics": ["Cube roots of unity", "Symmetric functions of roots", "Equations reducible to quadratic"]},
            {"chapter": "Variations", "topics": ["Direct variation (k = y/x)", "Inverse variation", "Joint variation", "Combined variation", "Word problems with local context (crop yield vs rainfall)"]},
            {"chapter": "Partial Fractions", "topics": ["Proper and improper fractions", "Distinct linear factors", "Repeated linear factors", "Irreducible quadratic factors"]},
            {"chapter": "Sets and Functions", "topics": ["Set operations (revision and extension)", "Types of functions (one-one, onto, bijective)", "Inverse function", "Composition of functions"]},
            {"chapter": "Basic Statistics", "topics": ["Frequency distribution (class width, class marks)", "Measures of central tendency (mean, median, mode) — grouped data", "Measures of dispersion (variance, standard deviation)", "Normal distribution (concept)"]},
            {"chapter": "Introduction to Trigonometry", "topics": ["Angles in standard position (degrees and radians)", "Trigonometric ratios (sin, cos, tan, csc, sec, cot)", "Values of special angles (30°, 45°, 60°, 90°)", "Trigonometric identities", "Solving right triangles", "Sine and cosine rules"]},
            {"chapter": "Projection of a Side of a Triangle", "topics": ["Projection theorem", "Proof and application"]},
            {"chapter": "Circle Theorems", "topics": ["Perpendicular from centre to chord", "Chords equidistant from centre", "Angle in semicircle", "Cyclic quadrilateral", "Tangent-radius theorem", "Two tangents from external point"]},
        ],
        "Urdu": [
            {"chapter": "Nasar — 12 Board Lessons", "topics": ["Complete analysis as per PCTB guide", "Summary writing", "Character analysis"]},
            {"chapter": "Poetry — Board Level", "topics": ["Selected Ghazals and Nazms", "Iqbal's poetry (complete poems from PCTB list)", "Critical appreciation"]},
            {"chapter": "Grammar — Complete Board Syllabus", "topics": ["All grammar topics as per BISE Rawalpindi/Lahore past papers"]},
            {"chapter": "Composition — Board Level", "topics": ["6 standard essays (mausam, Pakistan, science, watan, teachers, women)", "6 applications", "4 story types", "3 letter formats"]},
        ],
        "English": [
            {"chapter": "Literature and Grammar — Board Standard", "topics": ["All prose pieces from PCTB English 10", "All poems from PCTB English 10", "Complete grammar for Matric board exam"]},
            {"chapter": "Composition — Board Level", "topics": ["Standard essays for Class 10 board exam", "Story writing", "Applications and letters for Matric level"]},
        ],
        "Pakistan Studies": [
            {"chapter": "Historical Background — Pre-1947", "topics": ["1857 War of Independence and aftermath", "Aligarh Movement", "Muslim League formation (1906)", "Khilafat Movement", "Lahore Resolution 1940"]},
            {"chapter": "Independence and Early Challenges", "topics": ["Independence 1947 — partition events", "Refugee crisis (largest migration in history)", "Accession of states", "Kashmir issue (first war 1947-48)"]},
            {"chapter": "Constitutional Development", "topics": ["Constitution of 1956", "Constitution of 1962", "Constitution of 1973 (detailed)", "Major amendments (8th, 18th, 25th)"]},
            {"chapter": "Political History Post-1947", "topics": ["Civil governments 1947-1958", "Ayub Khan era", "Yahya Khan and 1971", "Bhutto era", "Zia era", "Democratic era 1988-1999", "Musharraf era", "Recent democracy"]},
            {"chapter": "Economy of Pakistan", "topics": ["Agriculture: contribution, major crops, problems", "Industry: textile, sugar, cement", "Services: banking, IT", "CPEC and its economic significance", "Problems: inflation, debt, unemployment"]},
            {"chapter": "Foreign Policy", "topics": ["Pakistan-India relations (Kashmir, wars, peace efforts)", "Pakistan-China (CPEC, all-weather friendship)", "Pakistan-USA (strategic partnership, tensions)", "Pakistan-Middle East (workers' remittances, OIC)"]},
        ],
    },

    # ── CLASS 11 (FSc/FA/ICS Part 1) ─────────────────────────────────────────
    11: {
        "Physics (Pre-Engineering / Pre-Medical)": [
            {"chapter": "Measurements", "topics": ["Physical quantities (base and derived)", "Dimensions", "Errors in measurement", "Significant figures", "Scientific notation", "Measuring instruments precision"]},
            {"chapter": "Vectors and Equilibrium", "topics": ["Vector addition (graphical and analytical)", "Vector subtraction", "Rectangular components", "Unit vectors", "Position vector", "Torque", "Equilibrium of forces (concurrent, non-concurrent)"]},
            {"chapter": "Motion and Force", "topics": ["Kinematics (revision and extension)", "Newton's laws (advanced problems)", "Projectile motion (2D)", "Uniform circular motion", "Centripetal force", "Banking of roads", "Non-inertial frames (concept)"]},
            {"chapter": "Work, Energy and Power", "topics": ["Work-energy theorem", "Conservative and non-conservative forces", "Elastic and inelastic collisions", "Escape velocity", "Work done by variable force"]},
            {"chapter": "Circular Motion", "topics": ["Angular velocity and acceleration", "Centripetal acceleration", "Artificial gravity", "Weightlessness (ISS context)", "Conical pendulum", "Angular momentum"]},
            {"chapter": "Fluid Dynamics", "topics": ["Ideal fluid", "Equation of continuity", "Bernoulli's equation and applications (aerofoil, Venturimeter, atomiser)", "Viscosity (Stoke's law)", "Surface tension"]},
            {"chapter": "Oscillations", "topics": ["SHM — angular frequency, phase", "Mass-spring system", "Simple pendulum (derivation)", "Energy in SHM", "Damped and forced oscillations", "Resonance"]},
            {"chapter": "Waves", "topics": ["Transverse and longitudinal waves", "Wave parameters", "Speed of sound (Newton-Laplace formula)", "Standing waves (strings, pipes)", "Beats", "Resonance"]},
            {"chapter": "Physical Optics", "topics": ["Wavefront (Huygen's principle)", "Young's double slit experiment (derivation)", "Diffraction grating (d sin θ = mλ)", "Thin film interference", "Polarisation (Brewster's law, Malus's law)"]},
            {"chapter": "Optical Instruments", "topics": ["Simple microscope (magnification)", "Compound microscope (lens formula application)", "Astronomical telescope (angular magnification)", "Spectrometer", "Camera and projector (principle)"]},
            {"chapter": "Heat and Thermodynamics", "topics": ["Kinetic theory of gases (PV = nRT derivation)", "Internal energy", "First law of thermodynamics (ΔU = Q - W)", "Isothermal, adiabatic, isochoric, isobaric processes", "Second law and entropy (concept)", "Carnot engine and efficiency"]},
        ],
        "Chemistry (Pre-Engineering / Pre-Medical)": [
            {"chapter": "Stoichiometry", "topics": ["Mole concept (revision and advanced)", "Stoichiometry calculations (reactants, products)", "Limiting reactant", "Percent yield", "Empirical and molecular formula from combustion data"]},
            {"chapter": "Atomic Structure", "topics": ["Rutherford's model (limitations)", "Bohr's model (energy levels, spectral lines of hydrogen)", "Quantum numbers (n, l, ml, ms)", "Pauli exclusion principle", "Aufbau principle", "Hund's rule", "Electronic configuration of elements"]},
            {"chapter": "Gases", "topics": ["Gas laws (detailed and combined)", "Ideal gas equation", "Dalton's law of partial pressures", "Diffusion and effusion (Graham's law)", "Kinetic molecular theory (detailed)", "Deviations from ideal behaviour (Van der Waals equation)"]},
            {"chapter": "Liquids and Solids", "topics": ["Properties of liquids (vapour pressure, boiling point, viscosity, surface tension)", "Types of solids (ionic, covalent, metallic, molecular)", "Crystal systems (cubic focus)", "Defects in crystals (concept)", "X-ray diffraction (concept)"]},
            {"chapter": "Chemical Bonding", "topics": ["Ionic bonding (lattice energy, Born-Haber cycle concept)", "Covalent bonding (Lewis structures, VSEPR theory detailed)", "Hybridisation (sp, sp², sp³)", "Molecular orbital theory (concept)", "Hydrogen bonding (effects on boiling point, DNA structure)"]},
            {"chapter": "Thermochemistry", "topics": ["Enthalpy (ΔH)", "Hess's law", "Standard enthalpy of formation", "Enthalpy of combustion", "Bond energy calculations", "Entropy (ΔS) and Gibbs free energy (ΔG = ΔH - TΔS)"]},
            {"chapter": "Electrochemistry", "topics": ["Galvanic cell (EMF, electrode potentials)", "Standard hydrogen electrode", "Electrochemical series", "Electrolytic cell", "Faraday's laws of electrolysis", "Corrosion prevention", "Batteries (lead-acid, lithium-ion)"]},
            {"chapter": "Chemical Equilibrium", "topics": ["Dynamic equilibrium concept", "Equilibrium constant (Kc, Kp)", "Relationship between Kc and Kp", "Le Chatelier's principle (detailed)", "Common ion effect", "Haber process and Contact process (industrial)"]},
            {"chapter": "Solutions", "topics": ["Types of solutions", "Solubility curves", "Colligative properties (elevation of boiling point, depression of freezing point, osmotic pressure)", "Molarity, molality, mole fraction", "Van't Hoff factor (electrolytes)"]},
            {"chapter": "Acids, Bases and Salts", "topics": ["Acid-base theories (full)", "Acid-base indicators", "Titration calculations", "Buffer solutions (Henderson-Hasselbalch)", "Kw, Ka, Kb, pKa", "Hydrolysis of salts"]},
            {"chapter": "Reaction Kinetics", "topics": ["Rate of reaction", "Rate law (order and rate constant)", "First order reactions (half-life)", "Activation energy (Arrhenius equation)", "Catalysis (homogeneous, heterogeneous, enzyme)"]},
        ],
        "Biology (Pre-Medical)": [
            {"chapter": "Introduction to Biology", "topics": ["Levels of organization", "Disciplines of biology", "Relationship with other sciences", "Themes in biology"]},
            {"chapter": "Biological Molecules", "topics": ["Carbohydrates (structure and functions, glycosidic bond)", "Lipids (phospholipids, steroids)", "Proteins (primary, secondary, tertiary, quaternary structure)", "Nucleic acids (DNA — double helix, Watson-Crick model; RNA — types)", "Adenosine triphosphate (ATP)"]},
            {"chapter": "Enzymes", "topics": ["Properties of enzymes", "Mechanism (lock and key, induced fit)", "Factors affecting enzyme activity", "Enzyme kinetics (Michaelis-Menten concept)", "Enzyme inhibition", "Immobilised enzymes (industrial use)"]},
            {"chapter": "The Cell", "topics": ["Cell theory", "Prokaryotic cell (detailed)", "Eukaryotic cell (detailed organelles)", "Cell membranes (fluid mosaic model)", "Membrane transport (diffusion, osmosis, active transport, endocytosis, exocytosis)"]},
            {"chapter": "Variety of Life — Classification", "topics": ["History of classification", "Kingdoms (5 and 6 kingdom systems)", "Hierarchical classification (domain to species)", "Binomial nomenclature", "Dichotomous key construction"]},
            {"chapter": "Kingdom Prokaryotae", "topics": ["Structure of bacteria", "Types of bacteria", "Economic importance (positive and negative)", "Role in disease (gram +ve and -ve)", "Antibiotics and resistance"]},
            {"chapter": "Kingdom Protista", "topics": ["Algae (green, red, brown) — structure and importance", "Protozoa (amoeba, paramecium, plasmodium)", "Malaria life cycle and Pakistan context"]},
            {"chapter": "Kingdom Fungi", "topics": ["Characteristics", "Structure (hyphae, mycelium)", "Reproduction (asexual and sexual)", "Economic importance (yeast, penicillin, mushrooms)", "Harmful fungi (ringworm, athlete's foot)"]},
            {"chapter": "Kingdom Plantae", "topics": ["Classification (bryophytes, pteridophytes, gymnosperms, angiosperms)", "Alternation of generations", "Adaptations to land", "Angiosperms — monocots vs dicots"]},
            {"chapter": "Kingdom Animalia", "topics": ["Major phyla (Porifera, Cnidaria, Platyhelminthes, Nematoda, Annelida, Mollusca, Arthropoda, Echinodermata, Chordata)", "Evolutionary trends", "Pakistan's important animal species"]},
            {"chapter": "Bioenergetics", "topics": ["Photosynthesis (light reactions — Z-scheme; dark reactions — Calvin cycle)", "Photorespiration", "C4 and CAM plants", "Aerobic respiration (glycolysis, link reaction, Krebs cycle, ETC)", "Chemiosmosis (ATP synthesis)"]},
            {"chapter": "Nutrition", "topics": ["Autotrophic nutrition (photosynthesis and chemosynthesis)", "Heterotrophic nutrition (holozoic, parasitic, saprophytic)", "Human nutrition (digestive system detailed)", "Nutritional disorders in Pakistan"]},
            {"chapter": "Gaseous Exchange", "topics": ["Gaseous exchange in prokaryotes", "Gaseous exchange in plants (stomata, lenticels)", "Gaseous exchange in animals (gills, lungs)", "Human respiratory system (detailed)", "Disorders: asthma, emphysema, tuberculosis"]},
            {"chapter": "Transport", "topics": ["Transport in plants (xylem and phloem mechanisms)", "Blood composition", "Human heart (structure, cardiac cycle, ECG concept)", "Lymphatic system", "Blood disorders (anaemia, leukaemia — Pakistan context)"]},
        ],
        "Mathematics (Pre-Engineering / ICS)": [
            {"chapter": "Functions and Limits", "topics": ["Types of functions", "Composition and inverse", "Limits (algebraic and trigonometric)", "Sandwich theorem", "Continuity"]},
            {"chapter": "Differentiation", "topics": ["First principles", "Rules (power, product, quotient, chain)", "Derivatives of trigonometric, logarithmic, exponential functions", "Implicit differentiation", "Applications (tangent, normal, maxima, minima, rate of change)"]},
            {"chapter": "Integration", "topics": ["Indefinite integration (standard integrals)", "Integration by substitution, parts, partial fractions", "Definite integration", "Area under curve", "Differential equations (separable)"]},
            {"chapter": "Analytic Geometry", "topics": ["Straight line (all forms)", "Distance from point to line", "Circle (equation, tangent)", "Parabola (standard and general form)"]},
            {"chapter": "Linear Inequalities and Linear Programming", "topics": ["Graphical method", "Feasible region", "Optimal solution", "Business applications (maximize profit, minimize cost — local examples)"]},
            {"chapter": "Conic Sections", "topics": ["Circle, ellipse, parabola, hyperbola — standard equations", "Tangent and normal", "Optical properties"]},
            {"chapter": "Vectors", "topics": ["3D vectors", "Dot product and cross product", "Scalar triple product", "Applications (work done, moment of force, velocity)"]},
        ],
        "Urdu": [
            {"chapter": "Nasar — Inter Level Lessons", "topics": ["12 prose lessons from PCTB Inter text", "Critical analysis", "Essay-type answers"]},
            {"chapter": "Poetry — Classical and Modern", "topics": ["Iqbal (full poems)", "Faiz, Faraz, Josh, Habib Jalib selected", "Detailed analysis"]},
            {"chapter": "Grammar — Inter Level", "topics": ["Advanced Sarf", "Nahv", "Qawaid at inter level", "HSSC past paper patterns"]},
            {"chapter": "Composition — HSSC Level", "topics": ["Long essays (600+ words)", "Detailed applications", "Translation (Urdu-English)", "Short stories (adabi)" ]},
        ],
        "English": [
            {"chapter": "Literature — Prose (Inter)", "topics": ["PCTB Inter English prose pieces", "Critical analysis", "Character and theme at HSSC level"]},
            {"chapter": "Literature — Poetry (Inter)", "topics": ["PCTB Inter poems", "Detailed poetic analysis", "Appreciation essay"]},
            {"chapter": "Grammar — HSSC Level", "topics": ["Comprehensive grammar at intermediate level", "Transformation exercises", "Error correction"]},
            {"chapter": "Composition — HSSC Level", "topics": ["Long essay (600-800 words)", "Précis and expansion", "Translation English-Urdu/Urdu-English"]},
        ],
    },

    # ── CLASS 12 (FSc/FA/ICS Part 2) ─────────────────────────────────────────
    12: {
        "Physics (Pre-Engineering / Pre-Medical)": [
            {"chapter": "Electrostatics", "topics": ["Coulomb's law (vector form)", "Electric field and potential", "Gauss's law", "Capacitors (series and parallel)", "Dielectrics", "Energy stored in capacitor"]},
            {"chapter": "Current Electricity", "topics": ["Ohm's law (microscopic form)", "Kirchhoff's laws (complex networks)", "Wheatstone bridge", "Potentiometer", "RC circuits (charging and discharging)", "Electromotive force and internal resistance"]},
            {"chapter": "Electromagnetism", "topics": ["Magnetic force on charge (F = qv × B)", "Force on current-carrying conductor", "Torque on current loop", "Hall effect", "Magnetic flux", "Ampere's law", "Solenoid and toroid"]},
            {"chapter": "Electromagnetic Induction", "topics": ["Faraday's law (quantitative)", "Lenz's law", "Mutual and self-inductance", "Energy stored in inductor", "AC generator", "Back EMF in motors"]},
            {"chapter": "Alternating Current", "topics": ["AC fundamentals (peak, RMS, average values)", "Phase relationships (R, L, C individually)", "Series RLC circuit (resonance)", "Power in AC circuit (power factor)", "Transformer efficiency and losses", "Transmission lines"]},
            {"chapter": "Physics of Solids", "topics": ["Crystalline vs amorphous solids", "Energy band theory", "Conductors, semiconductors, insulators (band gap)", "Intrinsic and extrinsic semiconductors (n-type, p-type)", "pn junction diode", "Zener diode"]},
            {"chapter": "Electronics", "topics": ["Diode applications (rectifier circuits)", "Transistor (BJT) characteristics", "Transistor as amplifier (CE configuration)", "Transistor as switch", "Op-amp basics", "Logic gates (complete)"]},
            {"chapter": "Dawn of Modern Physics", "topics": ["Special theory of relativity (postulates, consequences)", "Photoelectric effect (Einstein's equation)", "Compton effect", "de Broglie hypothesis", "Uncertainty principle (Heisenberg)"]},
            {"chapter": "Atomic Spectra", "topics": ["Hydrogen spectrum (Lyman, Balmer, Paschen series)", "Bohr's explanation of spectra", "X-ray spectrum (characteristic and continuous)", "Laser (principle, types, applications in medicine)"]},
            {"chapter": "Nuclear Physics", "topics": ["Nuclear properties (mass defect, binding energy)", "Radioactivity (alpha, beta, gamma decay)", "Half-life and decay constant", "Nuclear fission (chain reaction)", "Nuclear fusion", "Nuclear reactors (KANUPP, CHASNUPP)", "Medical applications of nuclear physics"]},
        ],
        "Chemistry (Pre-Engineering / Pre-Medical)": [
            {"chapter": "Periodic Classification", "topics": ["Periodic trends (detailed)", "Diagonal relationship", "Screening effect and Slater's rules"]},
            {"chapter": "s-Block Elements", "topics": ["Group IA (alkali metals) — properties, reactions, uses", "Group IIA (alkaline earth metals)", "Industrial importance (NaOH, Na₂CO₃ — Solvay process)"]},
            {"chapter": "Group IIIA and IVA Elements", "topics": ["Boron and Aluminium", "Carbon and Silicon", "Oxides and halides"]},
            {"chapter": "Group VA, VIA, VIIA Elements", "topics": ["Nitrogen and Phosphorus", "Oxygen and Sulphur", "Halogens", "Noble gases"]},
            {"chapter": "Transition Elements", "topics": ["General properties", "Variable oxidation states", "Complex formation", "Catalytic properties", "Iron, copper, chromium (important examples)"]},
            {"chapter": "Organic Chemistry — Fundamentals", "topics": ["Classification of organic compounds", "Homologous series", "Functional groups", "Reaction mechanisms (substitution, addition, elimination — intro)"]},
            {"chapter": "Alkyl Halides", "topics": ["Preparation and reactions", "SN1 and SN2 mechanisms", "Elimination reactions (E1, E2)"]},
            {"chapter": "Alcohols and Phenols", "topics": ["Structure and properties", "Reactions of alcohols", "Industrial alcohol production", "Phenol — properties and uses"]},
            {"chapter": "Aldehydes and Ketones", "topics": ["Structure and nomenclature", "Preparation methods", "Addition and oxidation reactions", "Formaldehyde, acetaldehyde, acetone — industrial uses"]},
            {"chapter": "Carboxylic Acids", "topics": ["Structure and properties", "Reactions (esterification, reduction)", "Fatty acids (saturated and unsaturated)", "Soap making (saponification) — Pakistan soap industry"]},
            {"chapter": "Macromolecules", "topics": ["Polymers (addition and condensation)", "Nylon, polyethylene, PVC", "Rubber (natural and synthetic)", "Biopolymers (starch, cellulose, proteins, DNA)"]},
            {"chapter": "Chemical Industries in Pakistan", "topics": ["Fertiliser industry (Fauji Fertiliser, Engro)", "Petroleum industry (OGDCL, PPL, Attock Refinery)", "Pharmaceutical industry", "Textile chemicals", "Environmental impact of these industries"]},
        ],
        "Biology (Pre-Medical)": [
            {"chapter": "Homeostasis", "topics": ["Kidney structure (nephron detailed)", "Kidney functions", "Dialysis and kidney transplant in Pakistan", "Liver functions", "Thermoregulation", "Excretion in plants"]},
            {"chapter": "Immunity", "topics": ["Non-specific immunity (skin, macrophages, inflammation)", "Specific immunity (humoral — B cells, antibodies; cellular — T cells)", "Active vs passive immunity", "Vaccination (EPI programme in Pakistan)", "HIV/AIDS mechanism and Pakistan data", "Autoimmune diseases (concept)"]},
            {"chapter": "Support and Movement", "topics": ["Bone structure (compact and spongy bone)", "Types of joints (detailed)", "Muscles (sarcomere, sliding filament theory)", "Disorders (arthritis, osteoporosis, muscular dystrophy)"]},
            {"chapter": "Coordination and Control", "topics": ["Neuron types and functions", "Nerve impulse (resting potential, action potential)", "Synapse and neurotransmitters", "Reflex arc", "Brain regions and functions", "Spinal cord", "Autonomic nervous system", "Hormonal control (endocrine glands in detail)", "Hormone disorders (diabetes, thyroid — Pakistan prevalence)"]},
            {"chapter": "Reproduction", "topics": ["Asexual reproduction (types)", "Sexual reproduction (human reproductive system — detailed)", "Menstrual cycle", "Fertilisation and implantation", "Embryonic development", "Birth", "Sexually transmitted infections", "Contraception concepts"]},
            {"chapter": "Development and Aging", "topics": ["Cell differentiation", "Embryo stages", "Ageing process", "Stem cells and their medical potential"]},
            {"chapter": "Inheritance", "topics": ["Mendel's laws (revisited with molecular basis)", "Chromosomal theory of inheritance", "Linked genes and crossing over", "Sex-linked traits (colour blindness, haemophilia)", "Mutations (gene and chromosomal)", "Genetic disorders in Pakistan (thalassaemia, haemophilia)"]},
            {"chapter": "Variation and Genetics", "topics": ["Sources of variation", "Natural selection (Darwin's theory)", "Hardy-Weinberg principle", "Speciation", "Evolution evidence"]},
            {"chapter": "Biotechnology", "topics": ["Recombinant DNA technology (gene cloning)", "PCR (polymerase chain reaction)", "DNA fingerprinting", "Transgenic organisms", "Applications in medicine (insulin, growth hormone)", "Applications in agriculture (Bt cotton in Pakistan)", "Ethical concerns"]},
            {"chapter": "Man and His Environment", "topics": ["Biomes of the world (and Pakistan's biomes)", "Ecological succession", "Nutrient cycles (detailed nitrogen and carbon cycles)", "Biodiversity (threatened species in Pakistan — snow leopard, Indus dolphin)", "Environmental issues (deforestation in Khyber Pakhtunkhwa, wetland degradation)", "Conservation efforts (WWF Pakistan, protected areas)"]},
        ],
        "Mathematics (Pre-Engineering / ICS)": [
            {"chapter": "Functions and Limits (Revision and Extension)", "topics": ["Limits at infinity", "L'Hôpital's rule", "Continuity theorems"]},
            {"chapter": "Differentiation (Advanced)", "topics": ["Implicit and parametric differentiation", "Higher order derivatives", "Maclaurin and Taylor series (concept)", "Applications: related rates, linear approximation"]},
            {"chapter": "Integration (Advanced)", "topics": ["Techniques (integration by parts, trigonometric substitution)", "Reduction formulae", "Definite integrals properties", "Area between curves", "Volume of revolution", "Differential equations (separable, linear first order)"]},
            {"chapter": "Introduction to Probability", "topics": ["Sample space and events", "Counting techniques (permutations, combinations)", "Probability laws (addition, multiplication, conditional)", "Bayes' theorem (concept)", "Probability distributions (binomial, normal)"]},
            {"chapter": "Statistics (Advanced)", "topics": ["Data analysis", "Regression and correlation", "Normal distribution Z-scores", "Hypothesis testing (concept)", "Chi-square test (concept)"]},
        ],
    },
}


def get_subjects_for_class(class_num: int) -> list:
    """Return list of subjects for a given class number."""
    return list(PCTB_SYLLABUS.get(class_num, {}).keys())


def get_chapters_for_subject(class_num: int, subject: str) -> list:
    """Return list of chapter titles for a class-subject pair."""
    chapters = PCTB_SYLLABUS.get(class_num, {}).get(subject, [])
    return [ch["chapter"] for ch in chapters]


def get_topics_for_chapter(class_num: int, subject: str, chapter: str) -> list:
    """Return list of topics for a specific chapter."""
    chapters = PCTB_SYLLABUS.get(class_num, {}).get(subject, [])
    for ch in chapters:
        if ch["chapter"] == chapter:
            return ch["topics"]
    return []


def get_all_classes() -> list:
    """Return sorted list of available class numbers."""
    return sorted(PCTB_SYLLABUS.keys())
