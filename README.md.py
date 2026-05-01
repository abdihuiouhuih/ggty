import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(page_title="منصة عبد الله الاحترافية", layout="wide", initial_sidebar_state="collapsed")

# --- تنسيق CSS متقدم لشاشة احترافية ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div.stButton > button {
        width: 100%;
        border-radius: 15px;
        height: 3em;
        background-color: #1f6aa5;
        color: white;
        border: none;
        transition: 0.3s;
    }
    div.stButton > button:hover { background-color: #2b8ed8; border: 1px solid white; }
    .card {
        padding: 20px;
        border-radius: 15px;
        background-color: #161b22;
        border: 1px solid #30363d;
        text-align: center;
        margin-bottom: 10px;
    }
    footer { visibility: hidden; }
    .rights { position: fixed; bottom: 10px; left: 10px; color: #58a6ff; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# إدارة الحالة (Navigation)
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_to(page_name):
    st.session_state.page = page_name

# حقوق المستخدم
st.markdown('<div class="rights">تم التطوير بواسطة عبد الله © 2026</div>', unsafe_allow_html=True)

# --- 1. الشاشة الرئيسية ---
if st.session_state.page == 'home':
    st.markdown("<h1 style='text-align: center; color: white;'>🚀 مرحباً بك في منصتك الاحترافية يا عبد الله</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #8b949e;'>أدر أهدافك الرياضية والدراسية وعاداتك بكفاءة عالية</p>", unsafe_allow_html=True)
    
    st.write("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="card"><h3>🏋️ تحدي الرياضة</h3><p>احسب سعراتك وخطط لنشاطك البدني</p></div>', unsafe_allow_html=True)
        if st.button("دخول قسم الرياضة"):
            go_to('fitness')
            st.rerun()

    with col2:
        st.markdown('<div class="card"><h3>📚 تحدي الدراسة</h3><p>خطة دراسية مخصصة لتخصصك الأكاديمي</p></div>', unsafe_allow_html=True)
        if st.button("دخول قسم الدراسة"):
            go_to('study')
            st.rerun()

    with col3:
        st.markdown('<div class="card"><h3>🚫 ترك العادات</h3><p>تتبع تقدمك في التخلص من العادات السلبية</p></div>', unsafe_allow_html=True)
        if st.button("دخول قسم العادات"):
            go_to('habits')
            st.rerun()

# --- 2. صفحة تحدي الرياضة ---
elif st.session_state.page == 'fitness':
    st.title("🏋️ قسم الرياضة والرشاقة")
    if st.button("⬅️ العودة للرئيسية"): go_to('home'); st.rerun()
    
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("الوزن الحالي (كجم):", min_value=30.0, value=75.0)
        height = st.number_input("الطول (سم):", min_value=100.0, value=175.0)
        age = st.number_input("العمر:", min_value=10, max_value=100, value=20)
    
    with col2:
        gender = st.radio("الجنس:", ["ذكر", "أنثى"], index=0) # افتراضي ذكر بناءً على طلبك
        activity = st.radio("مستوى النشاط الأسبوعي:", 
                           ["خامل (بدون تمارين)", 
                            "نشاط خفيف (1-2 يوم)", 
                            "نشاط متوسط (3-4 أيام)", 
                            "نشاط مرتفع (5-7 أيام)", 
                            "رياضي محترف (تمارين شاقة)"])

    if st.button("🔥 احسب احتياجي اليومي"):
        # معادلة Mifflin-St Jeor
        s = 5 if gender == "ذكر" else -161
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + s
        
        acts = {"خامل (بدون تمارين)": 1.2, "نشاط خفيف (1-2 يوم)": 1.375, 
                "نشاط متوسط (3-4 أيام)": 1.55, "نشاط مرتفع (5-7 أيام)": 1.725, "رياضي محترف (تمارين شاقة)": 1.9}
        
        total_calories = bmr * acts[activity]
        st.success(f"يا عبد الله، احتياج جسمك للبقاء على نفس الوزن هو: {int(total_calories)} سعرة حرارية.")
        st.info(f"لخسارة الوزن (نقص 0.5 كجم أسبوعياً): {int(total_calories - 500)} سعرة.")

# --- 3. صفحة تحدي ترك العادات ---
elif st.session_state.page == 'habits':
    st.title("🚫 تحدي ترك العادات السلبية")
    if st.button("⬅️ العودة للرئيسية"): go_to('home'); st.rerun()
    
    habit = st.text_input("اسم العادة التي تريد تركها:")
    col1, col2 = st.columns(2)
    with col1:
        times = st.radio("كم مرة تمارسها في اليوم حالياً؟", ["1-3 مرات", "4-7 مرات", "أكثر من ذلك"])
    with col2:
        period = st.radio("منذ متى وأنت تمارس هذه العادة؟", ["أقل من سنة", "1-3 سنوات", "أكثر من 3 سنوات"])
    
    if st.button("🚀 ابدأ خطة التغيير"):
        st.balloons()
        st.success(f"تم تسجيل التحدي لترك {habit}. تذكر أن أول 21 يوماً هي الأصعب، أنت قدها!")

# --- 4. صفحة تحدي الدراسة ---
elif st.session_state.page == 'study':
    st.title("📚 التخطيط الدراسي الذكي")
    if st.button("⬅️ العودة للرئيسية"): go_to('home'); st.rerun()
    
    major = st.selectbox("اختر تخصصك الحالي:", ["هندسة شبكات وأمن سيبراني", "تقنية معلومات", "ثانوي - مسار تقني", "آخر"])
    level = st.radio("مستواك الحالي في التخصص:", ["مبتدئ", "متوسط", "متقدم"])
    
    if major == "هندسة شبكات وأمن سيبراني":
        st.subheader("🛠️ خطة مقترحة لعبد الله (مهندس الشبكات المستقبلي):")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **المسار التقني:**
            - دراسة بروتوكولات IPv4/IPv6 بعمق.
            - التدرب على إعدادات الراوتر والسويتش (Cisco/Juniper).
            - فهم أساسيات الـ Firewall والـ VPN.
            """)
        with col2:
            st.markdown("""
            **الشهادات المقترحة:**
            - شهادة **CCNA** (أساس قوي).
            - شهادة **CompTIA Security+**.
            - البدء في تعلم **Python** لأتمتة الشبكات.
            """)
    
    if st.button("توليد الجدول الدراسي"):
        st.write(f"بناءً على مستواك ({level})، ننصحك بتركيز 60% من وقتك على التطبيق العملي في المختبرات (Labs).")
