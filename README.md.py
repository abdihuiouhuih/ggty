import streamlit as st

# 1. إعدادات الصفحة والواجهة
st.set_page_config(page_title="تطبيق التحديات - عبدالله الأحمري", layout="centered")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    stDeployButton {display:none;}
    [data-testid="stStatusWidget"] {display: none;}
    .main { text-align: right; direction: rtl; }
    div[data-testid="stBlock"] { direction: rtl; }
    button { border-radius: 12px; height: 3em; font-weight: bold; width: 100%; }
    .custom-footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        background-color: #f0f2f6; color: #31333F; text-align: center;
        padding: 10px; font-size: 14px; font-weight: bold;
        border-top: 1px solid #e6e9ef; z-index: 999;
    }
    </style>
    """, unsafe_allow_html=True)

def show_copyright():
    st.markdown(f"""<div class="custom-footer">جميع الحقوق محفوظة © 2026 | تطوير المهندس: عبدالله الأحمري 👨‍💻</div>""", unsafe_allow_html=True)

# إدارة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def go_to(page_name):
    st.session_state.page = page_name

# --- الصفحة الرئيسية ---
if st.session_state.page == 'main':
    st.title("🏆 منصة التحديات اليومية")
    st.subheader("اختر مسار التحدي الخاص بك:")
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🏃 تحدي اللياقة"): go_to('fitness'); st.rerun()
    with col2:
        if st.button("🚫 ترك العادات"): go_to('habits'); st.rerun()
    with col3:
        if st.button("📚 التفوق الدراسي"): go_to('study'); st.rerun()

# --- صفحة التحدي الرياضي (المطورة سابقاً) ---
elif st.session_state.page == 'fitness':
    st.title("🏃 المركز الرياضي المتكامل")
    if st.button("⬅️ العودة للرئيسية"): go_to('main'); st.rerun()
    st.divider()
    col_a, col_b = st.columns(2)
    with col_a:
        gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
        weight = st.number_input("الوزن (كجم)", 30.0, 250.0, 80.0)
        height = st.number_input("الطول (سم)", 100, 250, 170)
    with col_b:
        age = st.number_input("العمر", 10, 100, 25)
        activity = st.selectbox("النشاط", ["خامل", "خفيف", "متوسط", "عالٍ"])
        goal = st.selectbox("الهدف", ["خسارة وزن", "محافظة", "بناء عضلات"])
    if st.button("تحليل البيانات"):
        st.info("تم حساب البيانات بناءً على معاييرك الشخصية.")

# --- صفحة ترك العادات (التطوير الجديد) ---
elif st.session_state.page == 'habits':
    st.title("🚫 تحدي الإقلاع عن العادات السيئة")
    if st.button("⬅️ العودة للرئيسية"): go_to('main'); st.rerun()
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        habit_name = st.text_input("ما هي العادة التي تريد تركها؟", placeholder="مثال: التدخين، السهر، إضاعة الوقت")
        daily_cost = st.number_input("التكلفة اليومية التقديرية (ريال)", min_value=0, value=10)
    with col2:
        frequency = st.slider("كم مرة تمارسها يومياً؟", 1, 50, 5)
        years = st.number_input("منذ كم سنة تمارسها؟", 1, 60, 2)

    if st.button("تحليل التأثير وبدء التحدي"):
        st.write("### 📊 تحليل التأثير التراكمي:")
        
        total_times = frequency * 365 * years
        total_money = daily_cost * 365 * years
        
        res1, res2 = st.columns(2)
        res1.metric("مرات الممارسة التقديرية", f"{total_times:,} مرة")
        res2.metric("المبالغ المهدورة (تقريباً)", f"{total_money:,} ريال")
        
        st.warning("⚠️ **تذكر:** الإقلاع يبدأ بقرار اليوم. رحلة التغيير تستغرق عادة 21 يوماً لبناء مسار عصبي جديد في الدماغ.")
        
        st.write("---")
        st.write("### 📅 خطة الـ 21 يوماً القادمة:")
        tabs = st.tabs(["الأسبوع 1", "الأسبوع 2", "الأسبوع 3"])
        with tabs[0]:
            st.info("🚩 **مرحلة المقاومة:** ركز على تغيير بيئتك والابتعاد عن المحفزات.")
        with tabs[1]:
            st.info("🕒 **مرحلة التعود:** سيبدأ عقلك بالتعود على الروتين الجديد، ابحث عن بدائل صحية.")
        with tabs[2]:
            st.info("✅ **مرحلة التثبيت:** أنت الآن قريب من النصر، حافظ على تركيزك.")
        st.balloons()

# --- صفحة تحدي الدراسة ---
elif st.session_state.page == 'study':
    st.title("📚 مركز التخطيط الدراسي")
    if st.button("⬅️ العودة للرئيسية"): go_to('main'); st.rerun()
    major = st.selectbox("المجال", ["هندسة حاسب وأمن سيبراني", "برمجة", "إدارة", "أخرى"])
    if st.button("توليد خطة"): st.success(f"بالتوفيق يا مهندس!")

show_copyright()
