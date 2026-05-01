import streamlit as st

# --- إعدادات الصفحة الأساسية ---
st.set_page_config(page_title="منصة عبد الله الاحترافية", layout="wide", initial_sidebar_state="collapsed")

# --- تنسيق CSS لجعل الواجهة احترافية وتناسب جهاز Xiaomi Pad 7 ---
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #adbac7; }
    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background-color: #238636;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    div.stButton > button:hover { background-color: #2ea043; border: 1px solid #ffffff; }
    .card {
        padding: 25px;
        border-radius: 15px;
        background-color: #1c2128;
        border: 1px solid #444c56;
        text-align: center;
        margin-bottom: 15px;
        min-height: 200px;
    }
    .footer-text { position: fixed; bottom: 10px; left: 15px; color: #539bf5; font-size: 14px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# إدارة التنقل بين الصفحات
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

def navigate_to(page):
    st.session_state.current_page = page

# حقوق الملكية ثابتة في كل الصفحات
st.markdown(f'<div class="footer-text">حقوق التطوير محفوظة لـ عبد الله © 2026</div>', unsafe_allow_html=True)

# --- 1. الشاشة الرئيسية ---
if st.session_state.current_page == 'home':
    st.markdown("<h1 style='text-align: center; color: #adbac7;'>🚀 منصة الإنجاز المتكاملة</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #768390;'>مرحباً يا عبد الله، اختر وجهتك اليوم للبدء في التحدي</p>", unsafe_allow_html=True)
    
    st.write("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="card"><h2>🏋️ تحدي الرياضة</h2><p>حساب السعرات الدقيقة وتخطيط النشاط البدني اليومي</p></div>', unsafe_allow_html=True)
        if st.button("دخول تحدي الرياضة"):
            navigate_to('fitness')
            st.rerun()

    with col2:
        st.markdown('<div class="card"><h2>📚 تحدي الدراسة</h2><p>خطة أكاديمية مخصصة لجميع التخصصات الجامعية</p></div>', unsafe_allow_html=True)
        if st.button("دخول تحدي الدراسة"):
            navigate_to('study')
            st.rerun()

    with col3:
        st.markdown('<div class="card"><h2>🚫 ترك العادات</h2><p>نظام ذكي لتتبع التخلص من السلوكيات السلبية</p></div>', unsafe_allow_html=True)
        if st.button("دخول تحدي العادات"):
            navigate_to('habits')
            st.rerun()

# --- 2. صفحة تحدي الرياضة ---
elif st.session_state.current_page == 'fitness':
    st.title("🏋️ تحدي الرشاقة والنشاط البدني")
    if st.button("⬅️ العودة للرئيسية"): navigate_to('home'); st.rerun()
    
    with st.container():
        st.subheader("📊 حاسبة السعرات الاحترافية")
        c1, c2 = st.columns(2)
        with c1:
            weight = st.number_input("الوزن (كجم):", min_value=30.0, value=75.0)
            height = st.number_input("الطول (سم):", min_value=100.0, value=175.0)
        with c2:
            age = st.number_input("العمر:", min_value=10, max_value=90, value=22)
            activity = st.radio("مستوى النشاط الأسبوعي:", 
                                  ["خامل جداً (لا رياضة)", "نشاط خفيف (مرة/أسبوع)", "نشاط متوسط (3 مرات/أسبوع)", "نشاط عالي (5 مرات/أسبوع)", "رياضي محترف"])
    
    if st.button("🔥 استخراج النتائج"):
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        acts = {"خامل جداً (لا رياضة)": 1.2, "نشاط خفيف (مرة/أسبوع)": 1.375, "نشاط متوسط (3 مرات/أسبوع)": 1.55, "نشاط عالي (5 مرات/أسبوع)": 1.725, "رياضي محترف": 1.9}
        tdee = bmr * acts[activity]
        
        st.success(f"يا عبد الله، احتياج جسمك اليومي هو {int(tdee)} سعرة حرارية.")
        st.info(f"للتنشيف (خسارة وزن): {int(tdee - 500)} سعرة | للتضخيم (زيادة عضل): {int(tdee + 400)} سعرة.")

# --- 3. صفحة تحدي ترك العادات ---
elif st.session_state.current_page == 'habits':
    st.title("🚫 تحدي ترك العادات")
    if st.button("⬅️ العودة للرئيسية"): navigate_to('home'); st.rerun()
    
    habit_title = st.text_input("ما هي العادة التي قررت تركها؟")
    c1, c2 = st.columns(2)
    with c1:
        daily_freq = st.radio("كم مرة تكرر العادة يومياً؟", ["مرة واحدة", "2-4 مرات", "أكثر من 5 مرات"])
    with c2:
        years_active = st.radio("منذ كم سنة بدأت هذه العادة؟", ["أقل من سنة", "سنة إلى 3 سنوات", "أكثر من 3 سنوات"])
    
    if st.button("✅ ابدأ التحدي الآن"):
        st.balloons()
        st.warning(f"تم بدء التحدي! تذكر يا عبد الله أن الانضباط هو مفتاح النجاح لترك {habit_title}.")

# --- 4. صفحة تحدي الدراسة ---
elif st.session_state.current_page == 'study':
    st.title("📚 التخطيط الدراسي التخصصي")
    if st.button("⬅️ العودة للرئيسية"): navigate_to('home'); st.rerun()
    
    st.subheader("📍 تحديد المسار الأكاديمي")
    major = st.selectbox("اختر تخصصك الجامعي:", 
                        ["هندسة الشبكات", "الأمن السيبراني", "تقنية المعلومات", "هندسة البرمجيات", "علوم الحاسب", "الذكاء الاصطناعي", "هندسة كهربائية", "هندسة ميكانيكية", "الطب البشري", "إدارة أعمال", "الحقوق"])
    
    level = st.radio("مستواك الحالي:", ["مبتدئ (سنة أولى)", "متوسط (سنوات التخصص)", "خريج (تطبيق احترافي)"])
    
    plans = {
        "هندسة الشبكات": "ركز على شهادة CCNA والتدرب على برامج المحاكاة مثل Packet Tracer لضبط الـ Routers والـ Switches.",
        "الأمن السيبراني": "اهتم بأساسيات Linux وشهادة Security+ وتعلم مهارات اختبار الاختراق الأخلاقي.",
        "تقنية المعلومات": "عزز مهاراتك في إدارة قواعد البيانات وصيانة الأنظمة والدعم الفني التقني.",
        "هندسة البرمجيات": "ركز على دورة حياة بناء البرمجيات وأنماط التصميم (Design Patterns) ولغات البرمجة الحديثة.",
        "علوم الحاسب": "اهتم بالخوارزميات وهياكل البيانات والذكاء الاصطناعي والرياضيات المتقدمة.",
        "الذكاء الاصطناعي": "تعلم مكتبات Python مثل TensorFlow و Scikit-Learn وركز على تعلم الآلة.",
        "هندسة كهربائية": "ركز على الدوائر الإلكترونية، أنظمة الطاقة، والتحكم الرقمي.",
        "هندسة ميكانيكية": "اهتم بالتصميم بمساعدة الحاسوب (CAD) والديناميكا الحرارية والميكانيكا الحيوية.",
        "الطب البشري": "ركز على التشريح، علم وظائف الأعضاء، والممارسة السريرية المستمرة.",
        "إدارة أعمال": "نمِّ مهارات القيادة، التخطيط الاستراتيجي، والتحليل المالي.",
        "الحقوق": "ركز على مهارات المرافعة، صياغة العقود، وفهم القوانين المحلية والدولية."
    }

    st.markdown(f"### 💡 نصيحة مخصصة لتخصصك ({major}):")
    st.info(plans.get(major, "استمر في المثابرة والاطلاع على أحدث المستجدات في مجالك."))

    if st.button("📋 اعتماد الخطة الدراسية"):
        st.success(f"تم اعتماد خطة دراسية مخصصة لعبد الله في تخصص {major}. ابدأ بالتركيز على الجوانب التطبيقية أولاً!")
