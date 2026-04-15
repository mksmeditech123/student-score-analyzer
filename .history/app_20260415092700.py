import streamlit as st
from utils import calculate_average, get_grade
from utils import calculate_average, get_grade

st.title("🎓 Student Performance Analyzer")

st.write("Enter student scores:")

scores = st.text_input("Scores (comma separated)", "80, 75, 90")

if st.button("Analyze"):
    scores_list = list(map(int, scores.split(",")))
    
    avg = calculate_average(scores_list)
    grade = get_grade(avg)

    st.success(f"Average Score: {avg}")
    st.info(f"Grade: {grade}")