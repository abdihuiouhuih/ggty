import streamlit as st

# --- إعدادات الصفحة الأساسية ---
st.set_page_config(page_title="تطبيق التحديات الذكي", layout="centered")

# تنسيق الواجهة ليدعم العربية
st.markdown("""
    <style>
    .main { text-align: right; direction: rtl; }
    div[data-testid="stBlock"] { direction: rtl; }
    button { width: 100%; border-radius: 10px; hieght: 50px; }
    </style>
    """, unsafe_allow_html=True)

# --- إدارة التنقل (Navigation) ---
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def change_page(page_name):
    st.session_state.page = page_name

# --- الصفحة الرئيسية ---
if st.session_state.page == 'main':
    st.title("🏆 منصة التحديات اليومية")
    st.subheader("اختر التحدي الذي تريد البدء به:")
    st.write("---")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("🏃 **الرياضة**")
        if st.button("دخول التحدي الرياضي"):
            change_page('fitness')
            st.rerun()

    with col2:
        st.warning("🚫 **العادات**")
        if st.button("دخول تحدي العادات"):
            change_page('habits')
            st.rerun()

    with col3:
        st.success("📚 **الدراسة**")
        if st.button("دخول تحدي الدراسة"):
            change_page('study')
            st.rerun()

# --- صفحة التحدي الرياضي ---
elif st.session_state.page == 'fitness':
    st.title("🏃 تحدي اللياقة البدنية")
    if st.button("⬅️ العودة للرئيسية"):
        change_page('main')
        st.rerun()
    
    st.divider()
    w = st.number_input("الوزن (كجم)", 30, 200, 70)
    h = st.number_input("الطول (سم)", 100, 250, 170)
    age = st.number_input("العمر", 10, 100, 25)
    
    if st.button("احسب احتياجي من السعرات"):
        # حساب تقريبي (Mifflin-St Jeor)
        bmr = (10 * w) + (6.25 * h) - (5 * age) + 5
        st.success(f"سعراتك الأساسية هي: {bmr:.0f} سعرة.")
        st.info(f"لخسارة الوزن، حاول استهلاك {bmr - 500:.0f} سعرة يومياً.")

# --- صفحة ترك العادات ---
elif st.session_state.page == 'habits':
    st.title("🚫 تحدي ترك العادات السيئة")
    if st.button("⬅️ العودة للرئيسية"):
        change_page('main')
        st.rerun()
    
    st.divider()
    habit = st.text_input("ما هي العادة التي تريد الإقلاع عنها؟")
    times = st.number_input("كم مرة تمارسها يومياً؟", 1, 100, 5)
    years = st.number_input("كم سنة صار لك تمارسها؟", 1, 50, 2)
    
    if st.button("تحليل التأثير"):
        total = times * 365 * years
        st.error(f"لقد مارست هذه العادة حوالي {total:,} مرة!")
        st.write("التحدي الآن هو جعل العداد 'صفر' لمدة 21 يوماً متواصلة.")

# --- صفحة تحدي الدراسة ---
elif st.session_state.page == 'study':
    st.title("📚 تحدي التفوق الدراسي")
    if st.button("⬅️ العودة للرئيسية"):
        change_page('main')
        st.rerun()
    
    st.divider()
    major = st.selectbox("المرحلة/التخصص", ["هندسة شبكات", "أمن سيبراني", "برمجة", "أخرى"])
    hours = st.slider("كم ساعة تبي تدرس في اليوم؟", 1, 12, 4)
    
    if st.button("توليد خطة"):
        st.write(f"### خطة لـ {major}:")
        st.success(f"1. ابدأ أول ساعتين في أصعب مادة.\n2. خذ بريك 10 دقائق بعد كل ساعة.\n3. ركز على التطبيق العملي (Labs) إذا كنت تدرس {major}.")
