import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="تطبيق التحديات - عبدالله الأحمري", layout="centered")

# تنسيق الواجهة وإخفاء أدوات المطور
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

# وظيفة عرض الحقوق
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
        st.info("🏃 **الرياضة**")
        if st.button("تحدي اللياقة"): go_to('fitness'); st.rerun()
    with col2:
        st.warning("🚫 **العادات**")
        if st.button("ترك العادات"): go_to('habits'); st.rerun()
    with col3:
        st.success("📚 **الدراسة**")
        if st.button("التفوق الدراسي"): go_to('study'); st.rerun()

# --- صفحة التحدي الرياضي المطور ---
elif st.session_state.page == 'fitness':
    st.title("🏃 المركز الرياضي المتكامل")
    if st.button("⬅️ العودة للرئيسية"):
        go_to('main'); st.rerun()
    
    st.divider()
    
    col_a, col_b = st.columns(2)
    with col_a:
        gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
        weight = st.number_input("الوزن الحالي (كجم)", 30.0, 250.0, 80.0)
        height = st.number_input("الطول (سم)", 100, 250, 170)
    with col_b:
        age = st.number_input("العمر", 10, 100, 25)
        activity = st.selectbox("مستوى النشاط البدني", [
            "خامل (بدون تمارين)", 
            "نشاط خفيف (1-3 أيام/أسبوع)", 
            "نشاط متوسط (3-5 أيام/أسبوع)", 
            "نشاط عالٍ (6-7 أيام/أسبوع)"
        ])
        goal = st.selectbox("هدفك الحالي", ["خسارة وزن", "محافظة", "بناء عضلات"])

    if st.button("تحليل البيانات البدنية"):
        # حساب BMR (معادلة ميفلين)
        if gender == "ذكر":
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        else:
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
        
        # معامل النشاط
        factors = {"خامل (بدون تمارين)": 1.2, "نشاط خفيف (1-3 أيام/أسبوع)": 1.375, 
                   "نشاط متوسط (3-5 أيام/أسبوع)": 1.55, "نشاط عالٍ (6-7 أيام/أسبوع)": 1.725}
        maintenance = bmr * factors[activity]
        
        # حساب BMI
        bmi = weight / ((height/100)**2)
        
        st.write("---")
        res1, res2, res3 = st.columns(3)
        res1.metric("كتلة الجسم (BMI)", f"{bmi:.1f}")
        res2.metric("سعرات المحافظة", f"{maintenance:.0f}")
        
        if goal == "خسارة وزن":
            target = maintenance - 500
            res3.metric("السعرات المستهدفة", f"{target:.0f}")
            st.success(f"💡 للوصول لهدفك، تحتاج لتناول {target:.0f} سعرة يومياً. ستفقد حوالي 0.5 كجم أسبوعياً.")
        elif goal == "بناء عضلات":
            target = maintenance + 300
            res3.metric("السعرات المستهدفة", f"{target:.0f}")
            st.info(f"💡 لزيادة الكتلة العضلية، استهدف {target:.0f} سعرة مع التركيز على البروتين.")
        else:
            res3.metric("السعرات المستهدفة", f"{maintenance:.0f}")

# --- صفحة ترك العادات ---
elif st.session_state.page == 'habits':
    st.title("🚫 تحدي ترك العادات السيئة")
    if st.button("⬅️ العودة للرئيسية"): go_to('main'); st.rerun()
    habit = st.text_input("اسم العادة")
    if st.button("بدء التحدي"): st.write("استمر لـ 21 يوماً لتغيير حياتك!")

# --- صفحة تحدي الدراسة ---
elif st.session_state.page == 'study':
    st.title("📚 مركز التخطيط الدراسي")
    if st.button("⬅️ العودة للرئيسية"): go_to('main'); st.rerun()
    major = st.text_input("التخصص")
    if st.button("توليد خطة"): st.success(f"بالتوفيق يا مهندس {major}!")

show_copyright()
