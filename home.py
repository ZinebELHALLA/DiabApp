# home.py
import streamlit as st

st.set_page_config(page_title="DiabApp", layout="centered", initial_sidebar_state="collapsed")

# === LANGUE ===
lang = st.selectbox("اللغة / Langue", ["العربية", "Français"], index=1)

# === TEXTES BILINGUES ===
texts = {
    "العربية": {
        "title": "مخاطر السكري",
        "subtitle": "قم بتقييم مخاطر الإصابة بالسكري في دقيقتين",
        "button": "ابدأ التقييم"
    },
    "Français": {
        "title": "DiabApp",
        "subtitle": "Évaluez votre risque de diabète en 2 minutes",
        "button": "Commencer l'évaluation"
    }
}

t = texts[lang]

# === STYLE ===
st.markdown(f"""
<style>
    .main {{
        background: linear-gradient(to right, #1dd1a1, #48dbfb);
        color: white;
        padding: 3rem;
        font-family: 'Segoe UI', sans-serif;
    }}
    .title {{font-size: 3.8rem; font-weight: bold; text-align: center; margin: 2rem 0;}}
    .subtitle {{font-size: 1.6rem; text-align: center; margin-bottom: 4rem; opacity: 0.9;}}
    .stSelectbox {{text-align: center; margin-bottom: 2rem;}}
    .stButton>button {{
        background: white; color: #ff6b6b; font-weight: bold; font-size: 1.4rem;
        border-radius: 25px; height: 4.5rem; width: 100%; border: none;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2); transition: all 0.3s;
    }}
    .stButton>button:hover {{background: #f8f9fa; transform: scale(1.05);}}
</style>
""", unsafe_allow_html=True)

st.markdown(f"<h1 class='title'>{t['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='subtitle'>{t['subtitle']}</p>", unsafe_allow_html=True)

if st.button(t["button"]):
    st.session_state.lang = lang
    st.switch_page("pages/1_Predicteur.py")