import streamlit as st

# 1. إعدادات الهوية البصرية والتنسيق الاحترافي (CSS)
st.set_page_config(page_title="منصة عبد الله للتحديات", layout="wide")

st.markdown("""
    <style>
    /* إخفاء عناصر المطور */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stStatusWidget"] {display: none;}
    
    /* تنسيق الخطوط والمحتوى العربي */
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    
    /* ستايل البطاقات الاحترافية في الشاشة الرئيسية */
    .feature-card {
        background-color: #1e2130;
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
        text-align: center;
        transition: 0.4s;
        border: 1px solid #3d4156;
        margin-bottom: 20px;
    }
    .feature-card:hover {
        transform: translateY(-10px);
        border-color: #4CAF50;
    }

    /* الفوتر المحدث (حقوق عبد الله) */
    .custom-footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        background-color: #0e1117; color: #4CAF50; text-align: center;
        padding: 12px; font-weight: bold; z-index: 1000;
        border-top: 2px solid #4CAF50;
    }
    
    /* تنسيق الأزرار */
    .stButton>button {
        width: 100%; border-radius: 15px; height: 3.5em; font-weight: bold;
        background-color: #4CAF50; color: white; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

def show_footer():
    # تعديل الحقوق بناءً على طلبك (حذف 2026 والمهندس)
    st.markdown('<div class="custom-footer">جميع الحقوق محفوظة © | تطوير: عبد الله الأحمري 👨‍💻</div>', unsafe_allow_html=True)

# إدارة التنقل بين الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav_to(page):
    st.session_state.page = page

# --- الشاشة الرئيسية ---
if st.session_state.page == 'main':
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏆 منصة الإنجاز اليومي</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2em;'>صمم طريقك للنجاح مع أدواتنا المتكاملة</p>", unsafe_allow_html=True)
    st.write("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="feature-card"><h2>🔥</h2><h3>تحدي اللياقة</h3><p>حساب السعرات والاحتياج اليومي لجسمك</p></div>', unsafe_allow_html=True)
        if st.button("دخول القسم الرياضي"): nav_to('fit'); st.rerun()
    with col2:
        st.markdown('<div class="feature-card"><h2>🚫</h2><h3>تحدي العادات</h3><p>تحليل الأثر الزمني والمالي لترك العادات</p></div>', unsafe_allow_html=True)
        if st.button("بدء رحلة الإقلاع"): nav_to('habit'); st.rerun()
    with col3:
        st.markdown('<div class="feature-card"><h2>📖</h2><h3>تحدي الدراسة</h3><p>خطط دراسية مخصصة حسب تخصصك الجامعي</p></div>', unsafe_allow_html=True)
        if st.button("تخطيط دراستك"): nav_to('study'); st.rerun()

# --- صفحة الرياضة (حساب السعرات والنشاط) ---
elif st.session_state.page == 'fit':
    st.title("🏋️ المختبر الرياضي الذكي")
    if st.button("🏠 العودة للرئيسية"): nav_to('main'); st.rerun()
    st.divider()

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📋 البيانات الشخصية")
        weight = st.number_input("الوزن (كجم)", 40, 200, 80)
        height = st.number_input("الطول (سم)", 120, 230, 175)
        age = st.number_input("العمر", 15, 90, 25)
        gender = st.radio("الجنس", ["ذكر", "أنثى"], horizontal=True)
    with c2:
        st.subheader("⚡ مستوى النشاط والهدف")
        activity = st.select_slider("مستوى النشاط الأسبوعي:", 
                                    options=["خامل", "خفيف", "متوسط", "نشط جداً"])
        goal = st.selectbox("ما هو هدفك الحالي؟", ["خسارة وزن", "محافظة", "بناء عضلات"])

    if st.button("تحليل الاحتياج اليومي"):
        # حساب السعرات الأساسية (Mifflin-St Jeor)
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + (5 if gender == "ذكر" else -161)
        factor = {"خامل": 1.2, "خفيف": 1.375, "متوسط": 1.55, "نشط جداً": 1.725}[activity]
        maint = bmr * factor
        
        st.write("---")
        res1, res2 = st.columns(2)
        res1.metric("سعرات المحافظة", f"{int(maint)} سعرة")
        if goal == "خسارة وزن": target = maint - 500
        elif goal == "بناء عضلات": target = maint + 300
        else: target = maint
        res2.metric("السعرات المستهدفة للهدف", f"{int(target)} سعرة")
        st.success(f"يا عبد الله، للوصول لهدفك ({goal}) تحتاج لتناول {int(target)} سعرة يومياً.")

# --- صفحة العادات (تحليل الأثر التراكمي) ---
elif st.session_state.page == 'habit':
    st.title("🚫 رادار ترك العادات")
    if st.button("🏠 العودة للرئيسية"): nav_to('main'); st.rerun()
    st.divider()

    col_h1, col_h2 = st.columns(2)
    with col_h1:
        habit_name = st.text_input("ما هي العادة التي تريد تركها؟")
        h_freq = st.number_input("كم مرة تمارسها يومياً؟", 1, 100, 5)
    with col_h2:
        h_years = st.number_input("منذ كم سنة وأنت ممارس لها؟", 1, 60, 2)
        h_cost = st.number_input("تكلفة الممارسة الواحدة (ريال تقريباً)", 0, 500, 10)

    if st.button("تحليل الأثر التراكمي"):
        total_times = h_freq * 365 * h_years
        total_money = total_times * h_cost
        st.write("### 📊 التقرير التحليلي:")
        r1, r2 = st.columns(2)
        r1.metric("عدد المرات الإجمالي", f"{total_times:,}")
        r2.metric("إجمالي الأموال المهدورة", f"{total_money:,} ريال")
        st.error(f"بإقلاعك عن {habit_name} اليوم، ستوفر ثروة صحية ومالية تقدر بـ {total_money:,} ريال مستقبلاً!")
        st.balloons()

# --- صفحة الدراسة (خطط دراسية متخصصة) ---
elif st.session_state.page == 'study':
    st.title("📚 التخطيط الأكاديمي")
    if st.button("🏠 العودة للرئيسية"): nav_to('main'); st.rerun()
    st.divider()

    major = st.selectbox("اختر تخصصك الجامعي:", [
        "هندسة الشبكات والأمن السيبراني", 
        "هندسة الحاسب", 
        "علوم الحاسب والبرمجيات",
        "تخصص تقني آخر"
    ])
    study_hours = st.select_slider("ساعات المذاكرة المتاحة يومياً:", options=range(1, 13), value=4)

    if st.button("توليد الخطة الدراسية"):
        st.success(f"خطة مقترحة يا عبد الله لتخصص {major}:")
        if "شبكات" in major or "الأمن" in major:
            st.info(f"📍 تخصيص {study_hours * 0.6:.1f} ساعة للتدريب العملي على اللابات (Labs).")
            st.info(f"📍 تخصيص {study_hours * 0.4:.1f} ساعة لمذاكرة الجانب النظري والشهادات المهنية.")
        else:
            st.info(f"📍 تخصيص 70% من وقتك للتطبيق البرمجي الفعلي.")
            st.info(f"📍 تخصيص 30% لمراجعة الأساسيات النظرية.")
        st.snow()

show_footer()
