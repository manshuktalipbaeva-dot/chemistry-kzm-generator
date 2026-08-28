import streamlit as st

st.set_page_config(page_title="Химия ҚМЖ Генераторы", page_icon="🧪", layout="centered")

st.title("🧪 Химия пәнінен ҚМЖ (Қысқа мерзімді жоспар) генераторы")
st.write("Бұл жүйе мектеп мұғалімдеріне химия сабақтарының жоспарын жылдам жасауға көмектеседі.")

with st.form("kmz_form"):
    st.subheader("Сабақ деректерін енгізіңіз:")
    
    grade = st.selectbox("Сыныпты таңдаңыз:", ["7-сынып", "8-сынып", "9-сынып", "10-сынып (ЖМБ)", "10-сынып (ҚГБ)", "11-сынып (ЖМБ)"])
    quarter = st.selectbox("Тоқсан:", ["1-тоқсан", "2-тоқсан", "3-тоқсан", "4-тоқсан"])
    topic = st.text_input("Сабақтың тақырыбы:", placeholder="Мысалы: Оттегі, оның алынуы мен қасиеттері")
    learning_objective = st.text_area("Оқу мақсаты (ОМ):", placeholder="Мысалы: 8.4.1.2 - оттегінің зертханада алынуын сипаттау")
    
    submit_button = st.form_submit_button(label="ҚМЖ жасақтау")

if submit_button:
    if not topic or not learning_objective:
        st.error("⚠️ Өтінемін, сабақ тақырыбы мен оқу мақсатын толық жазыңыз!")
    else:
        st.success("✨ ҚМЖ сәтті дайындалды!")
        
        st.markdown("---")
        st.subheader(f"📄 Қысқа мерзімді жоспар (ҚМЖ)")
        
        st.markdown(f"**Пән:** Химия")
        st.markdown(f"**Сынып:** {grade} | **Тоқсан:** {quarter}")
        st.markdown(f"**Сабақ тақырыбы:** {topic}")
        st.markdown(f"**Оқу мақсаты:** {learning_objective}")
        
        st.markdown("### Сабақтың барысы:")
        
        with st.expander("1. Ұйымдастыру кезеңі (3 минут)", expanded=True):
            st.write("- Сәлемдесу, оқушылардың түгелдігін тексеру.")
            st.write("- Психологиялық ахуал тудыру.")
            
        with st.expander("2. Үй тапсырмасын тексеру (7 минут)"):
            st.write("- «Миға шабуыл» әдісі арқылы өткен тақырыпты пысықтау.")
            
        with st.expander("3. Жаңа сабаққа кіріспе (10 минут)"):
            st.write(f"- **Негізгі сұрақ:** {topic} өмірде не үшін қажет?")
            
        with st.expander("4. Практикалық бөлім (15 минут)"):
            st.write("- **Тапсырма:** Берілген тақырып бойынша жұмыс жасау.")
            st.markdown("*Дескрипторлар:* \n1. Негізгі ұғымдарды түсіндіреді; \n2. Мысал келтіреді.")
            
        with st.expander("5. Қорытынды және Кері байланыс (5 минут)"):
            st.write("- **«Табыс басқышы» әдісі арқылы кері байланыс алу.**")

        kmz_text = f"Пән: Химия\nСынып: {grade}\nТоқсан: {quarter}\nТақырып: {topic}\nОқу мақсаты: {learning_objective}"
        st.download_button(
            label="📥 ҚМЖ-ны жүктеп алу (Мәтіндік файл)",
            data=kmz_text,
            file_name=f"QMZ_{topic}.txt",
            mime="text/plain"
        )
