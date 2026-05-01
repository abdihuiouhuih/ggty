import streamlit as st

# 1. إعدادات الصفحة والهوية البصرية
st.set_page_config(page_title="منصة عبدالله الأحمري للتحديات", layout="wide")

st.markdown("""
    <style>
    /* إخفاء عناصر المطور */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stStatusWidget"] {display: none;}
    
    /* تنسيق الخطوط والمحتوى */
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    
    /* ستايل البطاقات في الشاشة الرئيسية */
    .main-card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        transition: 0.3s;
        border: 1px solid #eee;
        margin-bottom: 20px;
        color: #1E1E1E;
    }
    .main-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        border-color: #4CAF50;
    }
    
    /* تنسيق الفوتر الثابت (الحقوق) */
    .footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        background-color: #0e1117; color: white; text-align: center;
        padding: 15px; font-weight: bold; z-index: 1000;
        border-top: 3px solid #4CAF50;
    }
    
    /* تنسيق خاص للأزرار */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3em;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# دالة الحقوق الثابتة
def show_footer():
    st.markdown('<div class="footer">جميع الحقوق محفوظة © 2026 | تطوير المهندس: عبدالله الأحمري 👨‍💻</div>', unsafe_allow_html=True)

# إدارة التنقل بين الغرف
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def navigate(target):
    st.session_state.page = target

# --- 1. الشاشة الرئيسية الاحترافية ---
if st.session_state.page == 'home':
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏆 منصة الإنجاز اليومي</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2em;'>صمم طريقك للنجاح مع أدواتنا المتكاملة</p>", unsafe_allow_html=True)
    st.write("---")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="main-card"><h2>🏃‍♂️</h2><h3>المركز الرياضي</h3><p>تحليل الجسم، السعرات، وتتبع النشاط</p></div>', unsafe_allow_html=True)
        if st.button("دخول المختبر الرياضي"): navigate('fitness'); st.rerun()

    with col2:
        st.markdown('<div class="main-card"><h2>🚫</h2><h3>رادار العادات</h3><p>تحليل مالي ونفسي للتخلص من العادات</p></div>', unsafe_allow_html=True)
        if st.button("بدء رحلة التغيير"): navigate('habits'); st.rerun()

    with col3:
        st.markdown('<div class="main-card"><h2>📚</h2><h3>التخطيط الدراسي</h3><p>أدوات مخصصة لهندسة الحاسب والتقنية</p></div>', unsafe_allow_html=True)
        if st.button("تجهيز الجدول الدراسي"): navigate('study'); st.rerun()

# --- 2. غرفة الرياضة (محدثة بالكامل) ---
elif st.session_state.page == 'fitness':
    st.title("🏃‍♂️ المختبر الرياضي المتكامل")
    if st.button("🏠 العودة للرئيسية"): navigate('home'); st.rerun()
    st.divider()

    col_a, col_b = st.columns([1, 1.2])
    with col_a:
        st.subheader("📋 المدخلات")
        gender = st.radio("الجنس", ["ذكر", "أنثى"], horizontal=True)
        weight = st.number_input("الوزن الحالي (كجم)", 40.0, 200.0, 80.0)
        height = st.number_input("الطول (سم)", 120, 230, 175)
        age = st.number_input("العمر", 15, 90, 22)
        
        st.write("**مستوى النشاط الأسبوعي:**")
        activity = st.radio(
            "اختر مستواك بدقة:",
            ["خامل (لا يوجد تمارين)", 
             "خفيف (تمارين 1-3 أيام)", 
             "متوسط (تمارين 3-5 أيام)", 
             "نشط جداً (تمارين يومية مكثفة)"]
        )

    with col_b:
        st.subheader("📊 نتائج التحليل")
        # حسابات Mifflin-St Jeor
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + (5 if gender == "ذكر" else -161)
        factors = {"خامل (لا يوجد تمارين)": 1.2, "خفيف (تمارين 1-3 أيام)": 1.375, 
                   "متوسط (تمارين 3-5 أيام)": 1.55, "نشط جداً (تمارين يومية مكثفة)": 1.725}
        maintenance = bmr * factors[activity]
        bmi = weight / ((height/100)**2)
        
        r1, r2 = st.columns(2)
        r1.metric("مؤشر كتلة الجسم BMI", f"{bmi:.1f}")
        r2.metric("سعرات المحافظة", f"{int(maintenance)} سعرة")
        
        st.write("---")
        goal = st.selectbox("هدفك الحالي", ["خسارة وزن", "بناء عضلات", "محافظة"])
        if goal == "خسارة وزن":
            st.warning(f"لتحقيق هدفك، ينصح بتناول {int(maintenance - 500)} سعرة يومياً.")
        elif goal == "بناء عضلات":
            st.success(f"لتحقيق هدفك، ينصح بتناول {int(maintenance + 300)} سعرة يومياً مع زيادة البروتين.")

# --- 3. غرفة العادات (محدثة بالكامل) ---
elif st.session_state.page == 'habits':
    st.title("🚫 رادار ترك العادات السيئة")
    if st.button("🏠 العودة للرئيسية"): navigate('home'); st.rerun()
    st.divider()

    h_col1, h_col2 = st.columns(2)
    with h_col1:
        habit_name = st.text_input("ما هي العادة التي تريد تركها؟", "التدخين")
        daily_cost = st.number_input("التكلفة المالية اليومية (ريال)", 0, 1000, 25)
        frequency = st.slider("كم مرة تمارسها يومياً؟", 1, 50, 10)
    with h_col2:
        duration_years = st.number_input("منذ كم سنة تمارسها؟", 1, 50, 5)
        impact = st.multiselect("ما هي جوانب الضرر؟", ["صحي", "مالي", "نفسي", "اجتماعي"])

    if st.button("تحليل التأثير وبدء التحدي"):
        total_money = daily_cost * 365 * duration_years
        total_times = frequency * 365 * duration_years
        
        st.write("### 📊 تقرير الخسائر التراكمي:")
        c1, c2 = st.columns(2)
        c1.metric("أموال مهدورة", f"{total_money:,} ريال")
        c2.metric("مرات الممارسة", f"{total_times:,} مرة")
        
        st.error(f"تخيل يا عبدالله، هذا المبلغ ({total_money:,} ريال) كان كافياً لشراء أحدث أجهزة الشبكات أو تطوير معملك الخاص!")
        st.balloons()

# --- 4. غرفة الدراسة (مخصصة للهندسة والتقنية) ---
elif st.session_state.page == 'study':
    st.title("📚 التميز الدراسي والأكاديمي")
    if st.button("🏠 العودة للرئيسية"): navigate('home'); st.rerun()
    st.divider()

    st.subheader("🛠️ أدوات طالب الهندسة")
    major = st.selectbox("التخصص الدراسي", ["هندسة الشبكات", "الأمن السيبراني", "تطوير البرمجيات", "أخرى"])
    
    s1, s2 = st.columns(2)
    with s1:
        study_hours = st.slider("ساعات المذاكرة المتاحة اليوم", 1, 12, 4)
        has_lab = st.checkbox("هل لديك تطبيق عملي (Labs) اليوم؟")
    with s2:
        exam_soon = st.radio("هل لديك اختبار قريب؟", ["لا يوجد حالياً", "خلال أيام", "غداً!"])

    if st.button("توليد الخطة الذكية"):
        st.success(f"خطة مقترحة لتخصص {major}:")
        if has_lab:
            st.info(f"خصص {study_hours * 0.6:.1f} ساعة للتطبيق العملي على Packet Tracer أو المختبرات.")
            st.info(f"خصص {study_hours * 0.4:.1f} ساعة للمراجعة النظرية.")
        else:
            st.info(f"خصص كامل الوقت ({study_hours} ساعة) لمراجعة المفاهيم وحل المسائل.")
        
        if exam_soon != "لا يوجد حالياً":
            st.warning("⚠️ ركز على النماذج السابقة والمفاهيم الأساسية أولاً.")

show_footer()
