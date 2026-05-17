"""
ui_style.py  --  Seekho Platform  Visual Layer  

"""

import json
import streamlit as st
import streamlit.components.v1 as _comp

# ── BRAND ─────────────────────────────────────────────────────────────────────
LOGO_URL      = "https://i.ibb.co/k2wpwPfV/download.png"
LOGO_FALLBACK = "https://i.ibb.co/k2wpwPfV/download.png"
PRIMARY   = "#1a7f4b"
PRIMARY_D = "#15693e"


# ─────────────────────────────────────────────────────────────────────────────
# INJECT ALL  --  call once immediately after st.set_page_config()
# ─────────────────────────────────────────────────────────────────────────────
def inject_all() -> None:
    st.markdown(f"""
<!-- Google Font: Plus Jakarta Sans -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

<!-- Animated background orbs (decorative, on top of gradient) -->
<div id="seekho-bg-orbs" aria-hidden="true">
  <div class="orb o1"></div>
  <div class="orb o2"></div>
  <div class="orb o3"></div>
  <div class="orb o4"></div>
  <div class="orb o5"></div>
</div>

<style>
/* ═══ FONT RESET ═══════════════════════════════════════════════════════════ */
                /* ═══ GLOBAL UI SCALE ══════════════════════════════════════════════════════ */
html {{
    font-size: 18px !important; 
}}
html, body, h1, h2, h3, h4, h5, h6, p, div, 
input, textarea, select, button, label, th, td {{
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
}}

/* ═══ PROTECT ICONS ════════════════════════════════════════════════════════ */
span.material-symbols-rounded,
span.material-icons,
[data-testid="collapsedControl"],
[data-testid="collapsedControl"] *,
[class*="icon" i],
[class*="Icon" i] {{
    font-family: "Material Symbols Rounded", "Material Icons", sans-serif !important;
    font-feature-settings: "liga" !important;
}}

/* ═══ HIDE HEADER BACKGROUND ══════════════════════════════════════════════ */
header[data-testid="stHeader"] {{
    background: transparent !important;
    border: none !important;
    height: 0px !important; /* Collapses the bar but keeps children accessible */
}}

/* ═══ THE UNIVERSAL FLOATING SIDEBAR BUTTON ═══════════════════════════════ */
/* This targets the button whether the sidebar is OPEN or CLOSED */
[data-testid="stSidebarCollapseButton"],
button[aria-label="Open sidebar"],
button[aria-label="Close sidebar"] {{
    background-color: {PRIMARY} !important;
    color: white !important;
    border-radius: 50% !important;
    width: 60px !important;
    height: 60px !important;
    position: fixed !important;
    top: 20px !important;
    left: 20px !important;
    z-index: 1000001 !important; /* Higher than everything else */
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    box-shadow: 0 4px 15px rgba(26,127,75,0.4) !important;
    transition: transform 0.2s ease !important;
}}

/* Scale the actual icon/SVG inside the button */
[data-testid="stSidebarCollapseButton"] svg,
button[aria-label="Open sidebar"] svg,
button[aria-label="Close sidebar"] svg {{
    width: 35px !important;
    height: 35px !important;
    fill: white !important;
    color: white !important;
}}

/* Ensure the button stays visible on hover */
[data-testid="stSidebarCollapseButton"]:hover {{
    transform: scale(1.1) !important;
    background-color: {PRIMARY_D} !important;
}}
/* We are leaving the header visible so the sidebar button doesn't vanish */

/* ═══ APP BACKGROUND (Greenish Blue Gradient) ══════════════════════════════ */
.stApp {{
    background: linear-gradient(145deg, #dcfce7 0%, #e0f2fe 50%, #ccfbf1 100%) !important;
    min-height: 100vh;
}}

/* ═══ BACKGROUND ORBS (decorative, not structural) ════════════════════════ */
#seekho-bg-orbs {{
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    overflow: hidden;
}}

@keyframes orb1 {{
    0%,100% {{ transform: translate(0,0) scale(1); }}
    33%      {{ transform: translate(65px,-85px) scale(1.07); }}
    66%      {{ transform: translate(-45px,55px) scale(0.95); }}
}}
@keyframes orb2 {{
    0%,100% {{ transform: translate(0,0) scale(1); }}
    40%      {{ transform: translate(-75px,65px) scale(1.09); }}
    70%      {{ transform: translate(50px,-40px) scale(0.93); }}
}}
@keyframes orb3 {{
    0%,100% {{ transform: translate(0,0) scale(1); }}
    25%      {{ transform: translate(45px,75px) scale(1.05); }}
    75%      {{ transform: translate(-60px,-30px) scale(0.97); }}
}}
@keyframes orb4 {{
    0%,100% {{ transform: translate(0,0) scale(1); }}
    50%      {{ transform: translate(-35px,-55px) scale(1.1); }}
}}
@keyframes orb5 {{
    0%,100% {{ transform: translate(0,0) scale(1); }}
    45%      {{ transform: translate(55px,45px) scale(0.92); }}
}}

.orb {{
    position: absolute;
    border-radius: 50%;
    filter: blur(90px);
    pointer-events: none;
}}
.o1 {{
    width: 540px; height: 540px;
    top: -170px; left: -150px;
    background: radial-gradient(circle, rgba(26,127,75,.20) 0%, rgba(13,148,136,.10) 55%, transparent 80%);
    animation: orb1 34s ease-in-out infinite;
}}
.o2 {{
    width: 400px; height: 400px;
    top: 28vh; right: -110px;
    background: radial-gradient(circle, rgba(99,102,241,.13) 0%, rgba(26,127,75,.08) 55%, transparent 80%);
    animation: orb2 28s ease-in-out infinite;
}}
.o3 {{
    width: 360px; height: 360px;
    bottom: 8vh; left: 16vw;
    background: radial-gradient(circle, rgba(13,148,136,.14) 0%, rgba(26,127,75,.07) 55%, transparent 80%);
    animation: orb3 40s ease-in-out infinite;
}}
.o4 {{
    width: 260px; height: 260px;
    top: 52vh; left: 6vw;
    background: radial-gradient(circle, rgba(34,197,94,.11) 0%, transparent 70%);
    animation: orb4 24s ease-in-out infinite;
}}
.o5 {{
    width: 300px; height: 300px;
    top: 10vh; right: 20vw;
    background: radial-gradient(circle, rgba(26,127,75,.12) 0%, rgba(99,102,241,.07) 60%, transparent 80%);
    animation: orb5 31s ease-in-out infinite reverse;
}}

/* Ensure content renders above orbs */
.block-container,
[data-testid="stSidebar"] > div {{
    position: relative;
    z-index: 1;
}}

/* Glass card for main content area */
/* ═══ MAIN CONTENT GLASS CARD ══════════════════════════════════════════════ */
.main .block-container {{
    background: rgba(255, 255, 255, 0.92) !important; 
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.3);
    padding: 2.5rem !important;
    margin-top: 1.5rem;
    color: #0f172a !important; 
}}

/* ═══ SIDEBAR ══════════════════════════════════════════════════════════════ */
[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, #090f1e 0%, #0d1f36 55%, #091a0f 100%) !important;
    border-right: 1px solid rgba(255,255,255,0.05);
}}
[data-testid="stSidebar"] * {{ color: #c8d5e8 !important; }}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] strong   {{ color: #e8edf5 !important; }}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {{
    color: #7a8fa8 !important; font-size: 0.82rem; line-height: 1.55;
}}
[data-testid="stSidebar"] hr {{
    border: none !important; height: 1px !important;
    background: rgba(255,255,255,0.07) !important; margin: 1rem 0 !important;
}}
[data-testid="stSidebar"] .stRadio label  {{ color: #b8cade !important; font-size: 0.88rem; }}
[data-testid="stSidebar"] .stTextInput input,
[data-testid="stSidebar"] .stTextArea textarea {{
    background: rgba(255,255,255,0.07) !important;
    border: 1px solid rgba(255,255,255,0.11) !important;
    color: #dde8f4 !important; border-radius: 8px !important;
}}
[data-testid="stSidebar"] [data-testid="stSelectbox"] > div > div {{
    background: rgba(255,255,255,0.07) !important;
    border: 1px solid rgba(255,255,255,0.11) !important;
    border-radius: 8px !important; color: #dde8f4 !important;
}}
[data-testid="stSidebar"] .stButton > button {{
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    color: #c8d5e8 !important; border-radius: 8px !important;
    font-size: 0.83rem !important; font-weight: 500 !important;
    width: 100% !important;
    transition: background .15s, border-color .15s !important;
}}
[data-testid="stSidebar"] .stButton > button:hover {{
    background: rgba(255,255,255,0.14) !important;
    border-color: rgba(255,255,255,0.23) !important;
    color: #eef3ff !important;
}}
[data-testid="stSidebar"] .stExpander {{
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 8px !important;
}}

/* ═══ PRIMARY BUTTON ═══════════════════════════════════════════════════════ */
.stButton > button[kind="primary"] {{
    background: linear-gradient(135deg, {PRIMARY} 0%, #22a862 100%) !important;
    color: white !important; border: none !important;
    border-radius: 11px !important; font-weight: 700 !important;
    font-size: 0.95rem !important; letter-spacing: 0.2px;
    padding: 0.6rem 1.8rem !important; position: relative; overflow: hidden;
    transition: transform .18s ease, box-shadow .18s ease !important;
    box-shadow: 0 3px 14px rgba(26,127,75,.32) !important;
}}
.stButton > button[kind="primary"]:hover {{
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 26px rgba(26,127,75,.46) !important;
}}
.stButton > button[kind="primary"]:active {{
    transform: translateY(0) !important;
    box-shadow: 0 2px 8px rgba(26,127,75,.30) !important;
}}

/* ═══ SECONDARY BUTTONS ════════════════════════════════════════════════════ */
.stButton > button:not([kind="primary"]) {{
    background: rgba(255,255,255,0.88) !important;
    border: 1.5px solid #dde5f0 !important; border-radius: 9px !important;
    color: #374151 !important; font-weight: 500 !important; font-size: 0.85rem !important;
    backdrop-filter: blur(6px);
    transition: border-color .15s, color .15s, transform .15s, box-shadow .15s !important;
    box-shadow: 0 1px 4px rgba(0,0,0,.05) !important;
}}
.stButton > button:not([kind="primary"]):hover {{
    border-color: {PRIMARY} !important; color: {PRIMARY} !important;
    background: rgba(240,253,244,.92) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(26,127,75,.14) !important;
}}

/* ═══ TEXT INPUTS ══════════════════════════════════════════════════════════ */
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea {{
    background: rgba(248,250,252,.92) !important;
    border: 1.5px solid #dde5f0 !important; border-radius: 10px !important;
    font-size: 0.9rem !important; color: #1e293b !important;
    transition: border-color .15s, box-shadow .15s, background .15s !important;
}}
[data-testid="stTextInput"] input:focus,
[data-testid="stTextArea"] textarea:focus {{
    border-color: {PRIMARY} !important;
    box-shadow: 0 0 0 3px rgba(26,127,75,.13) !important;
    background: rgba(255,255,255,.99) !important; outline: none !important;
}}
[data-testid="stTextInput"] input::placeholder,
[data-testid="stTextArea"] textarea::placeholder {{ color: #94a3b8 !important; }}

/* ═══ SELECT BOXES ═════════════════════════════════════════════════════════ */
[data-testid="stSelectbox"] > div > div {{
    background: rgba(248,250,252,.92) !important;
    border: 1.5px solid #dde5f0 !important; border-radius: 10px !important;
    transition: border-color .15s, box-shadow .15s !important;
}}
[data-testid="stSelectbox"] > div > div:hover {{
    border-color: {PRIMARY} !important;
    box-shadow: 0 0 0 2px rgba(26,127,75,.09) !important;
}}

/* ═══ TABS ══════════════════════════════════════════════════════════════════ */
.stTabs [data-baseweb="tab-list"] {{
    background: rgba(236,239,248,.88) !important; border-radius: 12px !important;
    padding: 4px !important; gap: 2px !important; border: none !important;
    backdrop-filter: blur(6px);
}}
.stTabs [data-baseweb="tab"] {{
    border-radius: 9px !important; font-weight: 500 !important;
    font-size: 0.87rem !important; color: #64748b !important;
    border: none !important; padding: .4rem 1rem !important; transition: all .15s !important;
}}
.stTabs [aria-selected="true"] {{
    background: white !important; color: {PRIMARY} !important;
    box-shadow: 0 1px 6px rgba(0,0,0,.10) !important; font-weight: 700 !important;
}}
.stTabs [data-baseweb="tab-panel"] {{ padding-top: 1.25rem !important; }}

/* ═══ METRICS ═══════════════════════════════════════════════════════════════ */
[data-testid="stMetric"] {{
    background: rgba(255,255,255,.82) !important;
    border: 1px solid rgba(224,232,244,.9) !important; border-radius: 12px !important;
    padding: .8rem 1rem !important; backdrop-filter: blur(8px);
    box-shadow: 0 1px 6px rgba(0,0,0,.05) !important;
    transition: transform .15s, box-shadow .15s !important;
}}
[data-testid="stMetric"]:hover {{
    transform: translateY(-2px) !important;
    box-shadow: 0 5px 16px rgba(0,0,0,.09) !important;
}}
[data-testid="stMetricLabel"] {{
    color: #64748b !important; font-size: .72rem !important;
    font-weight: 700 !important; text-transform: uppercase !important; letter-spacing: .6px !important;
}}
[data-testid="stMetricValue"] {{
    color: #1e293b !important; font-size: .92rem !important; font-weight: 700 !important;
}}

/* ═══ EXPANDERS ═════════════════════════════════════════════════════════════ */
[data-testid="stExpander"] {{
    border: 1px solid #e4ecf5 !important; border-radius: 10px !important;
    background: rgba(255,255,255,.72) !important;
    backdrop-filter: blur(6px); overflow: hidden !important;
    transition: box-shadow .15s !important;
}}
[data-testid="stExpander"]:hover {{ box-shadow: 0 3px 14px rgba(0,0,0,.07) !important; }}

/* ═══ ALERTS ════════════════════════════════════════════════════════════════ */
[data-testid="stAlert"] {{
    border-radius: 10px !important; border: none !important;
    backdrop-filter: blur(6px); font-size: .88rem !important;
}}

/* ═══ DIVIDER ═══════════════════════════════════════════════════════════════ */
hr {{
    border: none !important; height: 1px !important;
    background: linear-gradient(to right, transparent, #d8e2f0, transparent) !important;
    margin: 1.4rem 0 !important;
}}

/* ═══ META BAR ══════════════════════════════════════════════════════════════ */
.meta-bar {{
    background: rgba(255,255,255,.78); border: 1px solid rgba(218,228,242,.8);
    border-radius: 10px; padding: .6rem 1rem;
    font-size: .85rem; color: #475569; margin-bottom: 1rem;
    backdrop-filter: blur(8px); box-shadow: 0 1px 5px rgba(0,0,0,.04);
}}

/* ═══ MAIN HEADER ═══════════════════════════════════════════════════════════ */
.seekho-header {{
    display: flex; align-items: center; gap: 14px;
    padding: .5rem 0 1rem 0;
}}
.seekho-header img {{
    width: 150px; height: 150px; border-radius: 12px; object-fit: contain;
    box-shadow: 0 3px 12px rgba(26,127,75,.25);
}}
.seekho-header-text h1 {{
    font-size: 1.6rem !important; font-weight: 800 !important;
    color: #0f172a !important; margin: 0 !important; letter-spacing: -.4px; line-height: 1.15;
}}
.seekho-header-text p {{
    font-size: .82rem !important; color: #64748b !important;
    margin: 2px 0 0 !important; letter-spacing: .1px;
}}

/* ═══ SIDEBAR LOGO BLOCK ════════════════════════════════════════════════════ */
.sb-logo {{
    display: flex; align-items: center; gap: 10px;
    padding: 1.2rem 1rem 1rem;
    border-bottom: 1px solid rgba(255,255,255,.07); margin-bottom: .5rem;
}}
.sb-logo img {{
    width: 90px; height: 90px; border-radius: 8px; object-fit: contain;
}}
.sb-logo span {{
    font-size: 1rem !important; font-weight: 800 !important;
    color: #e8edf5 !important; letter-spacing: -.2px;
}}

/* ═══ STAT PILLS ═══════════════════════════════════════════════════════════ */
.stat-pill {{
    display: inline-flex; align-items: center; gap: 5px;
    background: rgba(26,127,75,.12); border: 1px solid rgba(26,127,75,.22);
    border-radius: 20px; padding: 3px 10px;
    font-size: .78rem; font-weight: 600; color: #a3e4c1; margin: 3px 4px 3px 0;
}}

/* ═══ FAST & SMOOTH HOVER-REVEAL CARDS ════════════════════════════════════ */
.feature-card {{
    background: rgba(255, 255, 255, 0.98) !important;
    border: 1px solid rgba(255, 255, 255, 0.4);
    
    /* Starting Circle */
    width: 200px;
    height: 200px;
    border-radius: 50% !important;
    
    margin: 15px auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 25px;
    
    /* Snappy 0.4s Timing */
    transition: all 0.4s ease-out !important;
    cursor: pointer;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
    overflow: hidden;
}}

.feature-card h4 {{
    font-size: 1rem !important;
    font-weight: 800 !important;
    color: {PRIMARY} !important;
    margin: 6px 0 !important;
    transition: all 0.3s ease-out;
}}

.feature-card p {{
    opacity: 0;
    max-height: 0;
    overflow: hidden;
    font-size: 0.85rem !important;
    color: #334155 !important;
    line-height: 1.4;
    margin: 0 !important;
    /* Faster text fade */
    transition: opacity 0.3s ease-out, max-height 0.4s ease-out;
}}

/* ═══ THE FAST TRANSFORMATION ═════════════════════════════════════════════ */
.feature-card:hover {{
    border-radius: 16px !important;
    width: 100%; 
    height: 240px; 
    background: white !important;
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.3);
}}

.feature-card:hover p {{
    opacity: 1;
    max-height: 200px; 
    margin-top: 10px !important;
}}

.feature-card .fc-icon {{
    font-size: 2.2rem;
    transition: transform 0.4s ease-out;
}}

.feature-card:hover .fc-icon {{
    transform: scale(1.1);
}}

/* ═══ RTL URDU ══════════════════════════════════════════════════════════════ */
.urdu-rtl {{
    direction: rtl; text-align: right;
    font-family: 'Noto Nastaliq Urdu','Amiri',serif !important;
    font-size: 1.15em; line-height: 2.4;
    padding: 1.2rem 1.6rem;
    background: rgba(255,253,245,.92); border-right: 4px solid {PRIMARY};
    border-radius: 10px; backdrop-filter: blur(4px);
}}

/* ═══ PRINT ══════════════════════════════════════════════════════════════════ */
@media print {{
    #seekho-bg-orbs, [data-testid="stSidebar"],
    .stButton, [data-testid="stTabs"] nav,
    [data-testid="stAlert"], footer, header,
    .meta-bar {{ display:none !important; }}
    .main .block-container {{
        background: white !important; box-shadow: none !important;
        border: none !important; padding: 0 !important; max-width: 100% !important;
    }}
    .stApp {{ background: white !important; }}
}}
</style>

<!-- FIX 3: Audio context unlock on first user gesture (stored on window for iframes to access) -->
<!-- FIX: Keyboard shortcut Ctrl+Enter triggers Generate                                       -->
<!-- FIX: Button ripple effect                                                                 -->
<script>
(function(){{
    // ── Audio unlock on first click/keydown ─────────────────────────────
    // AudioContext requires a user gesture. We unlock it on the first interaction
    // and store it on window so _comp.html iframes can access it via window.parent.
    function unlockAudio(){{
        if(window._seekhoAudioCtx) return;
        try{{
            window._seekhoAudioCtx = new(window.AudioContext || window.webkitAudioContext)();
        }}catch(e){{}}
    }}
    document.addEventListener('click',  unlockAudio, {{passive:true}});
    document.addEventListener('keydown', unlockAudio, {{passive:true}});

    // ── Ctrl+Enter shortcut ──────────────────────────────────────────────
    document.addEventListener('keydown', function(e){{
        if((e.ctrlKey||e.metaKey) && e.key==='Enter'){{
            document.querySelectorAll('button').forEach(function(b){{
                if(b.innerText.trim().toLowerCase()==='generate') b.click();
            }});
        }}
    }});

    // ── Ripple on primary buttons ────────────────────────────────────────
    var rStyle=document.createElement('style');
    rStyle.textContent='@keyframes ripple{{to{{transform:scale(3);opacity:0;}}}}';
    document.head.appendChild(rStyle);

    function attachRipple(btn){{
        if(btn.dataset.ripple) return;
        btn.dataset.ripple='1';
        btn.style.position='relative'; btn.style.overflow='hidden';
        btn.addEventListener('click',function(e){{
            var c=document.createElement('span');
            var d=Math.max(btn.clientWidth,btn.clientHeight);
            var r=btn.getBoundingClientRect();
            c.style.cssText=[
                'position:absolute','border-radius:50%',
                'background:rgba(255,255,255,.28)','pointer-events:none',
                'animation:ripple .52s linear',
                'width:'+d+'px','height:'+d+'px',
                'left:'+(e.clientX-r.left-d/2)+'px',
                'top:'+(e.clientY-r.top-d/2)+'px'
            ].join(';');
            btn.appendChild(c);
            setTimeout(function(){{c.remove();}},560);
        }});
    }}
    var obs=new MutationObserver(function(){{
        document.querySelectorAll('button[kind="primary"]').forEach(attachRipple);
    }});
    obs.observe(document.body,{{childList:true,subtree:true}});
    document.querySelectorAll('button[kind="primary"]').forEach(attachRipple);
}})();
</script>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# SPLASH  (FIX 1 + FIX 3: set splash_done=True immediately, return False always)
# ─────────────────────────────────────────────────────────────────────────────
def maybe_show_splash() -> bool:
    """
    Shows an animated full-screen splash on the very first page load.

    FIX 1: Sets splash_done = True immediately so the next Streamlit rerun
            never shows the splash again.
    FIX 3: Plays a welcome chord using the AudioContext that inject_all()
            already unlocked (since the user will have clicked something to
            reach the app -- or we use autoplay on page interaction).
    
    The splash is a position:fixed CSS overlay. The app renders UNDERNEATH it.
    After 3.4s the CSS animation fades the overlay out, revealing the app.
    No st.stop() needed. No blank-page-after-fade. No unreachable buttons.

    Always returns False so the caller never calls st.stop().
    """
    if st.session_state.get("splash_done"):
        return False

    # Mark as shown IMMEDIATELY so reruns never re-trigger
    st.session_state.splash_done = True

    st.markdown(f"""
<style>
/* Splash overlay: covers the app while it loads, then auto-fades */
@keyframes splashFadeOut {{
    0%   {{ opacity: 1; pointer-events: auto; }}
    75%  {{ opacity: 1; pointer-events: auto; }}
    100% {{ opacity: 0; pointer-events: none; }}
}}
#sp {{
    position: fixed; inset: 0;
    background: linear-gradient(145deg, #060d1a 0%, #0b1d35 55%, #060f0a 100%);
    z-index: 999999;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    animation: splashFadeOut 3.6s ease-out forwards;
}}

/* Individual element entrance animations */
@keyframes logoIn {{
    from {{ opacity:0; transform:scale(.62) translateY(12px); }}
    to   {{ opacity:1; transform:scale(1) translateY(0); }}
}}
@keyframes textUp {{
    from {{ opacity:0; transform:translateY(24px); }}
    to   {{ opacity:1; transform:translateY(0); }}
}}
@keyframes fadeIn {{
    from {{ opacity:0; }}
    to   {{ opacity:1; }}
}}
@keyframes shimmer {{
    0%   {{ background-position: -220% center; }}
    100% {{ background-position: 220% center; }}
}}
@keyframes dotPulse {{
    0%,100% {{ opacity:.45; transform:scale(1); }}
    50%      {{ opacity:1;   transform:scale(1.18); }}
}}

#sp-logo {{
    width: 200px; height: 200px; border-radius: 22px; object-fit: contain;
    margin-bottom: 28px;
    animation: logoIn .72s cubic-bezier(.34,1.56,.64,1) .15s both;
    box-shadow: 0 12px 44px rgba(26,127,75,.42), 0 0 0 1px rgba(255,255,255,.07);
}}
#sp-title {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 2.75rem; font-weight: 800; letter-spacing: -.7px; margin: 0;
    background: linear-gradient(90deg, #ffffff 0%, #a3e4c1 44%, #ffffff 84%);
    background-size: 200% auto;
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
    animation: textUp .62s ease .72s both, shimmer 3.8s linear 1.4s infinite;
}}
#sp-tag {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 1rem; color: rgba(148,163,184,.9);
    margin: 12px 0 0; font-weight: 400;
    animation: fadeIn .8s ease 1.1s both;
    text-align: center; letter-spacing: .15px;
}}
#sp-urdu {{
    font-family: 'Noto Nastaliq Urdu', serif;
    font-size: 1.06rem; color: rgba(163,228,193,.68);
    margin: 7px 0 0; direction: rtl;
    animation: fadeIn .8s ease 1.3s both;
}}
#sp-dots {{
    display: flex; gap: 8px; margin-top: 44px;
    animation: fadeIn .5s ease 1.6s both;
}}
.sp-dot {{
    width: 7px; height: 7px; border-radius: 50%;
    background: rgba(26,127,75,.55);
    animation: dotPulse 1.4s ease-in-out infinite;
}}
.sp-dot:nth-child(2) {{ animation-delay: .22s; }}
.sp-dot:nth-child(3) {{ animation-delay: .44s; }}
#sp-hint {{
    position: absolute; bottom: 36px;
    font-family: 'Plus Jakarta Sans', sans-serif; font-size: .8rem;
    color: rgba(100,116,139,.6);
    animation: fadeIn 1s ease 2.4s both; letter-spacing: .3px;
}}
</style>

<div id="sp">
  <img id="sp-logo"
       src="{LOGO_URL}"
       onerror="this.src='{LOGO_FALLBACK}'; this.onerror=null;"
       alt="Seekho Platform">
  <h1 id="sp-title">Seekho Platform</h1>
  <p id="sp-tag">Pakistan's Hyper-Local AI Curriculum Engine</p>
  <p id="sp-urdu">پاکستانی اساتذہ کے لیے ذہین نصاب</p>
  <div id="sp-dots">
    <div class="sp-dot"></div>
    <div class="sp-dot"></div>
    <div class="sp-dot"></div>
  </div>
  <p id="sp-hint">Loading your workspace...</p>
</div>

<script>
// FIX 3: Welcome chord
// AudioContext is created fresh here since this is the first page interaction.
// We also store it on window so inject_all's audio system can use it.
(function(){{
    try {{
        if(!window._seekhoAudioCtx){{
            window._seekhoAudioCtx = new(window.AudioContext || window.webkitAudioContext)();
        }}
        var ctx = window._seekhoAudioCtx;
        // Gentle C-E-G chord
        var notes = [[523.25, 0.5, 0.9, 0.10], [659.25, 0.68, 0.8, 0.08], [783.99, 0.82, 0.7, 0.07]];
        notes.forEach(function(n){{
            var osc = ctx.createOscillator();
            var gain = ctx.createGain();
            osc.connect(gain); gain.connect(ctx.destination);
            osc.type = 'sine'; osc.frequency.value = n[0];
            gain.gain.setValueAtTime(0, ctx.currentTime + n[1]);
            gain.gain.linearRampToValueAtTime(n[3], ctx.currentTime + n[1] + 0.05);
            gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + n[1] + n[2]);
            osc.start(ctx.currentTime + n[1]);
            osc.stop(ctx.currentTime + n[1] + n[2]);
        }});
    }} catch(e) {{
        // AudioContext blocked or unavailable -- silent fallback
    }}
}})();
</script>
""", unsafe_allow_html=True)

    # Always return False: app renders underneath the CSS overlay.
    # The overlay auto-fades via animation. No st.stop() needed.
    return False


# ── SIDEBAR LOGO ──────────────────────────────────────────────────────────────
def render_sidebar_logo() -> None:
    st.markdown(f"""
<div class="sb-logo">
  <img src="{LOGO_URL}"
       onerror="this.src='{LOGO_FALLBACK}'; this.onerror=null;"
       alt="Seekho Platform">
  <span>Seekho Platform</span>
</div>""", unsafe_allow_html=True)


# ── MAIN PAGE HEADER ──────────────────────────────────────────────────────────
def render_main_header() -> None:
    st.markdown(f"""
<div class="seekho-header">
  <img src="{LOGO_URL}"
       onerror="this.src='{LOGO_FALLBACK}'; this.onerror=null;"
       alt="Seekho Platform">
  <div class="seekho-header-text">
    <h1>Seekho Platform</h1>
    <p>Pakistan's Hyper-Local AI Curriculum Engine &nbsp;|&nbsp; PCTB-Aligned &nbsp;|&nbsp; Class 1-12 &nbsp;|&nbsp; Active Learning</p>
  </div>
</div>""", unsafe_allow_html=True)


# ── SUCCESS SOUND ─────────────────────────────────────────────────────────────
def play_success_sound() -> None:
    """
    FIX 3: Plays a soft three-note ascending chime.
    Uses window.parent._seekhoAudioCtx so the AudioContext unlocked by inject_all()
    (on the main page) is reused. height=1 ensures browsers execute the iframe JS.
    """
    _comp.html("""
<script>
(function(){
    try {
        // Access the AudioContext that inject_all() unlocked on the parent page
        var ctx = window.parent && window.parent._seekhoAudioCtx;
        if (!ctx) return;  // Not unlocked yet -- skip silently

        var notes = [[880, 0, .18, .10], [1047, .14, .22, .08], [1319, .26, .30, .07]];
        notes.forEach(function(n) {
            var osc = ctx.createOscillator();
            var gain = ctx.createGain();
            osc.connect(gain); gain.connect(ctx.destination);
            osc.type = 'sine'; osc.frequency.value = n[0];
            gain.gain.setValueAtTime(0, ctx.currentTime + n[1]);
            gain.gain.linearRampToValueAtTime(n[3], ctx.currentTime + n[1] + 0.04);
            gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + n[1] + n[2]);
            osc.start(ctx.currentTime + n[1]);
            osc.stop(ctx.currentTime + n[1] + n[2]);
        });
    } catch(e) {}
})();
</script>
""", height=1)  # height=1 (not 0): ensures browsers execute JS in the iframe


# ── COPY-TO-CLIPBOARD ─────────────────────────────────────────────────────────
def copy_button(text: str, key: str) -> None:
    js_string = json.dumps(text)
    _comp.html(f"""
<button
  id="cb-{key}"
  style="
    font-family: 'Plus Jakarta Sans', sans-serif; font-size: .78rem; font-weight: 600;
    background: rgba(255,255,255,.88); border: 1.5px solid #dde5f0;
    border-radius: 7px; padding: 4px 14px; cursor: pointer; color: #475569;
    transition: all .15s; backdrop-filter: blur(4px);
  "
  onmouseover="this.style.color='#1a7f4b'; this.style.borderColor='#1a7f4b';"
  onmouseout="this.style.color='#475569'; this.style.borderColor='#dde5f0';"
>
  Copy
</button>
<script>
  var contentToCopy = {js_string};
  document.getElementById('cb-{key}').addEventListener('click', function() {{
      navigator.clipboard.writeText(contentToCopy).then(function() {{
          var b = document.getElementById('cb-{key}');
          b.innerText = 'Copied!';
          b.style.color = '#1a7f4b';
          b.style.borderColor = '#1a7f4b';
          setTimeout(function() {{
              b.innerText = 'Copy';
              b.style.color = '#475569';
              b.style.borderColor = '#dde5f0';
          }}, 1800);
      }}).catch(function() {{
          var b = document.getElementById('cb-{key}');
          b.innerText = 'Failed';
      }});
  }});
</script>
""", height=36)