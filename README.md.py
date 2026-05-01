import streamlit as st

# 1. إعدادات الهوية البصرية والتنسيق (CSS)
st.set_page_config(page_title="منصة عبدالله للأداء العالي", layout="wide")

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
    
    /* إصلاح اتجاه العناصر وحل مشكلة الـ Slider */
    div[data-testid="stSlider"] { direction: ltr; } /* الـ Slider يعمل أفضل في التنسيق اليساري لتجنب عكس الأرقام */
    div[data-testid="stMarkdownContainer"] { text-align: right; }
    
    /* ستايل البطاقات الاحترافية */
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

    /* الفوتر (حقوق عبدالله) */
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
    st.markdown('<div class="custom-footer">جميع الحقوق محفوظة © 2026 | تطوير المهندس: عبدالله الأحمري 👨‍💻</div>', unsafe_allow_html=True)

# إدارة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav_to(page):
    st.session_state.page = page

# --- الشاشة الرئيسية ---
if st.session_state.page == 'main':
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏆 منصة عبدالله للإنجاز اليومي</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2em;'>اختر تخصصك لليوم وابدأ التحدي</p>", unsafe_allow_html=True)
    st.write("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="feature-card"><h2>🔥</h2><h3>تحدي اللياقة</h3><p>حساب السعرات والماكروز بناءً على نشاطك</p></div>', unsafe_allow_html=True)
        if st.button("دخول المختبر الرياضي"): nav_to('fit'); st.rerun()
    with col2:
        st.markdown('<div class="feature-card"><h2>🚫</h2><h3>تحدي العادات</h3><p>تحليل عميق للأثر المالي والزمني للعادات</p></div>', unsafe_allow_html=True)
        if st.button("بدء رحلة الإقلاع"): nav_to('habit'); st.rerun()
    with col3:
        st.markdown('<div class="feature-card"><h2>📖</h2><h3>تحدي الدراسة</h3><p>خطط دراسية مخصصة لطلاب الهندسة والتقنية</p></div>', unsafe_allow_html=True)
        if st.button("تخطيط جدولك"): nav_to('study'); st.rerun()

# --- صفحة الرياضة ---
elif st.session_state.page == 'fit':
    st.title("🏋️ المختبر الرياضي الذكي")
    if st.button("⬅️ العودة للرئيسية"): nav_to('main'); st.rerun()
    st.divider()

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📋 البيانات الأساسية")
        weight = st.number_input("الوزن (كجم)", 40, 200, 80)
        height = st.number_input("الطول (سم)", 120, 230, 175)
        age = st.number_input("العمر", 15, 90, 25)
        gender = st.radio("الجنس", ["ذكر", "أنثى"], horizontal=True)
    with c2:
        st.subheader("⚡ مستوى النشاط")
        activity = st.selectbox("اختر مستواك الحقيقي:", [
            "خامل (لا تمارين)", 
            "خفيف (تمارين 1-3 أيام)", 
            "متوسط (تمارين 3-5 أيام)", 
            "نشط جداً (تمارين يومية مكثفة)"
        ])
        goal = st.selectbox("هدفك الحالي:", ["تنشيف", "محافظة", "تضخيم"])

    if st.button("تحليل البيانات"):
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + (5 if gender == "ذكر" else -161)
        factor = {"خامل (لا تمارين)": 1.2, "خفيف (تمارين 1-3 أيام)": 1.375, "متوسط (تمارين 3-5 أيام)": 1.55, "نشط جداً (تمارين يومية مكثفة)": 1.725}[activity]
        maint = bmr * factor
        
        st.write("---")
        res1, res2 = st.columns(2)
        res1.metric("سعرات المحافظة", f"{int(maint)} سعرة")
        if goal == "تنشيف": target = maint - 500
        elif goal == "تضخيم": target = maint + 300
        else: target = maint
        res2.metric("السعرات المستهدفة", f"{int(target)} سعرة")
        st.success(f"يا عبدالله، بناءً على طولك ({height}سم) ونشاطك، هذا هو وقود جسمك المثالي.")

# --- صفحة العادات ---
elif st.session_state.page == 'habit':
    st.title("🚫 رادار ترك العادات")
    if st.button("⬅️ العودة للرئيسية"): nav_to('main'); st.rerun()
    st.divider()

    col_h1, col_h2 = st.columns(2)
    with col_h1:
        h_name = st.text_input("اسم العادة:")
        h_freq = st.slider("كم مرة تمارسها يومياً؟", 1, 50, 5) # تم تعديل الـ Slider ليعمل بشكل سليم
    with col_h2:
        h_years = st.number_input("منذ كم سنة تمارسها؟", 1, 60, 2)
        h_cost = st.number_input("تكلفة المرة الواحدة (ريال)", 0, 100, 10)

    if st.button("تحليل الأثر التراكمي"):
        total_times = h_freq * 365 * h_years
        total_money = total_times * h_cost
        st.error(f"تحذير: لقد مارست {h_name} حوالي {total_times:,} مرة، وكلفتك قرابة {total_money:,} ريال!")
        st.info("💡 قرارك اليوم بتركها سيوفر لك ثروة صحية ومالية في المستقبل.")
        st.balloons()

# --- صفحة الدراسة ---
elif st.session_state.page == 'study':
    st.title("📚 التخطيط الأكاديمي")
    if st.button("⬅️ العودة للرئيسية"): nav_to('main'); st.rerun()
    st.divider()

    st.subheader("أدخل بياناتك الدراسية")
    level = st.selectbox("المستوى الدراسي:", ["ثانوي", "جامعي - تخصص هندسة شبكات", "جامعي - تخصص أمن سيبراني", "جامعي - تخصص تقني آخر"])
    study_hours = st.slider("ساعات المذاكرة المتاحة يومياً:", 1, 12, 4)

    if st.button("توليد خطة الدراسة"):
        st.success(f"خطة مقترحة يا مهندس عبدالله لمستوى {level}:")
        if "جامعي" in level:
            st.info(f"- تخصيص {study_hours * 0.6:.1f} ساعة للجانب العملي والـ Labs.")
            st.info(f"- تخصيص {study_hours * 0.4:.1f} ساعة للمذاكرة النظرية والتحضير للشهادات المهنية.")
        else:
            st.info(f"- تخصيص {study_hours * 0.7:.1f} ساعة للمواد العلمية الأساسية.")
            st.info(f"- تخصيص {study_hours * 0.3:.1f} ساعة للمراجعة وحل التدريبات.")

show_footer()
