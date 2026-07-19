# ============================================================
# Project 14 - AI SQL Assistant
#
# File: app.py
#
# Streamlit User Interface
# ============================================================

import streamlit as st

from sql_agent import ask_database


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="AI SQL Assistant",
    page_icon="🗄️"
)

st.title("🗄️ AI SQL Assistant")

st.write(
    "Ask questions about the Employee Database using natural language."
)


# ============================================================
# User Input
# ============================================================

question = st.text_input(
    "Ask your question"
)


# ============================================================
# Ask Button
# ============================================================

if st.button("Ask"):

    if question:

        with st.spinner("Thinking..."):

            answer = ask_database(question)

        st.success(answer)