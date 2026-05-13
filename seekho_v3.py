"""
seekho_v3.py  --  Seekho Platform
Pakistan's Hyper-Local AI Curriculum Engine

Run:  streamlit run seekho_v3.py
"""

import io, re, os
import streamlit as st
from datetime import datetime
from google import genai

import database  as db
import ui_style

# ── PAGE CONFIG  (must be first Streamlit call) ───────────────────────────────
st.set_page_config(
    page_title="Seekho Platform",
    page_icon=ui_style.LOGO_URL,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={"About": "Seekho Platform  --  PCTB-aligned AI curriculum for Pakistani teachers."},
)

# ── GLOBAL STYLES  (orbs + all CSS + keyboard shortcut + ripple) ─────────────
ui_style.inject_all()

# ── SESSION STATE ─────────────────────────────────────────────────────────────
_DEFAULTS = {
    "splash_done":      False,
    "lesson_content":   "",
    "last_params":      {},
    "history":          [],      # stores metadata only (no content blob)
    "wa_messages":      "",
    "just_generated":   False,
    "last_school":      "",
    "last_district":    "",
}
for _k, _v in _DEFAULTS.items():
    if _k not in st.session_state:
        st.session_state[_k] = _v

# ── SPLASH ────────────────────────────────────────────────────────────────────
if ui_style.maybe_show_splash():
    st.stop()

# ── GEMINI CLIENT ─────────────────────────────────────────────────────────────
@st.cache_resource
def _gemini():
    key = ""
    try:
        key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        key = os.environ.get("GEMINI_API_KEY", "")
    if not key:
        st.error("GEMINI_API_KEY missing. Add it to .streamlit/secrets.toml and restart.")
        st.stop()
    return genai.Client(api_key=key)

gemini = _gemini()
MODEL  = "gemini-flash-latest"

# ── CLASS CONFIGS ─────────────────────────────────────────────────────────────
CLASS_CFG = {
    1:  {"vocab":"3-5 word sentences. Monosyllabic words. Heavy repetition.",
         "q":   "True/False or circle-the-picture. Max 3 questions.",
         "bl":  "REMEMBER only.",
         "len": "60-90 words. One concept.",
         "n":   "Teacher reads aloud. Writing = tracing."},
    2:  {"vocab":"2-syllable words. 5-7 word sentences.",
         "q":   "Match column or 3-option MCQ. Max 4 questions.",
         "bl":  "REMEMBER + basic UNDERSTAND.",
         "len": "100-140 words.",
         "n":   "Anchor to objects the child can hold."},
    3:  {"vocab":"Everyday words. Max 8 words/sentence. Repeat key terms 3 times.",
         "q":   "3-option MCQ + 1 fill-in-blank. 5 questions.",
         "bl":  "REMEMBER + UNDERSTAND. Simple categorisation.",
         "len": "150-200 words.",
         "n":   "Group oral activities work better than individual writing."},
    4:  {"vocab":"Define any term inline. Max 10 words/sentence.",
         "q":   "3-option MCQ + match column. 5-6 questions.",
         "bl":  "REMEMBER, UNDERSTAND, simple APPLY.",
         "len": "200-260 words.",
         "n":   "Drawing activities improve retention for this age."},
    5:  {"vocab":"Technical terms with bracket definition. Max 12 words.",
         "q":   "4-option MCQ + fill-blank + 1 short answer. 6 questions.",
         "bl":  "REMEMBER, UNDERSTAND, APPLY.",
         "len": "250-320 words.",
         "n":   "PCTB board pressure begins here. Past-paper vocabulary."},
    6:  {"vocab":"Technical terms with parenthetical definition. Max 12 words.",
         "q":   "4-option MCQ + short answer + diagram label. 7 questions.",
         "bl":  "REMEMBER, UNDERSTAND, APPLY. One application question.",
         "len": "300-380 words.",
         "n":   "BISE alignment critical. Match PCTB chapter references."},
    7:  {"vocab":"Board-level vocabulary. Sentences up to 14 words.",
         "q":   "MCQ (4-option) + SQs (2-3 marks) + 1 reasoning question. 8 questions.",
         "bl":  "REMEMBER through ANALYZE. At least one analytical question.",
         "len": "350-430 words.",
         "n":   "Pair work and written discussion appropriate."},
    8:  {"vocab":"Full PCTB vocabulary. Board exam sentence structure.",
         "q":   "MCQ + SQ + LQ outline. 8-10 questions. Board format.",
         "bl":  "All levels through ANALYZE.",
         "len": "400-500 words.",
         "n":   "Matric preparation. Formal, exam-aligned tone."},
    9:  {"vocab":"Complete PCTB Matric vocabulary. Precise definitions.",
         "q":   "MCQ (1-mark) + SQ (2-3 mark) + LQ (5-mark). 10 questions.",
         "bl":  "All Bloom's levels. Analysis + evaluation required.",
         "len": "450-550 words. Board exam format.",
         "n":   "Reference PCTB chapter explicitly. Past-paper language."},
    10: {"vocab":"Board exam vocabulary. Complex sentences acceptable.",
         "q":   "Full board format: MCQ + SQ + LQ. 10-12 questions.",
         "bl":  "All levels. CREATE + EVALUATE dominant.",
         "len": "500-620 words. BISE standard.",
         "n":   "Board year. Every element must be exam-relevant."},
    11: {"vocab":"University-entrance vocabulary. FSc/FA technical language.",
         "q":   "HSSC SQs + LQs. Essay-type possible. 8-12 questions.",
         "bl":  "EVALUATE + CREATE dominant. Cross-topic synthesis.",
         "len": "600+ words. HSSC standard.",
         "n":   "MDCAT/ECAT relevance where applicable."},
    12: {"vocab":"University-entrance vocabulary. Critical analysis language.",
         "q":   "Board SQs, LQs, numericals. 10-14 questions.",
         "bl":  "EVALUATE, CREATE, synthesis.",
         "len": "650+ words. HSSC final year.",
         "n":   "Entry test preparation is the primary driver."},
}

# ── PROMPT ────────────────────────────────────────────────────────────────────
def build_prompt(school, district, class_num, subject, chapter, topic,
                 language, mode, profile, extra, topics_list):

    d  = db.get_district(district)
    cc = CLASS_CFG.get(class_num, CLASS_CFG[6])
    today = datetime.now().strftime("%d %b %Y")

    lang_block = {
        "Pure Urdu (Script)": """
LANGUAGE: Write EVERYTHING in pure Urdu Nastaliq script.
Every header, bullet, question, table cell in Urdu script.
Only exception: unavoidable symbols (CO2, H2O, km, PKR).
""",
        "Roman Urdu": """
LANGUAGE: Write EVERYTHING in Roman Urdu (Urdu words spelled in English letters).
Exactly as Pakistani students type on WhatsApp.
NOT formal English. NOT Urdu script.
Example: 'Dekho, ye concept bilkul aasaan hai. Socho jaise Akbar ke abbu ki fasal...'
""",
    }.get(language, """
LANGUAGE: Clear Pakistani English (not British or American).
Where a Urdu/Punjabi term adds warmth, include it in brackets.
""")

    profile_block = {
        "Weak Class (Below Average)": """
CLASS PROFILE -- WEAK CLASS:
Reduce vocabulary one full grade below stated class.
Break every concept into the smallest possible step.
No abstract concepts -- everything physical and tangible.
Write for oral delivery, not silent reading.
Repeat the key term at least 3 times in the handout.
""",
        "Strong Class (Above Average)": """
CLASS PROFILE -- STRONG CLASS:
Add one [CHALLENGE] question above stated class level.
Add one "Did You Know?" extension fact beyond the PCTB chapter.
Invite hypothesis formation or cross-topic connection.
""",
    }.get(profile, "CLASS PROFILE -- AVERAGE CLASS: Standard complexity for this class level.")

    topics_str = "\n".join(f"  - {t}" for t in topics_list) if topics_list else "  - All topics in this chapter"

    mode_block = {
        "Full Lesson Pack": """
Generate SECTION 1 (Teacher Guide) then SECTION 2 (Student Handout + Assessment + AI Activity).
Do NOT generate a WhatsApp message. That is handled separately.
""",
        "Student Handout Only": "Generate ONLY the Student Handout section (Section 2).",
        "Assessment Sheet Only": "Generate ONLY the Assessment Sheet with Answer Key.",
        "Teacher Guide Only": "Generate ONLY Section 1 (Teacher Guide).",
    }.get(mode, "Generate Full Lesson Pack.")

    return f"""
You are SEEKHO ENGINE -- a specialist Pakistani curriculum expert with 20 years in PCTB-aligned
schools. You know the 8 real failures of Pakistani classrooms:
  a) Passive learning  b) Rote memorisation  c) No local relevance  d) No scaffolding
  e) Assessment-only teaching  f) No active retrieval  g) Wasted AI homework  h) Paragraph walls

Your job is to fix all 8 in every output.

PARAMETERS
School: {school} | District: {district} | Board: {d.get("board","BISE")}
Class: {class_num} | Subject: {subject} | Chapter: {chapter}
Focus: {topic if topic != "Full Chapter Overview" else "Complete chapter"} | Date: {today}
Language: {language} | Profile: {profile} | Mode: {mode}

LOCAL CONTEXT FOR {district.upper()}
Economy: {d.get("economy","")}
Landmarks: {d.get("landmarks","")}
Transport: {d.get("transport","")}
Food: {d.get("food","")}
Occupations: {d.get("occupations","")}
Nature: {d.get("nature","")}
Names: {d.get("local_names","")}
Schools: {d.get("school_type","")}

LOCALISATION RULES (violations invalidate the output):
BANNED: generic transport, foreign names, Western references, "In developed countries..."
REQUIRED: every example uses a specific name, place, and item from the lists above.
TEST: "Would a student from {district} recognise this from their own daily life?" If no, replace it.

CHAPTER TOPICS (PCTB reference)
{topics_str}
PCTB REF: PCTB {subject} Class {class_num}, Chapter: {chapter}

CLASS {class_num} RULES
Vocabulary: {cc["vocab"]}
Questions: {cc["q"]}
Bloom level: {cc["bl"]}
Length: {cc["len"]}
Note: {cc["n"]}

{lang_block}
{profile_block}

EXTRA INSTRUCTIONS
{extra.strip() if extra.strip() else "None. Use best pedagogical judgment."}

OUTPUT MODE
{mode_block}

FORMAT RULES (non-negotiable)

RULE 1 -- NO PARAGRAPH WALLS:
No prose block longer than 2 sentences anywhere in Section 2.
Use: table, numbered list, bullet list, labelled text format, question-answer pair.
If you are writing a paragraph, STOP and convert it to one of the above.

RULE 2 -- CONCEPT LADDER (mandatory in every Student Handout):
Step 1 -- Local Analogy: specific named person + specific local place + specific activity. ZERO jargon.
Step 2 -- The Bridge: 1-2 sentences connecting analogy to concept. First use of technical term.
Step 3 -- The Definition: PCTB-standard definition. Bold the key term.

RULE 3 -- QUICK THINK BOX (mandatory):
2 in-class questions placed BEFORE the assessment.
Both questions require thinking, not copying from the handout.
A question answerable by copying a sentence is rejected.

RULE 4 -- AI HOME ACTIVITY (mandatory, purposeful):
Structure:
  a) EXACT PROMPT: The precise text to type into ChatGPT or Gemini. Quoted block.
     Design it to produce output the student can work with, not just read.
  b) WHAT YOU WILL GET: One sentence describing the AI response format.
  c) YOUR TASK: A specific cognitive task using the AI output.
     Valid: "List 3 things AI said that match + 1 that differs"
     Valid: "Draw and label a diagram based on the AI description"
     Valid: "Write 2 questions you still have after reading it"
     Invalid: "Share with class" / "Take notes" / "Read it again"
  d) BRING TO CLASS: The specific physical artifact (a sketch, a written list, a question in notebook).
  e) TIME: Realistic estimate in minutes.

RULE 5 -- BLOOM LABELS on every assessment question:
(K) Remember  (U) Understand  (A) Apply  (AN) Analyze  (E) Evaluate

RULE 6 -- MCQ INTEGRITY:
Exactly ONE unambiguous correct answer per MCQ.
Three plausible but clearly wrong distractors.
No trick questions. No option identifiable as correct by length alone.

RULE 7 -- ANSWER KEY:
End assessment with:
---
TEACHER ANSWER KEY -- DO NOT DISTRIBUTE
---
List every answer numbered.

RULE 8 -- TEACHER DELIVERY TABLE (Section 1 only):
| Time | Activity | What To Say or Do |

RULE 9 -- WRAP-UP SCRIPT (Section 1 only):
Say: "[exact words in the selected language to close the lesson]"

RULE 10 -- MISCONCEPTION FLAG (Section 1 only):
Common Wrong Belief: [what students incorrectly think]
Correct It By Saying: "[exact correction sentence]"

RULE 11 -- NO EM DASHES anywhere in the output.

RULE 12 -- SEEKHO FOOTER: End every section with one line:
*Seekho Platform |Let's make learning fun!*

OUTPUT TEMPLATE
Begin immediately with the title. No preamble.

---
# {school} | {subject} | Class {class_num}
## {chapter}
*PCTB {subject} Class {class_num} | {district} | {today}*

---
## SECTION 1: TEACHER GUIDE
*(Private -- do not distribute)*

### Common Misconception
Common Wrong Belief: [...]
Correct It By Saying: "[...]"

### Prerequisites
- [...]
- [...]

### 40-Minute Delivery Plan
| Time | Activity | What To Say or Do |
|------|----------|-------------------|
...

### No-Tech Activity
Name: [...] | Time: [...] min
Steps:
1. [...]
2. [...]
What good understanding looks like: [...]

### Wrap-Up Script
Say: "[...]"

---
## SECTION 2: STUDENT HANDOUT
*(Print one copy per student)*

### The Big Question
*[Hook question -- students do not already know the answer. The lesson answers it.]*

### Step 1 -- Start With What You Know
[Local analogy: named person + named place + specific activity. Zero jargon.]

### Step 2 -- The Connection
[Bridge to concept. Introduce technical term here for the first time, with simple definition in brackets.]

### Step 3 -- The Definition
**[Technical Term]:** [PCTB-standard definition]

### Key Terms
| Term | Simple Meaning | Example From {district} |
|------|---------------|-------------------------|
...

### How It Works
1. [Step -- one sentence max]
2. [...]
3. [...]

### Quick Think
*Answer in your notebook right now. Do not copy from the handout.*
1. [Recall + light application]
2. [Comparison or reasoning]

---
### Assessment

**Part A: Circle the Correct Answer** (1 mark each)
1. (K) [...] a) [...] b) [...] c) [...] d) [...]
2. (U) [...] a) [...] b) [...] c) [...] d) [...]
3. (A) [local-context application] a) [...] b) [...] c) [...] d) [...]

**Part B: Short Questions** (2 marks each)
4. (U) [Explain -- not define]
5. (A) [Apply to a new scenario from {district}]
6. (AN) [Compare or analyse two things]

**Part C: Real-Life Application** (5 marks)
7. (A+AN) [Multi-part question entirely grounded in {district} context]

---
### AI Activity
*Do at home if you have phone or computer with internet.*

**Type this exact prompt into ChatGPT or Gemini:**
> [Crafted prompt designed to produce usable output for the task below]

**What you will get back:** [One sentence]

**Your task:**
[Specific cognitive task using the AI output]

**Bring to next class:** [Specific physical artifact -- not "your phone"]

**Time needed:** [...] minutes

---
TEACHER ANSWER KEY -- DO NOT DISTRIBUTE

Part A: 1-[...] 2-[...] 3-[...]
Part B: 4-[...] 5-[...] 6-[...]
Part C: 7-[full model answer]

---
*Seekho Platform |Let's make learning fun!*
"""


# ── DOCX GENERATOR ───────────────────────────────────────────────────────────
def _add_run(para, text):
    for part in re.split(r"(\*\*[^*]+\*\*)", text):
        if part.startswith("**") and part.endswith("**"):
            r = para.add_run(part[2:-2]); r.bold = True
        elif part:
            para.add_run(part)


def generate_docx(content: str, params: dict) -> bytes:
    from docx import Document
    from docx.shared import Pt, Inches, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH

    doc = Document()
    for sec in doc.sections:
        sec.top_margin = sec.bottom_margin = Inches(1.0)
        sec.left_margin = sec.right_margin = Inches(1.25)

    # Header
    hp = doc.add_paragraph(); hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    hr = hp.add_run(params.get("school_name", "Seekho Platform"))
    hr.bold = True; hr.font.size = Pt(16)
    hr.font.color.rgb = RGBColor(0x1a, 0x7f, 0x4b)

    mp = doc.add_paragraph(); mp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    mr = mp.add_run(
        f"Class {params.get('class_num','')} | {params.get('subject','')} | "
        f"{params.get('chapter','')} | {params.get('district','')} | "
        f"{datetime.now().strftime('%d %b %Y')}"
    ); mr.font.size = Pt(10); mr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    doc.add_paragraph()

    in_table = False; t_hdrs = []; t_rows = []

    def flush():
        nonlocal in_table, t_hdrs, t_rows
        if not t_hdrs: in_table = False; return
        t = doc.add_table(rows=1 + len(t_rows), cols=len(t_hdrs)); t.style = "Table Grid"
        for j, h in enumerate(t_hdrs):
            c = t.rows[0].cells[j]; c.text = h.strip()
            for p in c.paragraphs:
                for r in p.runs: r.bold = True; r.font.size = Pt(10)
        for ri, row in enumerate(t_rows, 1):
            for j, ct in enumerate(row):
                if j < len(t_hdrs):
                    t.rows[ri].cells[j].text = ct.strip()
        doc.add_paragraph()
        in_table = False; t_hdrs.clear(); t_rows.clear()

    GREEN = RGBColor(0x1a, 0x7f, 0x4b)
    BLUE  = RGBColor(0x2a, 0x5f, 0xa0)

    for line in content.split("\n"):
        s = line.strip()
        if s.startswith("|") and s.endswith("|"):
            parts = [p.strip() for p in s.strip("|").split("|")]
            if not in_table:
                in_table = True; t_hdrs = parts
            elif re.match(r"^[\s\-|:]+$", s):
                pass
            else:
                t_rows.append(parts)
            continue
        elif in_table:
            flush()

        if not s: doc.add_paragraph(); continue
        if s.startswith("# "):
            h = doc.add_heading(s[2:], 1)
            if h.runs: h.runs[0].font.color.rgb = GREEN
        elif s.startswith("## "):
            h = doc.add_heading(s[3:], 2)
            if h.runs: h.runs[0].font.color.rgb = GREEN
        elif s.startswith("### "):
            h = doc.add_heading(s[4:], 3)
            if h.runs: h.runs[0].font.color.rgb = BLUE
        elif s.startswith(("* ", "- ")):
            p = doc.add_paragraph(style="List Bullet"); _add_run(p, s[2:])
        elif re.match(r"^\d+\.\s", s):
            p = doc.add_paragraph(style="List Number"); _add_run(p, re.sub(r"^\d+\.\s*","",s))
        elif s.startswith(">"):
            p = doc.add_paragraph(); p.paragraph_format.left_indent = Inches(.5)
            r = p.add_run(s.lstrip("> ")); r.italic = True; r.font.size = Pt(11)
        elif s.startswith("---") or s.startswith("==="):
            doc.add_paragraph("_" * 54)
        elif s.startswith("*") and s.endswith("*") and not s.startswith("**"):
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(s.strip("*")); r.italic = True; r.font.size = Pt(9)
            r.font.color.rgb = RGBColor(0x88, 0x88, 0x88)
        else:
            p = doc.add_paragraph(); _add_run(p, s)
            for r in p.runs: r.font.size = Pt(11)

    if in_table: flush()

    for sec in doc.sections:
        fp = sec.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fr = fp.add_run(
            f"Seekho Platform |Let's make learning fun! | "
            f"{params.get('school_name','')} | "
            f"Class {params.get('class_num','')} {params.get('subject','')} | "
            f"{datetime.now().strftime('%d %b %Y')}"
        ); fr.font.size = Pt(8); fr.font.color.rgb = RGBColor(0x99, 0x99, 0x99)

    buf = io.BytesIO(); doc.save(buf); buf.seek(0)
    return buf.getvalue()


# ── WHATSAPP ─────────────────────────────────────────────────────────────────
def gen_whatsapp(content: str, params: dict) -> str:
    p = params
    prompt = f"""
Format this lesson for WhatsApp. Generate 3 copy-paste ready messages separated by "---".

Lesson: Class {p.get('class_num','')} {p.get('subject','')} | {p.get('chapter','')} | {p.get('district','')}
School: {p.get('school_name','')}

MESSAGE A -- PARENT GROUP:
Open: "Assalam o Alaikum {p.get('school_name','')} parents!"
2 sentences on what was taught. 1 question for parent to ask child tonight.
1 zero-material home activity. Under 130 words.

MESSAGE B -- STUDENT GROUP:
Casual elder-sibling tone. Today's key point in 2 fun sentences.
1 question they can reply to. Under 90 words.

MESSAGE C -- TEACHER COLLEAGUES:
Professional. 1 teaching tip or local analogy that works for this topic. Under 70 words.

Source (first 1200 chars):
{content[:1200]}
"""
    try:
        return gemini.models.generate_content(model=MODEL, contents=prompt).text
    except Exception as e:
        return f"WhatsApp generation failed: {e}"


# ── AI REFINE ────────────────────────────────────────────────────────────────
def refine(content: str, instruction: str) -> str:
    return gemini.models.generate_content(model=MODEL, contents=f"""
Edit this Pakistani curriculum document.

INSTRUCTION: {instruction}

RULES:
- Apply ONLY the stated instruction. Change nothing else.
- Keep all existing Markdown formatting.
- No paragraph walls -- use tables and lists.
- No em dashes.
- Return the complete updated document with no preamble.

DOCUMENT:
{content}
""").text


# ════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    ui_style.render_sidebar_logo()

    # Usage stats from Supabase
    with st.container():
        try:
            stats = db.get_analytics_summary()
            total = stats.get("total_lessons", 0)
            if total:
                st.markdown(
                    f'<div style="padding:.5rem 0 .2rem;">'
                    f'<span class="stat-pill">Lessons generated: {total:,}</span>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
        except Exception:
            pass

    st.markdown("## Settings")

    output_mode = st.selectbox("Output Mode", [
        "Full Lesson Pack",
        "Student Handout Only",
        "Assessment Sheet Only",
        "Teacher Guide Only",
    ])

    class_profile = st.radio("Class Profile", [
        "Average Class",
        "Weak Class (Below Average)",
        "Strong Class (Above Average)",
    ])

    extra = st.text_area("Custom Instructions", placeholder=(
        "Use cricket analogies\n"
        "Add Ramadan context\n"
        "Include drawing activity\n"
        "Add comparison table\n"
        "Reference Waris Shah"
    ), height=110)

    st.divider()

    # Session history (metadata only, no content blob)
    st.markdown("## History")
    if st.session_state.history:
        for i, h in enumerate(reversed(st.session_state.history[-6:])):
            lbl = f"**{h.get('chapter','Lesson')}** (Cl.{h.get('class_num','')})"
            with st.expander(lbl, expanded=False):
                st.caption(f"{h.get('subject','')} | {h.get('district','')} | {h.get('time','')}")
                if st.button("Reload", key=f"rl_{i}_{h.get('time',i)}"):
                    st.session_state.lesson_content = h.get("content_preview", "")
                    st.session_state.last_params    = h
                    st.rerun()
    else:
        st.caption("No lessons yet this session.")

    st.divider()
    st.markdown("### Pro Waitlist")
    st.caption("Direct WhatsApp broadcast, prompt vault, school analytics -- coming soon.")
    wl_ph = st.text_input("Phone", placeholder="03XX-XXXXXXX", label_visibility="collapsed")
    wl_sc = st.text_input("School", placeholder="School name",   label_visibility="collapsed")
    if st.button("Join Waitlist", use_container_width=True):
        if wl_ph:
            db.save_waitlist_entry(wl_ph, wl_sc, st.session_state.last_params.get("district",""))
            st.toast("Added to waitlist!")
        else:
            st.warning("Enter your phone number.")


# ════════════════════════════════════════════════════════════════════════════
# MAIN HEADER
# ════════════════════════════════════════════════════════════════════════════
ui_style.render_main_header()
st.divider()


# ════════════════════════════════════════════════════════════════════════════
# EMPTY STATE  (shown before first generation)
# ════════════════════════════════════════════════════════════════════════════
if not st.session_state.lesson_content:
    st.markdown("### What Seekho Platform creates for you")
    fc1, fc2, fc3, fc4 = st.columns(4)
    cards = [
        ("", "PCTB-Aligned Lesson", "Chapter-specific content mapped to your exact PCTB syllabus. Select class, subject, and chapter -- the engine does the rest."),
        ("", "Hyper-Local Examples", "Every analogy uses real places, occupations, and food from your district. A student in Attock sees sugarcane fields, not European forests."),
        ("", "Active Learning Design", "Concept Ladder, Quick Think breaks, and a structured AI Activity replace passive note-taking with real thinking."),
        ("", "Download + WhatsApp", "Print-ready PDF via Ctrl+P, one-click DOCX download for the print shop, and three WhatsApp messages for parents, students, and teachers."),
    ]
    for col, (icon, title, desc) in zip([fc1,fc2,fc3,fc4], cards):
        col.markdown(
            f'<div class="feature-card"><span class="fc-icon">{icon}</span>'
            f'<h4>{title}</h4><p>{desc}</p></div>',
            unsafe_allow_html=True,
        )
    st.markdown("")
    st.info("Tip: Press **Ctrl+Enter** (or **Cmd+Enter**) after filling the form to generate instantly.")
    st.divider()


# ════════════════════════════════════════════════════════════════════════════
# INPUT FORM
# ════════════════════════════════════════════════════════════════════════════
ca, cb = st.columns(2)
with ca:
    school_name = st.text_input(
        "School Name",
        value=st.session_state.last_school,
        placeholder="e.g. Govt. Boys High School Fateh Jang",
    )
with cb:
    all_districts = db.get_district_names() + ["Other (type below)"]
    d_pick = st.selectbox("District / City", all_districts,
                          index=all_districts.index(st.session_state.last_district)
                          if st.session_state.last_district in all_districts else 0)
    district_name = st.text_input("Custom district", placeholder="e.g. Chakwal") \
        if d_pick == "Other (type below)" else d_pick

c1, c2, c3 = st.columns(3)
with c1:
    class_num = st.selectbox("Class", range(1, 13), format_func=lambda x: f"Class {x}")
with c2:
    subjects = db.get_subjects(class_num)
    subject  = st.selectbox("Subject", subjects)
with c3:
    language = st.select_slider("Language",
                                options=["English","Roman Urdu","Pure Urdu (Script)"])

c4, c5 = st.columns(2)
with c4:
    chapters       = db.get_chapters(class_num, subject)
    chapter        = st.selectbox("Chapter", chapters)
with c5:
    chapter_topics = db.get_topics(class_num, subject, chapter)
    topic_opts     = ["Full Chapter Overview"] + chapter_topics
    topic          = st.selectbox("Specific Topic (optional)", topic_opts)

# Preview bar + action buttons
if school_name and district_name:
    st.markdown(
        f'<div class="meta-bar">Ready: <b>Class {class_num} {subject}</b>'
        f' | <b>{chapter}</b>'
        f'{" | " + topic if topic != "Full Chapter Overview" else ""}'
        f' | {district_name} | {language} | {output_mode}</div>',
        unsafe_allow_html=True,
    )

btn_col, reset_col, _ = st.columns([1, 1, 6])
with btn_col:
    generate = st.button("Generate", type="primary", use_container_width=True,
                         help="Ctrl+Enter also works")
with reset_col:
    if st.button("New Lesson", use_container_width=True,
                 help="Clear current lesson and start fresh"):
        st.session_state.lesson_content = ""
        st.session_state.last_params    = {}
        st.session_state.wa_messages    = ""
        st.session_state.just_generated = False
        st.rerun()


# ════════════════════════════════════════════════════════════════════════════
# VALIDATION
# ════════════════════════════════════════════════════════════════════════════
if generate:
    if not school_name.strip():
        st.warning("Please enter the school name.")
        generate = False
    if not district_name or district_name.strip() == "Other (type below)":
        st.warning("Please select or type a district name.")
        generate = False


# ════════════════════════════════════════════════════════════════════════════
# GENERATION
# ════════════════════════════════════════════════════════════════════════════
if generate:
    prompt = build_prompt(
        school=school_name, district=district_name, class_num=class_num,
        subject=subject, chapter=chapter, topic=topic, language=language,
        mode=output_mode, profile=class_profile, extra=extra,
        topics_list=chapter_topics,
    )
    with st.spinner(f"Building {output_mode} for {chapter} (Class {class_num}, {district_name})..."):
        try:
            content = gemini.models.generate_content(model=MODEL, contents=prompt).text

            params = {
                "school_name":   school_name,
                "district":      district_name,
                "class_num":     class_num,
                "subject":       subject,
                "chapter":       chapter,
                "topic":         topic,
                "language":      language,
                "output_mode":   output_mode,
                "class_profile": class_profile,
                "time":          datetime.now().strftime("%H:%M"),
                # store only preview in history to avoid memory bloat
                "content_preview": content[:400],
            }

            st.session_state.lesson_content = content
            st.session_state.last_params    = params
            st.session_state.last_school    = school_name
            st.session_state.last_district  = district_name
            st.session_state.wa_messages    = ""
            st.session_state.just_generated = True

            # Trim history to last 10 entries
            st.session_state.history.append(params)
            if len(st.session_state.history) > 10:
                st.session_state.history = st.session_state.history[-10:]

            # Save to Supabase (fire-and-forget, never blocks UI)
            try:
                db.save_lesson(
                    school_name=school_name, district=district_name,
                    class_num=class_num, subject=subject, chapter=chapter,
                    topic=topic, language=language, output_mode=output_mode,
                    class_profile=class_profile, content=content,
                )
            except Exception:
                pass

            ui_style.play_success_sound()
            st.rerun()

        except Exception as e:
            st.error(f"Generation failed: {e}")


# ════════════════════════════════════════════════════════════════════════════
# OUTPUT
# ════════════════════════════════════════════════════════════════════════════
if st.session_state.lesson_content:
    content = st.session_state.lesson_content
    p       = st.session_state.last_params

    st.divider()
    st.markdown('<div class="output-wrap">', unsafe_allow_html=True)

    # Metadata strip + DOCX button on same row
    m1,m2,m3,m4,m5,d_col = st.columns([1.5,1.5,1.7,1.5,0.9,1.5])
    m1.metric("Class",    f"Class {p.get('class_num','')}")
    m2.metric("Subject",  str(p.get("subject",""))[:18])
    m3.metric("Chapter",  str(p.get("chapter",""))[:20])
    m4.metric("District", str(p.get("district",""))[:16])
    m5.metric("Words",    str(len(content.split())))
    with d_col:
        st.markdown("<br>", unsafe_allow_html=True)
        do_docx = st.button("Download DOCX", use_container_width=True,
                            help="Download as Word document for print shop")

    if do_docx:
        with st.spinner("Building Word document..."):
            try:
                docx_bytes = generate_docx(content, p)
                fname = (
                    f"Seekho_{p.get('subject','Lesson').replace(' ','_')}_"
                    f"Cl{p.get('class_num','')}_"
                    f"{p.get('chapter','Ch').replace(' ','_')[:18]}.docx"
                )
                st.download_button(
                    "Click to download DOCX", docx_bytes, fname,
                    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    key="dl_docx",
                )
                st.toast("Word document ready!")
            except Exception as e:
                st.error(f"DOCX failed: {e}. Run: pip install python-docx")

    st.markdown("")

    # 4 tabs (no separate DOCX tab)
    tab_view, tab_edit, tab_wa, tab_refine = st.tabs([
        "Print Preview", "Edit", "WhatsApp", "AI Refine"
    ])

    # ── PRINT PREVIEW ─────────────────────────────────────────────────────
    with tab_view:
        st.success("Press **Ctrl+P** (Cmd+P on Mac) and choose **Save as PDF**.")

        hcol, ccol = st.columns([6, 1])
        with ccol:
            ui_style.copy_button(content, "copy_all")

        if p.get("language") == "Pure Urdu (Script)":
            st.markdown(f'<div class="urdu-rtl">{content}</div>', unsafe_allow_html=True)
        else:
            st.markdown(content)

        st.caption(
            f"Words: {len(content.split())} | "
            f"Generated: {p.get('time','')} | "
            f"Class {p.get('class_num','')} {p.get('subject','')} | {p.get('district','')}"
        )

    # ── EDIT ──────────────────────────────────────────────────────────────
    with tab_edit:
        st.markdown("Edit below. Changes appear in Print Preview immediately.")
        with st.expander("Add your school logo"):
            st.markdown("""
Upload your logo to [imgbb.com](https://imgbb.com) (free) and paste the link here:
```
![School Logo](PASTE_IMAGE_URL_HERE)
```
Add this line at the very top of the content.
            """)
        edited = st.text_area("Content", value=content, height=660,
                              label_visibility="collapsed")
        if edited != content:
            st.session_state.lesson_content         = edited
            st.session_state.last_params["content_preview"] = edited[:400]

    # ── WHATSAPP ──────────────────────────────────────────────────────────
    with tab_wa:
        st.markdown("### WhatsApp Distribution")
        st.markdown("Three copy-paste ready messages: parent group, student group, fellow teachers.")

        if st.button("Generate Messages", type="primary", key="wa_btn"):
            with st.spinner("Formatting for WhatsApp..."):
                st.session_state.wa_messages = gen_whatsapp(content, p)
                st.toast("Messages ready! Copy each one below.")

        if st.session_state.wa_messages:
            st.markdown(st.session_state.wa_messages)
            ui_style.copy_button(st.session_state.wa_messages, "copy_wa")
            st.caption("Tap inside any message, select all, copy, paste into WhatsApp.")

        st.divider()
        st.markdown("**Pro coming soon:** direct broadcast to parent/student/teacher groups, "
                    "open-rate tracking, scheduled sends. Join the waitlist in the sidebar.")

    # ── AI REFINE ─────────────────────────────────────────────────────────
    with tab_refine:
        st.markdown("### AI Refinement Studio")
        st.markdown("One-click upgrades or write your own instruction.")

        dist = p.get("district", "the local area")

        st.markdown("**Quick Actions:**")
        ra, rb, rc = st.columns(3)
        rd, re_, rf = st.columns(3)
        quick = None

        with ra:
            if st.button("More Local Examples", use_container_width=True):
                quick = (f"Replace every generic analogy with something specific to {dist}, Pakistan. "
                         "Use real places, real occupations, real food. Name specific people and locations.")
        with rb:
            if st.button("Simplify Language", use_container_width=True):
                quick = ("Reduce complexity by one grade level. Max 10 words per sentence. "
                         "Replace every technical word with a simpler alternative. Facts unchanged.")
        with rc:
            if st.button("Add Bloom Labels", use_container_width=True):
                quick = ("Add Bloom labels to every assessment question: "
                         "(K) Remember (U) Understand (A) Apply (AN) Analyze (E) Evaluate. "
                         "Do not change the questions.")
        with rd:
            if st.button("Add Drawing Activity", use_container_width=True):
                quick = ("Add a Draw and Label activity to the Student Handout. "
                         "Needs only pen and paper. Should reinforce the main concept visually.")
        with re_:
            if st.button("Double the MCQs", use_container_width=True):
                quick = ("Double the MCQ count. Each new MCQ: one correct answer, "
                         "three plausible distractors. Span all Bloom's levels. Local examples only.")
        with rf:
            if st.button("Roman Urdu Handout", use_container_width=True):
                quick = ("Rewrite ONLY the Student Handout section in Roman Urdu. "
                         "Keep all other sections unchanged.")

        st.markdown("")
        custom = st.text_input("Custom instruction",
                               placeholder="e.g. Add Hadith reference | Add comparison table | Use farming analogies",
                               label_visibility="collapsed")

        ac, _ = st.columns([1,4])
        with ac:
            if st.button("Apply", type="primary", use_container_width=True):
                instruction = quick or custom
                if instruction:
                    with st.spinner("Applying..."):
                        try:
                            refined = refine(content, instruction)
                            st.session_state.lesson_content = refined
                            st.session_state.last_params["content_preview"] = refined[:400]
                            st.toast("Refinement applied!")
                            st.rerun()
                        except Exception as e:
                            st.error(f"Refinement failed: {e}")
                else:
                    st.warning("Select a quick action or type an instruction first.")

    st.markdown('</div>', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# FOOTER
# ════════════════════════════════════════════════════════════════════════════
st.divider()
st.caption(
    "Seekho Platform | PCTB-Aligned | Free for all Pakistani teachers | "
    "AI-generated content -- review before use | Not affiliated with PCTB or any government body."
)
