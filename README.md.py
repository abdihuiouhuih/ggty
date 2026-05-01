import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="تطبيق التحديات المتكامل", layout="centered")

# تنسيق اللغة العربية
st.markdown("""<style> .main { text-align: right; direction: rtl; } div[data-testid="stBlock"] { direction: rtl; } button { border-radius: 12px; height: 3em; font-weight: bold; } </style>""", unsafe_allow_html=True)

# 2. إدارة التنقل بين الصفحات
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
        st.info(f"للحفاظ على وزنك تحتاج تقريباً {round(bmr * 1.375)} سعرة يومياً.")

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
        st.error(f"لقد مارست هذه العادة حوالي {total:,} مرة خلال {years} سنوات!")
        st.write("الهدف: صفر ممارسة لمدة 21 يوم متواصلة.")

# --- صفحة تحدي الدراسة (التخصصات الموسعة) ---
elif st.session_state.page == 'study':
    st.title("📚 مركز التخطيط الدراسي")
    if st.button("⬅️ العودة للرئيسية"):
        go_to('main')
        st.rerun()
    
    st.divider()
    
    # اختيار المجال الكبير
    category = st.selectbox("اختر مجال دراستك:", [
        "هندسة الحاسب والأمن السيبراني", 
        "تطوير البرمجيات والذكاء الاصطناعي", 
        "الهندسة المدنية والميكانيكية",
        "العلوم الإدارية والمالية", 
        "العلوم الصحية والطب",
        "اللغات والترجمة"
    ])

    # تخصصات فرعية بناءً على اختيارك
    if category == "هندسة الحاسب والأمن السيبراني":
        sub = st.selectbox("التخصص الدقيق:", ["Network Engineering (Cisco)", "Cybersecurity (SOC/Pentesting)", "Cloud Computing (AWS/Azure)", "Hardware Engineering"])
    elif category == "تطوير البرمجيات والذكاء الاصطناعي":
        sub = st.selectbox("التخصص الدقيق:", ["Frontend (React/Vue)", "Backend (Node/Python)", "Data Science", "AI & Robotics"])
    elif category == "العلوم الإدارية والمالية":
        sub = st.selectbox("التخصص الدقيق:", ["إدارة أعمال", "محاسبة", "تسويق رقمي", "علاقات عامة"])
    else:
        sub = st.text_input("اكتب تخصصك بدقة:")

    hours = st.slider("ساعات الدراسة المستهدفة اليوم:", 1, 12, 4)

    if st.button("توليد خطة الدراسة"):
        st.write(f"### 📋 خطة الـ {hours} ساعات لتخصص {sub}:")
        
        # منطق توزيع الخطة
        if "Cisco" in sub or "Network" in sub:
            st.success(f"• أول {hours*0.5:.1f} ساعة: تطبيق عملي على Packet Tracer أو GNS3.")
            st.info(f"• باقي الوقت: مراجعة نظريات البروتوكولات ورسم الشبكة.")
        elif "Security" in sub or "Cyber" in sub:
            st.success(f"• أول {hours*0.6:.1f} ساعة: تدريب على منصات مثل TryHackMe أو التحقق من الثغرات.")
            st.info(f"• باقي الوقت: قراءة تقارير أمنية أو مراجعة أدوات اللينكس.")
        else:
            st.success(f"• 60% من الوقت: قراءة وفهم المبادئ الأساسية.")
            st.info(f"• 40% من الوقت: تلخيص وحل أسئلة السنوات السابقة.")
        st.balloons()
