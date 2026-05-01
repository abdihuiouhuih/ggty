import streamlit as st

# 1. الإعدادات العامة والجماليات (CSS)
st.set_page_config(page_title="منصة عبدالله للتحديات", layout="wide")

st.markdown("""
    <style>
    /* إخفاء عناصر المطور وتنسيق الصفحة */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stStatusWidget"] {display: none;}
    
    /* تنسيق الخطوط والمحتوى العربي */
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    
    /* ستايل البطاقات في الشاشة الرئيسية */
    .card-container {
        background-color: #1e2130;
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        text-align: center;
        transition: 0.4s ease-in-out;
        border: 1px solid #3d4156;
        color: white;
        margin-bottom: 20px;
    }
    .card-container:hover {
        transform: translateY(-12px);
        border-color: #4CAF50;
        box-shadow: 0 12px 30px rgba(76, 175, 80, 0.2);
    }
    
    /* تنسيق الفوتر (حقوق عبدالله) */
    .footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        background-color: #0e1117; color: #4CAF50; text-align: center;
        padding: 15px; font-weight: bold; z-index: 1000;
        border-top: 2px solid #4CAF50;
        font-size: 16px;
    }
    
    /* تحسين الأزرار */
    .stButton>button {
        width: 100%; border-radius: 15px; height: 3.5em; font-weight: bold;
        background-color: #4CAF50; color: white; border: none; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #45a049; color: white; }
    </style>
    """, unsafe_allow_html=True)

# دالة عرض الحقوق
def show_rights():
    st.markdown('<div class="footer">جميع الحقوق محفوظة © 2026 | تطوير المهندس: عبدالله الأحمري 👨‍💻</div>', unsafe_allow_html=True)

# إدارة الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def go_to(page_name):
    st.session_state.page = page_name

# --- 1. الشاشة الرئيسية الاحترافية ---
if st.session_state.page == 'main':
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏆 منصة الإنجاز اليومي</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.3em;'>مرحباً بك يا بطل، اختر وجهتك لليوم</p>", unsafe_allow_html=True)
    st.write("---")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="card-container"><h2>🏋️‍♂️</h2><h3>المختبر الرياضي</h3><p>تحليل كامل لجسمك وحساب السعرات والنشاط</p></div>', unsafe_allow_html=True)
        if st.button("دخول القسم الرياضي"): go_to('fitness'); st.rerun()

    with col2:
        st.markdown('<div class="card-container"><h2>🚭</h2><h3>رادار العادات</h3><p>تتبع رحلة الإقلاع وتحليل الأثر الزمني والمالي</p></div>', unsafe_allow_html=True)
        if st.button("بدء تحدي العادات"): go_to('habits'); st.rerun()

    with col3:
        st.markdown('<div class="card-container"><h2>🎓</h2><h3>أكاديمية التفوق</h3><p>خطط دراسية ذكية مخصصة لطلاب الهندسة والتقنية</p></div>', unsafe_allow_html=True)
        if st.button("تخطيط دراستي"): go_to('study'); st.rerun()

# --- 2. صفحة المختبر الرياضي (تحدي اللياقة) ---
elif st.session_state.page == 'fitness':
    st.title("🏋️‍♂️ المختبر الرياضي الذكي")
    if st.button("🏠 العودة للرئيسية"): go_to('main'); st.rerun()
    st.divider()

    c1, c2 = st.columns([1, 1.2])
    with c1:
        st.subheader("📋 أدخل بيانات جسمك")
        gender = st.radio("الجنس", ["ذكر", "أنثى"], horizontal=True)
        weight = st.number_input("الوزن (كجم)", 40.0, 200.0, 80.0)
        height = st.number_input("الطول (سم)", 120, 230, 175)
        age = st.number_input("العمر", 15, 90, 22)
        
        st.write("**مستوى النشاط الأسبوعي:**")
        activity_level = st.selectbox("اختر بدقة:", [
            "خامل (عمل مكتبي ولا توجد تمارين)",
            "نشاط خفيف (تمارين 1-3 أيام في الأسبوع)",
            "نشاط متوسط (تمارين 3-5 أيام في الأسبوع)",
            "نشاط عالٍ (تمارين 6-7 أيام في الأسبوع)",
            "نشاط رياضي مكثف (تمارين مرتين يومياً)"
        ])

    with c2:
        st.subheader("📊 تحليل النتائج")
        # معادلة Mifflin-St Jeor
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + (5 if gender == "ذكر" else -161)
        
        # معامل النشاط
        activity_factors = {
            "خامل (عمل مكتبي ولا توجد تمارين)": 1.2,
            "نشاط خفيف (تمارين 1-3 أيام في الأسبوع)": 1.375,
            "نشاط متوسط (تمارين 3-5 أيام في الأسبوع)": 1.55,
            "نشاط عالٍ (تمارين 6-7 أيام في الأسبوع)": 1.725,
            "نشاط رياضي مكثف (تمارين مرتين يومياً)": 1.9
        }
        maintenance_calories = bmr * activity_factors[activity_level]
        bmi = weight / ((height/100)**2)
        
        res_col1, res_col2 = st.columns(2)
        res_col1.metric("مؤشر كتلة الجسم (BMI)", f"{bmi:.1f}")
        res_col2.metric("سعرات المحافظة", f"{int(maintenance_calories)} سعرة")
        
        st.write("---")
        goal = st.selectbox("ما هو هدفك؟", ["تنشيف (خسارة دهون)", "تضخيم (بناء عضلات)", "محافظة"])
        
        if goal == "تنشيف (خسارة دهون)":
            st.warning(f"لتحقيق هدفك، تناول {int(maintenance_calories - 500)} سعرة يومياً.")
        elif goal == "تضخيم (بناء عضلات)":
            st.success(f"لتحقيق هدفك، تناول {int(maintenance_calories + 300)} سعرة يومياً مع التركيز على البروتين.")
        else:
            st.info("استمر على سعرات المحافظة مع ممارسة تمارين المقاومة.")

# --- 3. صفحة رادار العادات (تحدي ترك العادات) ---
elif st.session_state.page == 'habits':
    st.title("🚫 رادار ترك العادات السيئة")
    if st.button("🏠 العودة للرئيسية"): go_to('main'); st.rerun()
    st.divider()

    col_h1, col_h2 = st.columns(2)
    with col_h1:
        habit = st.text_input("اسم العادة التي تريد تركها؟", placeholder="مثال: التدخين، السهر..")
        h_freq = st.slider("كم مرة تمارسها يومياً؟", 1, 50, 5)
        h_cost = st.number_input("التكلفة المالية التقريبية لليوم (ريال)", 0, 1000, 20)
    with col_h2:
        h_years = st.number_input("منذ كم سنة وأنت تمارسها؟", 1, 60, 3)
        st.info("💡 بمجرد الضغط على زر التحليل، ستعرف حجم الضرر الذي تسببت به هذه العادة.")

    if st.button("إظهار تقرير الخسائر"):
        total_days = h_years * 365
        total_times = h_freq * total_days
        total_money = h_cost * total_days
        
        st.markdown("### 📊 التقرير التحليلي:")
        r_c1, r_c2 = st.columns(2)
        r_c1.metric("عدد المرات الإجمالي", f"{total_times:,} مرة")
        r_c2.metric("إجمالي الأموال المهدورة", f"{total_money:,} ريال")
        
        st.error(f"يا عبدالله، لو استثمرت مبلغ {total_money:,} ريال في تخصصك، لكان الآن لديك معمل هندسة متكامل!")
        st.balloons()

# --- 4. صفحة أكاديمية التفوق (تحدي الدراسة) ---
elif st.session_state.page == 'study':
    st.title("🎓 مركز التخطيط الدراسي الذكي")
    if st.button("🏠 العودة للرئيسية"): go_to('main'); st.rerun()
    st.divider()

    st.subheader("⚙️ مخصص لطلاب الهندسة والتقنية")
    major = st.selectbox("اختر تخصصك الجامعي:", [
        "هندسة الشبكات والأمن السيبراني", 
        "هندسة الحاسب والبرمجيات", 
        "الذكاء الاصطناعي وعلم البيانات",
        "تخصص تقني آخر"
    ])
    
    s_col1, s_col2 = st.columns(2)
    with s_col1:
        hours = st.slider("كم ساعة تخصص للمذاكرة اليوم؟", 1, 14, 5)
        has_lab = st.checkbox("هل لديك تطبيق عملي أو لاب (Lab) اليوم؟")
    with s_col2:
        level = st.radio("مستواك الحالي في المواد:", ["تحت المتوسط (أحتاج تأسيس)", "متوسط", "متقدم (مراجعة فقط)"])

    if st.button("توليد خطة الدراسة المثالية"):
        st.success(f"إليك الخطة المقترحة يا مهندس عبدالله لتخصص {major}:")
        
        if has_lab:
            st.info(f"📍 تخصيص {hours * 0.6:.1f} ساعة للعمل على اللابات (Packet Tracer / VMs).")
            st.info(f"📍 تخصيص {hours * 0.4:.1f} ساعة لمذاكرة الجانب النظري والبروتوكولات.")
        else:
            st.info(f"📍 تخصيص 70% من الوقت للمذاكرة العميقة و 30% لحل أسئلة الاختبارات السابقة.")
        
        if "الأمن السيبراني" in major:
            st.warning("نصيحة: لا تنسَ تخصيص وقت لمنصات التدريب مثل TryHackMe أو HTB.")
        st.snow()

show_rights()
