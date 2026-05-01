import streamlit as st

# --- إعدادات الصفحة الأساسية ---
st.set_page_config(page_title="منصة الإنجاز الذكي", layout="wide", initial_sidebar_state="collapsed")

# --- تنسيق CSS متطور (Dark Theme) ---
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #adbac7; }
    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 3.8em;
        background-color: #238636;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    div.stButton > button:hover { background-color: #2ea043; transform: scale(1.02); }
    .card {
        padding: 30px;
        border-radius: 20px;
        background-color: #1c2128;
        border: 1px solid #444c56;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .footer-text { position: fixed; bottom: 10px; left: 15px; color: #539bf5; font-size: 14px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# إدارة التنقل
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

def navigate_to(page):
    st.session_state.current_page = page

# حقوق الملكية (عامة)
st.markdown('<div class="footer-text">حقوق التطوير محفوظة لـ عبد الله © 2026</div>', unsafe_allow_html=True)

# --- 1. الشاشة الرئيسية ---
if st.session_state.current_page == 'home':
    st.markdown("<h1 style='text-align: center; color: #ffffff;'>🚀 منصة التطوير الذاتي الشاملة</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #768390;'>استثمر في نفسك عبر تنظيم نشاطك البدني، دراستك، وعاداتك</p>", unsafe_allow_html=True)
    
    st.write("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="card"><h2>🏋️ التحدي الرياضي</h2><p>حساب دقيق للسعرات وتصميم جدول النشاط البدني</p></div>', unsafe_allow_html=True)
        if st.button("دخول التحدي"):
            navigate_to('fitness')
            st.rerun()

    with col2:
        st.markdown('<div class="card"><h2>📚 التحدي الدراسي</h2><p>خطط أكاديمية مخصصة لكل التخصصات الجامعية والمسارات</p></div>', unsafe_allow_html=True)
        if st.button("دخول التحدي"):
            navigate_to('study')
            st.rerun()

    with col3:
        st.markdown('<div class="card"><h2>🚫 تحدي العادات</h2><p>نظام ذكي لكسر العادات السلبية وبناء روتين جديد</p></div>', unsafe_allow_html=True)
        if st.button("دخول التحدي"):
            navigate_to('habits')
            st.rerun()

# --- 2. صفحة التحدي الرياضي ---
elif st.session_state.current_page == 'fitness':
    st.title("🏋️ التحدي الرياضي والرشاقة")
    if st.button("⬅️ العودة للرئيسية"): navigate_to('home'); st.rerun()
    
    st.subheader("📊 حساب السعرات الحرارية والنشاط")
    c1, c2 = st.columns(2)
    with c1:
        weight = st.number_input("الوزن (كجم):", min_value=30.0, value=70.0)
        height = st.number_input("الطول (سم):", min_value=100.0, value=170.0)
        age = st.number_input("العمر:", min_value=10, max_value=90, value=25)
    
    with c2:
        gender = st.radio("الجنس:", ["ذكر", "أنثى"])
        activity = st.radio("مستوى النشاط الأسبوعي:", 
                            ["خامل (لا يوجد تمارين)", 
                             "نشاط خفيف (1-2 يوم)", 
                             "نشاط متوسط (3-4 أيام)", 
                             "نشاط مكثف (5-6 أيام)", 
                             "نشاط رياضي شاق (يومياً)"])

    if st.button("🔥 احسب السعرات الآن"):
        s = 5 if gender == "ذكر" else -161
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + s
        mult = {"خامل (لا يوجد تمارين)": 1.2, "نشاط خفيف (1-2 يوم)": 1.375, "نشاط متوسط (3-4 أيام)": 1.55, "نشاط مكثف (5-6 أيام)": 1.725, "نشاط رياضي شاق (يومياً)": 1.9}
        total = bmr * mult[activity]
        
        st.success(f"احتياجك اليومي للمحافظة على الوزن: {int(total)} سعرة حرارية.")
        st.info(f"لخسارة الوزن: {int(total - 500)} سعرة | لزيادة الوزن: {int(total + 500)} سعرة.")

# --- 3. صفحة تحدي ترك العادات ---
elif st.session_state.current_page == 'habits':
    st.title("🚫 تحدي ترك العادات السلبية")
    if st.button("⬅️ العودة للرئيسية"): navigate_to('home'); st.rerun()
    
    habit = st.text_input("ما هي العادة التي تريد التخلص منها؟")
    c1, c2 = st.columns(2)
    with c1:
        times = st.radio("معدل ممارستك للعادة حالياً:", ["يومي بشكل متكرر", "مرة يومياً", "أحياناً خلال الأسبوع"])
    with c2:
        period = st.radio("منذ متى تمارس هذه العادة؟", ["أقل من سنة", "1-3 سنوات", "4-10 سنوات", "أكثر من 10 سنوات"])
    
    if st.button("✅ ابدأ رحلة التغيير"):
        st.success(f"تم بدء التحدي! تذكر أن الانضباط هو السر وراء كسر القيود القديمة.")

# --- 4. صفحة التحدي الدراسي ---
elif st.session_state.current_page == 'study':
    st.title("📚 التخطيط الدراسي والمسارات")
    if st.button("⬅️ العودة للرئيسية"): navigate_to('home'); st.rerun()
    
    major = st.selectbox("اختر تخصصك أو مجالك الأكاديمي:", 
                        ["هندسة الشبكات", "الأمن السيبراني", "الذكاء الاصطناعي", "علوم الحاسب", 
                         "الطب والجراحة", "هندسة البرمجيات", "إدارة الأعمال", "المحاسبة", 
                         "القانون", "اللغات والترجمة", "ثانوي - مسار علمي", "ثانوي - مسار أدبي"])
    
    level = st.radio("المستوى الدراسي الحالي:", ["مستجد (تأسيس)", "مستوى متوسط", "مستوى متقدم / تخرج"])
    
    # تفاصيل الخطط والنصائح لكل تخصص
    study_data = {
        "هندسة الشبكات": {"نصيحة": "ركز على الشهادات المهنية مثل CCNA و CCNP، والتدريب العملي على الأجهزة الحقيقية أو Packet Tracer.", "خطة": "تخصيص 40% نظري و 60% تطبيق عملي على البروتوكولات."},
        "الأمن السيبراني": {"نصيحة": "ابدأ بأساسيات الشبكات ثم انتقل لتعلم اختبار الاختراق الأخلاقي وشهادة Security+.", "خطة": "دراسة أنظمة Linux والتعامل مع الثغرات البرمجية بشكل أسبوعي."},
        "الذكاء الاصطناعي": {"نصيحة": "تقوية مهارات الرياضيات (الجبر الخطي والاحتمالات) وإتقان لغة Python ومكتباتها.", "خطة": "بناء مشروع صغير شهرياً لتطبيق نماذج Machine Learning."},
        "علوم الحاسب": {"نصيحة": "الخوارزميات وهياكل البيانات هي مفتاحك للشركات الكبرى؛ لا تتجاهل الأساسيات النظري.", "خطة": "حل تحديات برمجية يومية (LeetCode) لمدة ساعة."},
        "الطب والجراحة": {"نصيحة": "التكرار المتباعد (Spaced Repetition) هو أفضل وسيلة لحفظ المصطلحات والتشخيصات.", "خطة": "استخدام تطبيقات مثل Anki للحفظ والمراجعة السريرية المستمرة."},
        "هندسة البرمجيات": {"نصيحة": "اهتم بـ Clean Code وكيفية إدارة المشاريع البرمجية (Agile).", "خطة": "تعلم Git/GitHub والعمل الجماعي على مشاريع مفتوحة المصدر."},
        "إدارة الأعمال": {"نصيحة": "بناء شبكة علاقات قوية وفهم لغة الأرقام والبيانات المالية.", "خطة": "قراءة دراسة حالة (Case Study) عالمية كل أسبوع."},
        "المحاسبة": {"نصيحة": "الدقة هي كل شيء؛ تعلم استخدام Excel بمستوى متقدم ومعايير المحاسبة الدولية (IFRS).", "خطة": "مراجعة القيود المحاسبية والقوائم المالية بشكل دوري."},
        "القانون": {"نصيحة": "ركز على مهارات التحليل والاستنباط القانوني وقوة الصياغة.", "خطة": "قراءة الأحكام القضائية السابقة لتطوير الملكة القانونية."},
        "اللغات والترجمة": {"نصيحة": "الاستماع والممارسة اليومية أهم من دراسة القواعد فقط.", "خطة": "تخصيص وقت للترجمة الفورية والكتابية لنصوص متنوعة."},
        "ثانوي - مسار علمي": {"نصيحة": "التركيز على مواد الفيزياء والرياضيات كأساس للمجالات التقنية والطبية.", "خطة": "توزيع ساعات الدراسة لتغطية كافة المواد مع حل اختبارات سابقة."},
        "ثانوي - مسار أدبي": {"نصيحة": "تطوير مهارات الحفظ والفهم العميق للتاريخ والأدب والعلوم الإنسانية.", "خطة": "تحسين مهارات الكتابة الإبداعية والتحليل النقدي."}
    }

    st.markdown(f"### 💡 نصيحة التخصص:")
    st.info(study_data[major]["نصيحة"])
    
    st.markdown(f"### 📋 الخطة الدراسية المقترحة:")
    st.success(study_data[major]["خطة"])

    if st.button("اعتماد هذه الخطة"):
        st.toast("تم حفظ مسارك الدراسي بنجاح!")
