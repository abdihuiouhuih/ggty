import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="تطبيق التحديات - عبدالله الأحمري", layout="centered")

# تنسيق الواجهة ودعم العربية مع إضافة ستايل للحقوق في الأسفل
st.markdown("""
    <style>
    .main { text-align: right; direction: rtl; }
    div[data-testid="stBlock"] { direction: rtl; }
    button { border-radius: 12px; height: 3em; font-weight: bold; }
    
    /* ستايل الحقوق */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f0f2f6;
        color: #31333F;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        font-weight: bold;
        border-top: 1px solid #e6e9ef;
        z-index: 999;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. وظيفة عرض الحقوق (تظهر في كل الصفحات)
def show_copyright():
    st.markdown(f"""
        <div class="footer">
            جميع الحقوق محفوظة © 2026 | تطوير: عبدالله الأحمري 👨‍💻
        </div>
        """, unsafe_allow_html=True)

# 3. إدارة التنقل بين الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def go_to(page_name):
    st.session_state.page = page_name

# --- الصفحة الرئيسية ---
if st.session_state.page == 'main':
    st.title("🏆 منصة التحديات اليومية")
    st.subheader("اختر التحدي للذهاب لصفحته الخاصة:")
    st.divider()

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("🏃 **الرياضة**")
        if st.button("فتح تحدي الرياضة"):
            go_to('fitness')
            st.rerun()

    with col2:
        st.warning("🚫 **العادات**")
        if st.button("فتح تحدي العادات"):
            go_to('habits')
            st.rerun()

    with col3:
        st.success("📚 **الدراسة**")
        if st.button("فتح تحدي الدراسة"):
            go_to('study')
            st.rerun()

# --- صفحة التحدي الرياضي ---
elif st.session_state.page == 'fitness':
    st.title("🏃 تحدي اللياقة البدنية")
    if st.button("⬅️ العودة للرئيسية"):
        go_to('main')
        st.rerun()
    
    st.divider()
    w = st.number_input("الوزن (كجم)", 30, 200, 70)
    h = st.number_input("الطول (سم)", 100, 250, 170)
    age = st.number_input("العمر", 10, 100, 25)
    
    if st.button("احسب احتياجي من السعرات"):
        bmr = (10 * w) + (6.25 * h) - (5 * age) + 5
        st.success(f"سعراتك الأساسية هي: {bmr:.0f} سعرة.")

# --- صفحة ترك العادات ---
elif st.session_state.page == 'habits':
    st.title("🚫 تحدي ترك العادات السيئة")
    if st.button("⬅️ العودة للرئيسية"):
        go_to('main')
        st.rerun()
    
    st.divider()
    habit = st.text_input("ما هي العادة التي تريد الإقلاع عنها؟")
    times = st.number_input("كم مرة تمارسها يومياً؟", 1, 100, 5)
    years = st.number_input("كم سنة صار لك تمارسها؟", 1, 50, 2)
    
    if st.button("تحليل التأثير"):
        total = times * 365 * years
        st.error(f"لقد مارست هذه العادة حوالي {total:,} مرة!")

# --- صفحة تحدي الدراسة ---
elif st.session_state.page == 'study':
    st.title("📚 مركز التخطيط الدراسي")
    if st.button("⬅️ العودة للرئيسية"):
        go_to('main')
        st.rerun()
    
    st.divider()
    category = st.selectbox("اختر مجال دراستك:", [
        "هندسة الحاسب والأمن السيبراني", 
        "تطوير البرمجيات والذكاء الاصطناعي", 
        "العلوم الإدارية والمالية", 
        "تخصصات أخرى"
    ])
    
    sub = st.text_input("اكتب تخصصك الدقيق:")
    hours = st.slider("ساعات الدراسة اليومية:", 1, 12, 4)

    if st.button("توليد خطة الدراسة"):
        st.write(f"### 📋 خطة الـ {hours} ساعات لتخصص {sub}:")
        st.success(f"• ركز أول {hours*0.6:.1f} ساعة على المهام الصعبة والعملية.")
        st.info(f"• خصص الوقت المتبقي للمراجعة والتلخيص.")
        st.balloons()

# عرض الحقوق في أسفل كل صفحة
show_copyright()
