# University FAQ Assistant

import streamlit as st

st.title("🎓 University FAQ Assistant")

st.write("Ask any question related to admissions, programs, or policies.")

question = st.text_input("Enter your question:")

if question:
    st.write("You asked:")
    st.success(question)
