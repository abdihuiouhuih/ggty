import streamlit as st

# --- إعدادات الصفحة الأساسية ---
st.set_page_config(page_title="منصة الإنجاز الذكي", layout="wide", initial_sidebar_state="collapsed")

# --- تنسيق CSS متطور لإصلاح الواجهة وجعلها احترافية ---
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
        min-height: 250px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .footer-text { position: fixed; bottom: 10px; left: 15px; color: #539bf5; font-size: 14px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# إدارة التنقل - منع تكرار العناصر
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

def navigate_to(page):
    st.session_state.current_page = page

# حقوق الملكية ثابتة
st.markdown('<div class="footer-text">حقوق التطوير محفوظة لـ عبد الله © 2026</div>', unsafe_allow_html=True)

# --- 1. الشاشة الرئيسية ---
if st.session_state.current_page == 'home':
    st.markdown("<h1 style='text-align: center; color: #ffffff;'>🚀 منصة التطوير الذاتي الشاملة</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #768390;'>استثمر في نفسك عبر تنظيم نشاطك البدني، دراستك، وعاداتك</p>", unsafe_allow_html=True)
    
    st.write("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="card"><h2>🏋️ التحدي الرياضي</h2><p>حساب دقيق للسعرات وتصميم جدول النشاط البدني</p></div>', unsafe_allow_html=True)
        # إضافة key فريد لكل زر لمنع خطأ DuplicateElementId
        if st.button("دخول التحدي الرياضي", key="btn_fit"):
            navigate_to('fitness')
            st.rerun()

    with col2:
        st.markdown('<div class="card"><h2>📚 التحدي الدراسي</h2><p>خطط أكاديمية مخصصة لكل التخصصات الجامعية والمسارات</p></div>', unsafe_allow_html=True)
        if st.button("دخول التحدي الدراسي", key="btn_study"):
            navigate_to('study')
            st.rerun()

    with col3:
        st.markdown('<div class="card"><h2>🚫 تحدي العادات</h2><p>نظام ذكي لكسر العادات السلبية وبناء روتين جديد</p></div>', unsafe_allow_html=True)
        if st.button("دخول تحدي العادات", key="btn_habits"):
            navigate_to('habits')
            st.rerun()

# --- 2. صفحة التحدي الرياضي ---
elif st.session_state.current_page == 'fitness':
    st.title("🏋️ التحدي الرياضي والرشاقة")
    if st.button("⬅️ العودة للرئيسية", key="back_fit"): navigate_to('home'); st.rerun()
    
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

# --- 3. صفحة تحدي ترك العادات ---
elif st.session_state.current_page == 'habits':
    st.title("🚫 تحدي ترك العادات السلبية")
    if st.button("⬅️ العودة للرئيسية", key="back_habits"): navigate_to('home'); st.rerun()
    
    habit = st.text_input("ما هي العادة التي تريد التخلص منها؟")
    c1, c2 = st.columns(2)
    with c1:
        times = st.radio("كم مرة تمارس العادة يومياً؟", ["1-2 مرات", "3-5 مرات", "أكثر من 5"])
    with c2:
        period = st.radio("منذ متى تمارس هذه العادة؟", ["أقل من سنة", "1-3 سنوات", "4-10 سنوات", "أكثر من 10"])
    
    if st.button("✅ ابدأ رحلة التغيير"):
        st.success(f"تم بدء التحدي! تذكر أن الانضباط هو السر وراء كسر القيود القديمة.")

# --- 4. صفحة التحدي الدراسي ---
elif st.session_state.current_page == 'study':
    st.title("📚 التخطيط الدراسي والمسارات")
    if st.button("⬅️ العودة للرئيسية", key="back_study"): navigate_to('home'); st.rerun()
    
    major = st.selectbox("اختر تخصصك أو مجالك الأكاديمي:", 
                        ["هندسة الشبكات", "الأمن السيبراني", "الذكاء الاصطناعي", "علوم الحاسب", 
                         "الطب والجراحة", "هندسة البرمجيات", "إدارة الأعمال", "المحاسبة", 
                         "القانون", "اللغات والترجمة", "ثانوي - مسار علمي", "ثانوي - مسار أدبي"])
    
    level = st.radio("المستوى الدراسي الحالي:", ["مستجد (تأسيس)", "مستوى متوسط", "مستوى متقدم / تخرج"])
    
    study_data = {
        "هندسة الشبكات": {"نصيحة": "ركز على الشهادات المهنية مثل CCNA، والتدريب العملي على Packet Tracer.", "خطة": "تخصيص 60% من وقتك للتطبيق العملي."},
        "الأمن السيبراني": {"نصيحة": "ابدأ بأساسيات Linux وشهادة Security+ وتعلم مهارات اختبار الاختراق.", "خطة": "مراجعة الثغرات الأمنية يومياً."},
        "الذكاء الاصطناعي": {"نصيحة": "إتقان الرياضيات ولغة Python ومكتبات تعلم الآلة مثل TensorFlow.", "خطة": "بناء مشروع تطبيق عملي شهرياً."},
        "علوم الحاسب": {"نصيحة": "التركيز على الخوارزميات وهياكل البيانات كأساس قوي.", "خطة": "حل تحديات برمجية يومياً."},
        "الطب والجراحة": {"نصيحة": "استخدم تقنيات الحفظ المتباعد للمصطلحات والتشخيصات.", "خطة": "المراجعة المستمرة للمادة العلمية والسريرية."},
        "هندسة البرمجيات": {"نصيحة": "تعلم كيفية إدارة المشاريع (Agile) والـ Clean Code.", "خطة": "المشاركة في مشاريع مفتوحة المصدر (Open Source)."},
        "إدارة الأعمال": {"نصيحة": "فهم التحليل المالي وبناء علاقات مهنية قوية.", "خطة": "قراءة دراسة حالة أسبوعية لشركات ناجحة."},
        "المحاسبة": {"نصيحة": "إتقان الـ Excel المتقدم ومعايير المحاسبة الدولية.", "خطة": "التدريب على برامج المحاسبة السحابية."},
        "القانون": {"نصيحة": "تطوير مهارات الصياغة القانونية والبحث القضائي.", "خطة": "تحليل القضايا السابقة وتطوير الملكة القانونية."},
        "اللغات والترجمة": {"نصيحة": "الممارسة اليومية بالاستماع والكتابة والترجمة الفورية.", "خطة": "ترجمة نصوص متنوعة (سياسية، طبية، تقنية)."},
        "ثانوي - مسار علمي": {"نصيحة": "التركيز على الفيزياء والرياضيات كأساس للمستقبل التقني.", "خطة": "توزيع ساعات الدراسة بانتظام لكل مادة."},
        "ثانوي - مسار أدبي": {"نصيحة": "تطوير مهارات التحليل النقدي والكتابة الإبداعية.", "خطة": "فهم العمق التاريخي والأدبي للمواد."}
    }

    st.info(f"💡 نصيحة التخصص: {study_data[major]['نصيحة']}")
    st.success(f"📋 الخطة الدراسية المقترحة: {study_data[major]['خطة']}")
