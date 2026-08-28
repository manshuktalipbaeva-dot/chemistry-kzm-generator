import streamlit as st
from docx import Document
from io import BytesIO

st.set_page_config(
    page_title="ҚМЖ Генераторы - Word форматы",
    page_icon="📑",
    layout="wide"
)

st.title("📑 Химия пәнінен Кәсіби ҚМЖ Генераторы (Word кестесі)")
st.write("Бұл жүйе әр тақырыпқа сай әр түрлі тапсырмалар, дескрипторлар мен кестелер құрып, оны тікелей Word форматында жүктеп алуға мүмкіндік береді.")

with st.form("word_kmz_form"):
    st.subheader("Сабақ деректерін енгізіңіз:")
    
    col1, col2 = st.columns(2)
    with col1:
        org_name = st.text_input("Білім беру ұйымының атауы:", value="№ орта мектебі КММ")
        teacher_name = st.text_input("Педагогтің аты-жөні:", placeholder="Аты-жөніңіз")
        lesson_date = st.text_input("Күні:", value="28.08.2026")
        subject = st.text_input("Пән:", value="Химия")
        section = st.text_input("Бөлім:", value="Атом құрылысының таралуы")
        grade = st.selectbox("Сынып:", ["7-сынып", "8-сынып", "9-сынып", "10-сынып (ЖМБ)", "11-сынып (ЖМБ)"])
        topic = st.text_input("Сабақтың тақырыбы:", value="Атом — күрделі бөлшек. «Орташа салыстырмалы атомдық массаны есептеу»")
    
    with col2:
        learning_obj = st.text_area("Оқу мақсаты:", value="10.1.2.1 - нуклидтер мен нуклондар ұғымының физикалық мәнін түсіндіру; 10.1.2.2 - табиғи қопадағы химиялық элемент изотоптарының орташа салыстырмалы атомдық массаларын есептеу")
        value_name = st.text_input("Құндылық:", value="Зайырлы қоғам және жоғары руханият")
        quote = st.text_input("Аптаның дәйексөзі:", value="Білім – инемен құдық қазғандай.")

    submit_btn = st.form_submit_button(label="📥 Word кестесін жасақтау және жүктеу")

if submit_btn:
    if not topic or not learning_obj:
        st.error("⚠️ Өтінемін, тақырып пен оқу мақсатын толтырыңыз!")
    else:
        st.success("✨ ҚМЖ кестесі сәтті дайындалды!")

        # Word документин құру
        doc = Document()
        doc.add_heading(f"{org_name}", level=3)
        doc.add_heading(f"ҚЫСҚА МЕРЗІМДІ САБАҚ ЖОСПАРЫ: {topic}", level=1)

        # Ақпараттық кесте
        table_info = doc.add_table(rows=8, cols=2)
        table_info.style = 'Table Grid'
        
        info_data = [
            ("Бөлім", section),
            ("Педагогтің аты-жөні", teacher_name if teacher_name else "[ ]"),
            ("Күні", lesson_date),
            ("Сынып", f"Қатысушылар саны: 20 | Қатыспағандар саны: 0"),
            ("Сабақтың тақырыбы", topic),
            ("Оқыту мақсаттары", learning_obj),
            ("Сабақтың мақсаты", f"Оқу мақсатына сәйкес {topic} бойынша есептер шығарады және изотоптардың орташа атомдық массасын есептейді."),
            ("Құндылық", value_name)
        ]

        for i, (k, v) in enumerate(info_data):
            table_info.cell(i, 0).text = k
            table_info.cell(i, 1).text = v

        doc.add_paragraph("\nСАБАҚТЫҢ БАРЫСЫ")

        # Сабақ барысы кестесі
        table_course = doc.add_table(rows=4, cols=5)
        table_course.style = 'Table Grid'
        
        headers = ["Сабақтың кезеңі/уақыты", "Педагогтің әрекеті", "Оқушының әрекеті", "Бағалау", "Ресурстар"]
        for j, h in enumerate(headers):
            table_course.cell(0, j).text = h

        course_data = [
            ("Сабақтың басы\n(0-5 мин)", "1. Ұйымдастыру, түгелдеу.\n2. Психологиялық ахуал.\n3. Дәйексөз: «{quote}»", "Амандасады, ой бөліседі.", "Мадақтау", "Оқулық, тақта"),
            ("Сабақтың ортасы\n(5-35 мин)", f"1. Тақырып бойынша жаңа түсініктер беру.\n2. Сараланған тапсырмалар ұсыну.\n3. Изотоптар мен нуклидтерге есептер шығарту.", "Тапсырмаларды дескриптор бойынша орындайды.", "Критерий: Есептейді.\nДескриптор:\n- Формула таңдайды - 1 б.\n- Есептейді - 1 б.", "Үлестірмелі материалдар"),
            ("Сабақтың соңы\n(35-45 мин)", "1. Рефлексия: «Табыс басқышы».\n2. Үй тапсырмасын беру.", "Стикерге өз ойын жазады.", "Жиынтық баға (10 балл)", "Стикерлер")
        ]

        for row_idx, row_content in enumerate(course_data, start=1):
            for col_idx, text in enumerate(row_content):
                table_course.cell(row_idx, col_idx).text = text

        # 10 балдық бағалау картасы
        doc.add_heading("1-ҚОСЫМША. 10 БАЛДЫҚ БАҒАЛАУ КАРТАСЫ", level=2)
        table_eval = doc.add_table(rows=5, cols=5)
        table_eval.style = 'Table Grid'
        
        eval_headers = ["№", "Тапсырма", "Бағалау критерийі", "Дескриптор", "Балл"]
        for j, h in enumerate(eval_headers):
            table_eval.cell(0, j).text = h

        eval_rows = [
            ("1", "1-тапсырма", "Нуклидтерді анықтайды", "Физикалық мағынасын түсіндіреді", "2"),
            ("2", "2-тапсырма", "Изотоптарды ажыратады", "Құрамын сипаттайды", "3"),
            ("3", "3-тапсырма", "Орташа массаны есептейді", "Формуланы дұрыс қолданады", "3"),
            ("4", "Қорытынды", "Қорытынды жасайды", "Ой тұжырымдайды", "2")
        ]

        for row_idx, row_content in enumerate(eval_rows, start=1):
            for col_idx, text in enumerate(row_content):
                table_eval.cell(row_idx, col_idx).text = text

        # Файлды жадта сақтау
        buffer = BytesIO()
        doc.save(buffer)
        buffer.seek(0)

        st.download_button(
            label="📄 Word (.docx) файлы түрінде жүктеп алу",
            data=buffer,
            file_name=f"QMZ_{topic[:20]}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
