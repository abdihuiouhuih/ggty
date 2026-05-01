# --- صفحة تحدي الدراسة (نسخة مطورة) ---
elif st.session_state.page == 'study':
    st.title("📚 مركز التخطيط الدراسي الشامل")
    if st.button("⬅️ العودة للرئيسية"):
        change_page('main')
        st.rerun()
    
    st.divider()
    
    # تصنيف التخصصات
    category = st.selectbox("اختر مجال دراستك:", [
        "الأمن السيبراني والشبكات", 
        "تطوير البرمجيات والذكاء الاصطناعي", 
        "العلوم الإدارية والمالية", 
        "الهندسة (الكهربائية/الميكانيكية)",
        "العلوم الصحية"
    ])

    # تخصصات فرعية بناءً على المجال
    if category == "الأمن السيبراني والشبكات":
        sub_major = st.selectbox("التخصص الدقيق:", ["Network Engineering (CCNA/CCNP)", "Ethical Hacking", "Digital Forensics", "Zero Trust Architecture"])
    elif category == "تطوير البرمجيات والذكاء الاصطناعي":
        sub_major = st.selectbox("التخصص الدقيق:", ["Full Stack Development", "Data Science", "Machine Learning", "Mobile Apps"])
    else:
        sub_major = st.text_input("اكتب اسم تخصصك بالتحديد:")

    hours = st.slider("كم ساعة تنوي الدراسة اليوم؟", 1, 12, 4)

    if st.button("توليد الجدول الدراسي"):
        st.write(f"### 📋 خطة الـ {hours} ساعات لتخصص {sub_major}:")
        
        # توزيع الساعات بناءً على المجال
        if category == "الأمن السيبراني والشبكات":
            st.success(f"• **أول {hours*0.4:.1f} ساعة:** تطبيق عملي على Packet Tracer أو GNS3 (Labs).")
            st.info(f"• **ثاني {hours*0.4:.1f} ساعة:** دراسة البروتوكولات (OSPF, BGP, NAT) أو الثغرات.")
            st.warning(f"• **آخر {hours*0.2:.1f} ساعة:** مراجعة الـ Commands وتدوين الملاحظات للامتحان.")
            
        elif category == "تطوير البرمجيات والذكاء الاصطناعي":
            st.success(f"• **أول {hours*0.6:.1f} ساعة:** كتابة الكود (Coding Session) وحل المشكلات.")
            st.info(f"• **باقي الوقت:** قراءة الـ Documentation أو مشاهدة دروس تقنيات جديدة.")
            
        else:
            st.success(f"• **50% من الوقت:** مذاكرة المفاهيم الأساسية.")
            st.info(f"• **50% من الوقت:** حل تمارين واختبارات تجريبية.")

        st.balloons()
