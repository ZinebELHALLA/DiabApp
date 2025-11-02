# pages/1_Predicteur.py
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Évaluation", layout="centered", initial_sidebar_state="collapsed")

# === LANGUE (récupérée depuis home.py) ===
lang = st.session_state.get("lang", "Français")

# === TEXTES BILINGUES ===
texts = {
    "العربية": {
        "title": "تقييم المخاطر",
        "health": "صحتك",
        "diseases": "الأمراض",
        "lifestyle": "نمط الحياة",
        "medical": "المتابعة الطبية",
        "perceived": "الصحة المتصورة",
        "profile": "ملفك الشخصي",
        "weight_height": "الوزن والطول",
        "weight": "الوزن (كغ)",
        "height": "الطول (سم)",
        "bmi": "مؤشر كتلة الجسم",
        "sex": "الجنس",
        "age": "العمر",
        "education": "المستوى التعليمي",
        "income": "الدخل السنوي",
        "submit": "تقييم المخاطر",
        "result": "نتيجة التقييم",
        "high_risk": "مخاطر عالية جدًا",
        "elevated_risk": "مخاطر مرتفعة",
        "moderate_risk": "مخاطر متوسطة",
        "low_risk": "مخاطر منخفضة",
        "advice": "نصائح مخصصة",
        "weight_loss": "فقدان الوزن",
        "activity": "نشاط بدني",
        "checkup": "فحص طبي",
        "diet": "التغذية",
        "smoking": "التدخين",
        "well_done": "ممتاز!"
    },
    "Français": {
        "title": "Évaluation du risque",
        "health": "Votre santé",
        "diseases": "Maladies",
        "lifestyle": "Mode de vie",
        "medical": "Suivi médical",
        "perceived": "Santé perçue",
        "profile": "Profil personnel",
        "weight_height": "Poids & Taille",
        "weight": "Poids (kg)",
        "height": "Taille (cm)",
        "bmi": "IMC",
        "sex": "Sexe",
        "age": "Âge",
        "education": "Niveau d'éducation",
        "income": "Revenu annuel",
        "submit": "Évaluer mon risque",
        "result": "Votre résultat",
        "high_risk": "RISQUE TRÈS ÉLEVÉ",
        "elevated_risk": "RISQUE ÉLEVÉ",
        "moderate_risk": "RISQUE MODÉRÉ",
        "low_risk": "RISQUE FAIBLE",
        "advice": "Conseils personnalisés",
        "weight_loss": "Perte de poids",
        "activity": "Activité physique",
        "checkup": "Bilan médical",
        "diet": "Alimentation",
        "smoking": "Arrêt du tabac",
        "well_done": "Bravo !"
    }
}

t = texts[lang]

# === STYLE ===
st.markdown(f"""
<style>
    .main {{background-color: #f8f9fa; font-family: 'Segoe UI', sans-serif;}}
    .card {{padding: 1.5em; border-radius: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); margin: 1em 0;}}
    .high-risk {{background: linear-gradient(135deg, #ff6b6b, #ff8e8e); color: white;}}
    .moderate-risk {{background: linear-gradient(135deg, #feca57, #ff9ff3); color: white;}}
    .low-risk {{background: linear-gradient(135deg, #1dd1a1, #48dbfb); color: white;}}
    .advice-card {{padding: 1.2em; border-radius: 12px; margin: 0.5em 0; color: white;}}
    .stButton>button {{background: #ff6b6b; color: white; font-weight: bold; border-radius: 12px; height: 3em; width: 100%;}}
</style>
""", unsafe_allow_html=True)

# === CHARGEMENT MODÈLE ===
@st.cache_resource
def load_model():
    return joblib.load('diabetes_best_model.pkl')  # Chemin relatif

model = load_model()

# === MAPPINGS (inchangés) ===
GEN_HLTH_MAP = {"Excellente": 1, "Très bonne": 2, "Bonne": 3, "Moyenne": 4, "Mauvaise": 5}
EDUCATION_MAP = {v: k for k, v in enumerate([
    "Jamais allé à l'école", "Primaire", "Collège", "Lycée",
    "Université", "Diplôme supérieur"
], 1)}
INCOME_MAP = {v: k for k, v in enumerate([
    "< 10 000 €", "10–15k €", "15–20k €", "20–25k €",
    "25–35k €", "35–50k €", "50–75k €", "> 75 000 €"
], 1)}
AGE_MAP = {v: k for k, v in enumerate([
    "18-24 ans", "25-29 ans", "30-34 ans", "35-39 ans",
    "40-44 ans", "45-49 ans", "50-54 ans", "55-59 ans",
    "60-64 ans", "65-69 ans", "70-74 ans", "75-79 ans", "80+ ans"
], 1)}

# === FORMULAIRE ===
with st.form("health_form"):
    st.markdown(f"### {t['health']}")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"**{t['diseases']}**")
        high_bp = st.checkbox("J'ai de l'hypertension" if lang == "Français" else "أعاني من ارتفاع ضغط الدم")
        high_chol = st.checkbox("J'ai un cholestérol élevé" if lang == "Français" else "أعاني من ارتفاع الكوليسترول")
        stroke = st.checkbox("J'ai fait un AVC" if lang == "Français" else "أصبت بسكتة دماغية")
        heart_disease = st.checkbox("J'ai une maladie cardiaque" if lang == "Français" else "أعاني من مرض قلبي")
        diff_walk = st.checkbox("J'ai du mal à marcher" if lang == "Français" else "أواجه صعوبة في المشي")

        st.markdown(f"**{t['lifestyle']}**")
        smoker = st.checkbox("Je suis fumeur" if lang == "Français" else "أنا مدخن")
        phys_activity = st.checkbox("Je fais du sport régulièrement" if lang == "Français" else "أمارس الرياضة بانتظام")
        fruits = st.checkbox("Je mange des fruits tous les jours" if lang == "Français" else "آكل الفواكه يوميًا")
        veggies = st.checkbox("Je mange des légumes tous les jours" if lang == "Français" else "آكل الخضروات يوميًا")
        hvy_alcohol = st.checkbox("Je bois beaucoup d'alcool (>14 verres/semaine)" if lang == "Français" else "أشرب الكحول بكثرة (>14 كأس/أسبوع)")

    with col2:
        st.markdown(f"**{t['medical']}**")
        chol_check = st.checkbox("J'ai vérifié mon cholestérol récemment" if lang == "Français" else "فحصت الكوليسترول مؤخرًا")
        any_healthcare = st.checkbox("J'ai une assurance santé" if lang == "Français" else "لدي تأمين صحي")
        no_doc_cost = st.checkbox("Je n'ai pas vu de médecin à cause du coût" if lang == "Français" else "لم أزر الطبيب بسبب التكلفة")

        st.markdown(f"**{t['perceived']}**")
        gen_hlth_text = st.selectbox(t["perceived"], list(GEN_HLTH_MAP.keys()))
        gen_hlth = GEN_HLTH_MAP[gen_hlth_text]

        ment_hlth = st.slider(t["perceived"].split()[0] + " mentale", 0, 30, 0)
        phys_hlth = st.slider(t["perceived"].split()[0] + " physique", 0, 30, 0)

    st.markdown("---")
    st.markdown(f"### {t['profile']}")

    col3, col4 = st.columns(2)

    with col3:
        st.markdown(f"**{t['weight_height']}**")
        weight = st.number_input(t["weight"], min_value=30, max_value=200, value=70, step=1)
        height = st.number_input(t["height"], min_value=100, max_value=220, value=170, step=1)
        bmi = round(weight / ((height / 100) ** 2), 1)
        st.markdown(f"**{t['bmi']} : {bmi}**")

        sex = 1 if st.radio(t["sex"], ["Femme", "Homme"]) == "Homme" else 0

    with col4:
        age_text = st.selectbox(t["age"], list(AGE_MAP.keys()))
        age = AGE_MAP[age_text]
        education_text = st.selectbox(t["education"], list(EDUCATION_MAP.keys()))
        education = EDUCATION_MAP[education_text]
        income_text = st.selectbox(t["income"], list(INCOME_MAP.keys()))
        income = INCOME_MAP[income_text]

    submitted = st.form_submit_button(t["submit"], use_container_width=True)

# === PRÉDICTION ===
if submitted:
    input_data = pd.DataFrame([{
        'HighBP': int(high_bp), 'HighChol': int(high_chol), 'CholCheck': int(chol_check),
        'BMI': bmi, 'Smoker': int(smoker), 'Stroke': int(stroke),
        'HeartDiseaseorAttack': int(heart_disease), 'PhysActivity': int(phys_activity),
        'Fruits': int(fruits), 'Veggies': int(veggies), 'HvyAlcoholConsump': int(hvy_alcohol),
        'AnyHealthcare': int(any_healthcare), 'NoDocbcCost': int(no_doc_cost),
        'GenHlth': gen_hlth, 'MentHlth': ment_hlth, 'PhysHlth': phys_hlth,
        'DiffWalk': int(diff_walk), 'Sex': sex, 'Age': age,
        'Education': education, 'Income': income
    }])

    proba = model.predict_proba(input_data)[0][1] * 100

    # === RÉSULTAT ===
    st.markdown("---")
    st.markdown(f"<h2 style='text-align: center;'>{t['result']}</h2>", unsafe_allow_html=True)

    risk_class = "high-risk" if proba > 80 else "moderate-risk" if proba > 50 else "low-risk"
    risk_text = t["high_risk"] if proba > 80 else t["elevated_risk"] if proba > 50 else t["moderate_risk"] if proba > 30 else t["low_risk"]

    st.markdown(f"""
    <div class="card {risk_class}">
        <h3 style='margin:0; text-align:center;'>{risk_text}</h3>
        <h1 style='margin:10px 0; text-align:center; font-size:3em;'>{proba:.1f}%</h1>
        <p style='text-align:center; opacity:0.9;'>
            {'فحص طبي عاجل' if lang == "العربية" and proba > 80 else 'استشارة طبية فورية' if proba > 80
            else 'متابعة طبية' if proba > 60 else 'انتبه لحياتك' if proba > 40 else 'استمر!' if lang == "العربية" else 'Continuez ainsi !'}
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.progress(proba / 100)

    # === CONSEILS RICHES ===
    st.markdown(f"### {t['advice']}")

    if bmi > 30:
        st.markdown(f"""
        <div class="advice-card" style="background:#feca57;">
            <h4>{t['weight_loss']}</h4>
            <ul>
                <li>{'فقدان 5-10% من الوزن في 6 أشهر' if lang == "العربية" else 'Perdez 5-10% en 6 mois'}</li>
                <li>{'تجنب الحميات القاسية' if lang == "العربية" else 'Évitez les régimes extrêmes'}</li>
                <li>{'استشر أخصائي تغذية' if lang == "العربية" else 'Consultez un nutritionniste'}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    if not phys_activity:
        st.markdown(f"""
        <div class="advice-card" style="background:#54a0ff;">
            <h4>{t['activity']}</h4>
            <ul>
                <li>{'مشي 30 دقيقة يوميًا' if lang == "العربية" else 'Marchez 30 min/jour'}</li>
                <li>{'استخدم السلالم' if lang == "العربية" else 'Prenez les escaliers'}</li>
                <li>{'جرب الدراجة أو السباحة' if lang == "العربية" else 'Essayez vélo ou natation'}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    if gen_hlth > 3:
        st.markdown(f"""
        <div class="advice-card" style="background:#ff6b6b;">
            <h4>{t['checkup']}</h4>
            <ul>
                <li>{'احجز موعدًا مع طبيبك' if lang == "العربية" else 'Prenez RDV avec votre médecin'}</li>
                <li>{'فحص دم شامل' if lang == "العربية" else 'Faites un bilan sanguin'}</li>
                <li>{'تحقق من السكر والضغط' if lang == "العربية" else 'Vérifiez glycémie, tension'}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    if not fruits or not veggies:
        st.markdown(f"""
        <div class="advice-card" style="background:#1dd1a1;">
            <h4>{t['diet']}</h4>
            <ul>
                <li>{'5 فواكه وخضروات يوميًا' if lang == "العربية" else '5 fruits & légumes/jour'}</li>
                <li>{'قلل السكريات' if lang == "العربية" else 'Réduisez les sucres rapides'}</li>
                <li>{'اختر الحبوب الكاملة' if lang == "العربية" else 'Préférez les céréales complètes'}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    if smoker:
        st.markdown(f"""
        <div class="advice-card" style="background:#2d3436;">
            <h4>{t['smoking']}</h4>
            <ul>
                <li>{'اتصل بخدمة مكافحة التدخين' if lang == "العربية" else 'Contactez Tabac Info Service'}</li>
                <li>{'جرب اللاصقات' if lang == "العربية" else 'Essayez les patchs'}</li>
                <li>{'تجنب الأماكن المدخنة' if lang == "العربية" else 'Évitez les lieux enfumés'}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    if proba < 40:
        st.markdown(f"""
        <div class="advice-card" style="background:#48dbfb;">
            <h4>{t['well_done']}</h4>
            <ul>
                <li>{'استمر في عاداتك الجيدة' if lang == "العربية" else 'Continuez vos bonnes habitudes'}</li>
                <li>{'فحص سنوي' if lang == "العربية" else 'Faites un bilan annuel'}</li>
                <li>{'شارك تجربتك' if lang == "العربية" else 'Partagez votre expérience'}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)