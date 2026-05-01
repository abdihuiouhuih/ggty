import streamlit as st

# 1. إعدادات الهوية والتنسيق الاحترافي (CSS)
st.set_page_config(page_title="منصة عبد الله للتحديات", layout="wide")

st.markdown("""
    <style>
    /* إخفاء عناصر المطور وتنسيق الواجهة */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stStatusWidget"] {display: none;}
    
    /* تنسيق الخطوط والمحتوى العربي */
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    
    /* ستايل البطاقات في الشاشة الرئيسية */
    .feature-card {
        background-color: #1e2130;
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
        text-align: center;
        transition: 0.4s;
        border: 1px solid #3d4156;
        margin-bottom: 20px;
        color: white;
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
    st.markdown('<div class="custom-footer">جميع الحقوق محفوظة © | تطوير: عبد الله الأحمري 👨‍💻</div>', unsafe_allow_html=True)

# إدارة التنقل بين الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav_to(page):
    st.session_state.page = page

# --- الشاشة الرئيسية ---
if st.session_state.page == 'main':
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏆 منصة الإنجاز اليومي</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2em;'>اختر مسارك اليوم وطور حياتك</p>", unsafe_allow_html=True)
    st.write("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="feature-card"><h2>⚡</h2><h3>تحدي الأداء البدني</h3><p>المختبر الرياضي لحساب سعراتك واحتياج جسمك</p></div>', unsafe_allow_html=True)
        if st.button("دخول المختبر الرياضي"): nav_to('fitness'); st.rerun()
    with col2:
        st.markdown('<div class="feature-card"><h2>💎</h2><h3>تحدي الانضباط الشخصي</h3><p>رادار العادات لتحليل مكاسب الترك والإقلاع</p></div>', unsafe_allow_html=True)
        if st.button("دخول رادار العادات"): nav_to('habits'); st.rerun()
    with col3:
        st.markdown('<div class="feature-card"><h2>📖</h2><h3>تحدي التفوق الدراسي</h3><p>مركز التخطيط الذكي لطلاب الجامعات والمدارس</p></div>', unsafe_allow_html=True)
        if st.button("دخول مركز التخطيط"): nav_to('study'); st.rerun()

# --- صفحة الرياضة (تحدي الأداء البدني) ---
elif st.session_state.page == 'fitness':
    st.title("🏋️ المختبر الرياضي الذكي")
    if st.button("🏠 العودة للرئيسية"): nav_to('main'); st.rerun()
    st.divider()

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📋 قياسات الجسم")
        weight = st.number_input("الوزن (كجم)", 40, 200, 80)
        height = st.number_input("الطول (سم)", 120, 230, 175)
        age = st.number_input("العمر", 15, 90, 25)
        gender = st.radio("الجنس", ["ذكر", "أنثى"], horizontal=True)
    with c2:
        st.subheader("⚡ النشاط والهدف")
        # تحويل الشريط إلى خيارات (Radio) كما طلبت
        activity = st.radio("مستوى النشاط الأسبوعي:", [
            "خامل (لا توجد تمارين)", 
            "خفيف (تمارين 1-3 أيام)", 
            "متوسط (تمارين 3-5 أيام)", 
            "نشط جداً (تمارين يومية مكثفة)"
        ])
        goal = st.selectbox("ما هو هدفك الحالي؟", ["خسارة وزن (تنشيف)", "محافظة", "بناء عضلات (تضخيم)"])

    if st.button("حساب الاحتياج"):
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + (5 if gender == "ذكر" else -161)
        factor = {"خامل (لا توجد تمارين)": 1.2, "خفيف (تمارين 1-3 أيام)": 1.375, "متوسط (تمارين 3-5 أيام)": 1.55, "نشط جداً (تمارين يومية مكثفة)": 1.725}[activity]
        maint = bmr * factor
        
        st.write("---")
        res1, res2 = st.columns(2)
        res1.metric("سعرات المحافظة", f"{int(maint)} سعرة")
        target = maint - 500 if "خسارة" in goal else maint + 300 if "بناء" in goal else maint
        res2.metric("السعرات المستهدفة", f"{int(target)} سعرة")
        st.success(f"يا عبد الله، بناءً على قياساتك، هذا هو وقود جسمك المثالي للوصول لهدف الـ {goal}.")

# --- صفحة العادات (تحدي الانضباط الشخصي) ---
elif st.session_state.page == 'habits':
    st.title("🚫 رادار ترك العادات")
    if st.button("🏠 العودة للرئيسية"): nav_to('main'); st.rerun()
    st.divider()

    col_h1, col_h2 = st.columns(2)
    with col_h1:
        habit = st.text_input("اسم العادة التي تريد الإقلاع عنها:")
        h_freq = st.radio("كم مرة تمارسها يومياً؟", [1, 2, 3, 5, 10, "أكثر من ذلك"])
    with col_h2:
        h_years = st.number_input("منذ كم سنة تمارسها؟", 1, 60, 2)
        h_cost = st.number_input("التكلفة التقديرية للمرة الواحدة (ريال)", 0, 500, 10)

    if st.button("تحليل الخسائر والمكاسب"):
        freq_num = h_freq if isinstance(h_freq, int) else 15
        total_days = h_years * 365
        total_times = freq_num * total_days
        total_money = total_times * h_cost
        
        st.markdown(f"### 📊 تقرير رحلة التغيير")
        st_c1, st_c2 = st.columns(2)
        st_c1.metric("مرات الممارسة السابقة", f"{total_times:,} مرة")
        st_c2.metric("إجمالي المبالغ المستردة مستقبلاً", f"{total_money:,} ريال")
        st.success(f"يا عبد الله، بتركك لعادة {habit} ستوفر ثروة من الصحة والمال تقدر بـ {total_money:,} ريال!")
        st.balloons()

# --- صفحة الدراسة (تحدي التفوق الدراسي) ---
elif st.session_state.page == 'study':
    st.title("📚 مركز التخطيط الدراسي")
    if st.button("🏠 العودة للرئيسية"): nav_to('main'); st.rerun()
    st.divider()

    level = st.selectbox("المرحلة الدراسية / التخصص:", [
        "جامعي - هندسة شبكات", 
        "جامعي - أمن سيبراني", 
        "جامعي - تخصص تقني آخر",
        "مرحلة الثانوية",
        "مرحلة المتوسطة"
    ])
    
    s_col1, s_col2 = st.columns(2)
    with s_col1:
        study_hours = st.radio("ساعات المذاكرة المتاحة يومياً:", [2, 4, 6, 8, 10])
        focus_area = st.multiselect("ما هي أولوياتك؟", ["الجانب العملي", "المذاكرة النظرية", "حل اختبارات سابقة", "تعلم مهارات إضافية"])
    with s_col2:
        current_status = st.select_slider("مستواك الحالي في المواد:", options=["ضعيف", "متوسط", "جيد", "ممتاز"])

    if st.button("توليد خطة النجاح"):
        st.success(f"الخطة المقترحة يا عبد الله لمسار {level}:")
        if "جامعي" in level:
            st.info(f"📍 تخصيص {study_hours * 0.6:.1f} ساعة للتطبيق العملي (Labs) والمشاريع.")
            st.info(f"📍 تخصيص {study_hours * 0.4:.1f} ساعة للمذاكرة النظرية والشهادات المهنية.")
        else:
            st.info(f"📍 تخصيص 70% من وقتك للمواد الأساسية و 30% للمراجعة المستمرة.")
        st.snow()

show_footer()
