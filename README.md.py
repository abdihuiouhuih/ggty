import streamlit as st
import time

# 1. الإعدادات العامة والجماليات (CSS)
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
    }
    .main-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    
    /* تنسيق الفوتر (الحقوق) */
    .footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        background-color: #0e1117; color: white; text-align: center;
        padding: 15px; font-weight: bold; z-index: 1000;
        border-top: 2px solid #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

# دالة عرض الحقوق
def show_footer():
    st.markdown('<div class="footer">جميع الحقوق محفوظة © 2026 | تطوير المهندس: عبدالله الأحمري 👨‍💻</div>', unsafe_allow_html=True)

# إدارة الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def navigate_to(page):
    st.session_state.page = page

# --- 1. الشاشة الرئيسية الاحترافية ---
if st.session_state.page == 'home':
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏆 منصة الإنجاز اليومي</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2em;'>صمم طريقك للنجاح مع أدواتنا المتكاملة</p>", unsafe_allow_html=True)
    st.write("---")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="main-card"><h2>🏃‍♂️</h2><h3>تحدي اللياقة</h3><p>حساب سعرات، تتبع وزن، وتخطيط رياضي</p></div>', unsafe_allow_html=True)
        if st.button("دخول المختبر الرياضي", key="btn_fit"): navigate_to('fitness'); st.rerun()

    with col2:
        st.markdown('<div class="main-card"><h2>🚫</h2><h3>الإقلاع عن العادات</h3><p>تحليل مالي ونفسي لترك العادات السيئة</p></div>', unsafe_allow_html=True)
        if st.button("بدء رحلة التغيير", key="btn_hab"): navigate_to('habits'); st.rerun()

    with col3:
        st.markdown('<div class="main-card"><h2>📚</h2><h3>التفوق الأكاديمي</h3><p>خطط دراسية مخصصة لطلاب الهندسة والتقنية</p></div>', unsafe_allow_html=True)
        if st.button("تخطيط الدراسة", key="btn_std"): navigate_to('study'); st.rerun()

# --- 2. صفحة الرياضة المتكاملة ---
elif st.session_state.page == 'fitness':
    st.title("🏃‍♂️ المختبر الرياضي الذكي")
    if st.button("🏠 العودة للرئيسية"): navigate_to('home'); st.rerun()
    st.divider()

    c1, c2 = st.columns([1, 1.5])
    with c1:
        st.subheader("📋 البيانات الشخصية")
        g = st.radio("الجنس", ["ذكر", "أنثى"], horizontal=True)
        w = st.number_input("الوزن (كجم)", 40.0, 200.0, 80.0)
        h = st.number_input("الطول (سم)", 120, 230, 175)
        a = st.number_input("العمر", 15, 90, 25)
        act = st.select_slider("مستوى النشاط الأسبوعي", ["خامل", "خفيف", "متوسط", "نشط جداً"])
        target_w = st.number_input("الوزن المستهدف", 40.0, 200.0, 75.0)

    with c2:
        st.subheader("📊 التحليل والنتائج")
        # معادلات Mifflin-St Jeor
        bmr = (10 * w) + (6.25 * h) - (5 * a) + (5 if g == "ذكر" else -161)
        factor = {"خامل": 1.2, "خفيف": 1.375, "متوسط": 1.55, "نشط جداً": 1.725}[act]
        maint = bmr * factor
        bmi = w / ((h/100)**2)
        
        res1, res2 = st.columns(2)
        res1.metric("كتلة الجسم BMI", f"{bmi:.1f}")
        res2.metric("سعرات المحافظة", f"{int(maint)} سعرة")
        
        st.write("---")
        st.write("### 📅 توقعات الرحلة")
        diff = w - target_w
        if diff > 0:
            st.warning(f"تحتاج لخسارة {diff:.1f} كجم للوصول لهدفك.")
            st.info(f"الخطة المقترحة: تناول {int(maint - 500)} سعرة يومياً لخسارة الوزن بأمان.")
        else:
            st.success("وزنك الحالي ممتاز، ركز على بناء الكتلة العضلية!")

# --- 3. صفحة العادات (عرفة العادات) ---
elif st.session_state.page == 'habits':
    st.title("🚫 رادار ترك العادات السيئة")
    if st.button("🏠 العودة للرئيسية"): navigate_to('home'); st.rerun()
    st.divider()

    col_h1, col_h2 = st.columns(2)
    with col_h1:
        h_name = st.text_input("اسم العادة")
        h_cost = st.number_input("التكلفة اليومية (ريال)", 0, 500, 20)
        h_freq = st.slider("مرات الممارسة يومياً", 1, 50, 5)
    with col_h2:
        h_years = st.number_input("عدد سنوات ممارستها", 1, 50, 3)
        h_reason = st.text_area("لماذا تريد تركها؟ (الدافع الشخصي)")

    if st.button("تحليل الأثر التراكمي"):
        total_m = h_cost * 365 * h_years
        total_f = h_freq * 365 * h_years
        
        c_res1, c_res2 = st.columns(2)
        c_res1.metric("مبالغ مهدورة", f"{total_m:,} ريال")
        c_res2.metric("مرات الممارسة", f"{total_f:,} مرة")
        
        st.error(f"تخيل لو تم استثمار مبلغ {total_m:,} ريال في تطوير مهاراتك أو في مشروع خاص!")
        st.balloons()

# --- 4. صفحة الدراسة (هندسة وتقنية) ---
elif st.session_state.page == 'study':
    st.title("📚 التخطيط الأكاديمي الذكي")
    if st.button("🏠 العودة للرئيسية"): navigate_to('home'); st.rerun()
    st.divider()

    major = st.selectbox("التخصص الدراسي", [
        "هندسة الشبكات (Cisco/Network)", 
        "الأمن السيبراني (Cybersecurity)", 
        "تطوير البرمجيات (Python/FullStack)", 
        "الذكاء الاصطناعي (AI)",
        "أخرى"
    ])
    
    st.write("### 🛠️ بناء خطتك الدراسية")
    hrs = st.slider("كم ساعة تملك اليوم؟", 1, 12, 4)
    level = st.radio("مستواك الحالي", ["مبتدئ", "متوسط", "متقدم"], horizontal=True)

    if st.button("إنشاء جدول زمني"):
        st.write(f"#### 📅 جدول مقترح لتخصص {major}:")
        if "الشبكات" in major or "الأمن" in major:
            st.success(f"1. أول {hrs*0.5:.1f} ساعة: تطبيق عملي على الـ Labs (Packet Tracer / Virtual Machines).")
            st.info(f"2. ثاني {hrs*0.3:.1f} ساعة: مراجعة المفاهيم النظرية والبروتوكولات.")
            st.warning(f"3. آخر {hrs*0.2:.1f} ساعة: تلخيص الملاحظات للاختبارات المهنية.")
        else:
            st.success(f"1. 60% من الوقت: كتابة كود وتطبيق مشاريع.")
            st.info(f"2. 40% من الوقت: حل مشكلات برمجية وقراءة التوثيق.")
        st.snow()

show_footer()
