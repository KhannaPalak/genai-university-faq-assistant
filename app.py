import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

st.set_page_config(page_title="University FAQ Assistant")

st.title("🎓 University FAQ Assistant")

# Check if API key is loaded
if os.getenv("OPENAI_API_KEY"):
    st.success("OpenAI API key loaded successfully ✅")
else:
    st.error("OpenAI API key NOT found ❌")

st.write("Next step: connect documents and RAG pipeline.")
