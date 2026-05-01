import streamlit as st

# 1. إعدادات الصفحة والجماليات
st.set_page_config(page_title="تطبيق التحديات - عبدالله الأحمري", layout="centered")

st.markdown("""
    <style>
    /* إخفاء عناصر المطور */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    stDeployButton {display:none;}
    [data-testid="stStatusWidget"] {display: none;}
    
    /* تنسيق المحتوى العربي */
    .main { text-align: right; direction: rtl; }
    div[data-testid="stBlock"] { direction: rtl; }
    
    /* تحسين شكل الأزرار في الصفحة الرئيسية */
    div.stButton > button {
        border-radius: 20px;
        height: 150px;
        font-size: 24px !important;
        font-weight: bold;
        transition: all 0.3s ease;
        border: 2px solid #e6e9ef;
    }
    
    /* تأثير عند مرور الماوس على الأزرار */
    div.stButton > button:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        border-color: #4CAF50;
    }

    /* ستايل الحقوق السفلي */
    .custom-footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        background-color: #1E1E1E; color: white; text-align: center;
        padding: 12px; font-size: 15px; font-weight: bold;
        z-index: 999;
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

# --- الصفحة الرئيسية (التصميم الجديد) ---
if st.session_state.page == 'main':
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏆 منصة التحديات اليومية</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px;'>مرحباً بك يا بطل، اختر مسارك للبدء في التغيير</p>", unsafe_allow_html=True)
    st.write("---")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🏃\n\nتحدي اللياقة"):
            go_to('fitness'); st.rerun()

    with col2:
        if st.button("🚫\n\nترك العادات"):
            go_to('habits'); st.rerun()

    with col3:
        if st.button("📚\n\nالتفوق الدراسي"):
            go_to('study'); st.rerun()
    
    st.write("---")
    st.info("💡 نصيحة اليوم: النجاح هو مجموع تفاصيل صغيرة تُنفذ بانتظام.")

# --- صفحة التحدي الرياضي ---
elif st.session_state.page == 'fitness':
    st.title("🏃 المركز الرياضي")
    if st.button("⬅️ العودة للرئيسية"): go_to('main'); st.rerun()
    st.divider()
    # كود صفحة الرياضة السابق...
    st.info("أدخل بياناتك لتحصل على تحليل كامل لجسمك.")

# --- صفحة ترك العادات ---
elif st.session_state.page == 'habits':
    st.title("🚫 تحدي الإقلاع عن العادات")
    if st.button("⬅️ العودة للرئيسية"): go_to('main'); st.rerun()
    st.divider()
    # كود صفحة العادات السابق...
    st.warning("كل يوم يمر بدون العادة هو انتصار جديد.")

# --- صفحة تحدي الدراسة ---
elif st.session_state.page == 'study':
    st.title("📚 التخطيط الدراسي")
    if st.button("⬅️ العودة للرئيسية"): go_to('main'); st.rerun()
    st.divider()
    # كود صفحة الدراسة السابق...
    st.success("الاستمرار في التعلم هو مفتاح التميز المهني.")

show_copyright()
