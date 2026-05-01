import streamlit as st
import pandas as pd

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="منصة الإنجاز الشخصي - عبد الله", layout="wide")

# --- تنسيق CSS لتحسين المظهر وجعل الشاشة احترافية ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #4CAF50; color: white; }
    .stSelectbox, .stNumberInput { border-radius: 10px; }
    footer { visibility: hidden; }
    .footer-text { position: fixed; bottom: 10px; right: 10px; color: #888; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

# حقوق الملكية
st.markdown('<div class="footer-text">جميع الحقوق محفوظة لـ عبد الله © 2026</div>', unsafe_allow_html=True)

# --- القائمة الجانبية للتنقل بين الأقسام ---
st.sidebar.title("🎮 لوحة التحكم")
page = st.sidebar.radio("اختر القسم:", ["🏠 الشاشة الرئيسية", "🏋️ تحدي الرياضة والرشاقة", "🚫 تحدي ترك العادات", "📚 تحدي التفوق الدراسي"])

# --- 1. الشاشة الرئيسية ---
if page == "🏠 الشاشة الرئيسية":
    st.title("🚀 مرحبا بك في منصتك الاحترافية يا عبد الله")
    st.subheader("هنا يمكنك إدارة أهدافك الرياضية، الدراسية، والعادات اليومية بكفاءة عالية.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("🏋️ **الرياضة:** احسب سعراتك وراقب نشاطك.")
    with col2:
        st.success("📚 **الدراسة:** خطط لمستقبلك الأكاديمي.")
    with col3:
        st.warning("🚫 **العادات:** تخلص من العادات السلبية.")

# --- 2. تحدي الرياضة والرشاقة ---
elif page == "🏋️ تحدي الرياضة والرشاقة":
    st.title("🏋️ تحدي الرشاقة")
    
    with st.expander("📊 حاسبة السعرات الحرارية والنشاط", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            weight = st.number_input("الوزن (كجم):", min_value=30.0, value=75.0)
            height = st.number_input("الطول (سم):", min_value=100.0, value=175.0)
            age = st.number_input("العمر:", min_value=10, value=20)
        
        with col2:
            activity_level = st.selectbox("مستوى النشاط الأسبوعي:", 
                                         ["خامل (لا تمارين)", 
                                          "نشاط خفيف (1-3 أيام)", 
                                          "نشاط متوسط (3-5 أيام)", 
                                          "نشاط مكثف (6-7 أيام)", 
                                          "رياضي محترف"])
        
        if st.button("احسب السعرات المطلوبة"):
            # معادلة Mifflin-St Jeor للرجال (بناءً على طلبك كذكر)
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
            
            multipliers = {
                "خامل (لا تمارين)": 1.2,
                "نشاط خفيف (1-3 أيام)": 1.375,
                "نشاط متوسط (3-5 أيام)": 1.55,
                "نشاط مكثف (6-7 أيام)": 1.725,
                "رياضي محترف": 1.9
            }
            
            tdee = bmr * multipliers[activity_level]
            st.success(f"سعراتك الحرارية للمحافظة على الوزن هي: {int(tdee)} سعرة حرارية")
            st.info(f"لخسارة الوزن، استهدف: {int(tdee - 500)} سعرة.")

# --- 3. تحدي ترك العادات ---
elif page == "🚫 تحدي ترك العادات":
    st.title("🚫 تحدي التغيير للأفضل")
    
    habit_name = st.text_input("ما هي العادة التي تريد تركها؟")
    col1, col2 = st.columns(2)
    with col1:
        frequency = st.selectbox("كم مرة تمارس العادة يومياً؟", ["1-2 مرات", "3-5 مرات", "أكثر من 5"])
    with col2:
        years = st.number_input("منذ كم سنة تمارس هذه العادة؟", min_value=0, value=1)
    
    if st.button("ابدأ التحدي"):
        st.warning(f"لقد اتخذت خطوة شجاعة بترك {habit_name}. استمر!")
        st.write(f"تذكر أن الاستمرارية لمدة 21 يوماً كفيلة بتغيير أي سلوك.")

# --- 4. تحدي التفوق الدراسي ---
elif page == "📚 تحدي التفوق الدراسي":
    st.title("📚 التخطيط الدراسي")
    
    # تحسين القسم ليناسب تخصصك (هندسة الشبكات)
    major = st.selectbox("المرحلة / التخصص الجامعي:", 
                         ["هندسة شبكات وأمن سيبراني", "علوم حاسب", "هندسة برمجيات", "أخرى"])
    
    study_level = st.radio("مستواك الحالي في المواد:", ["ممتاز", "جيد جداً", "جيد", "تحتاج تحسين"])
    
    if major == "هندسة شبكات وأمن سيبراني":
        st.info("💡 خطة مقترحة لتخصص الشبكات:")
        st.markdown("""
        *   **الجانب العملي:** تخصيص ساعتين يومياً لمختبرات Cisco Packet Tracer أو GNS3.
        *   **الشهادات الاحترافية:** التحضير لشهادة CCNA أو CompTIA Security+.
        *   **المراجعة:** مراجعة بروتوكولات الـ TCP/IP والـ Subnetting أسبوعياً.
        """)
    
    if st.button("توليد خطة دراسية"):
        st.success(f"تم بناء خطة مخصصة لمستوى '{study_level}' في تخصص {major}.")
