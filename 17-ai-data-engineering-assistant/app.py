# ============================================================
# Project 17 - AI Data Engineering Assistant
#
# File: app.py
#
# Purpose:
# Streamlit Chat Application
# ============================================================

# ============================================================
# Import Libraries
# ============================================================

import streamlit as st

from assistant import ask_assistant

# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="AI Data Engineering Assistant",
    page_icon="🤖",
    layout="wide"
)

# ============================================================
# Title
# ============================================================

st.title("🤖 AI Data Engineering Assistant")

# ============================================================
# Sidebar
# ============================================================

with st.sidebar:

    st.header("🛠️ Features")

    st.markdown("""
- SQL Help
- PySpark
- Databricks
- Spark Optimization
- ETL Design
- Interview Preparation
- Code Generation
""")

    if st.button("🗑️ Clear Chat"):

        st.session_state.history = []

        st.rerun()


st.write(
    """
Ask anything related to:

- PySpark
- SQL
- Databricks
- Delta Lake
- Azure
- ETL
- Spark
- Data Engineering Interviews
"""
)

# ============================================================
# Initialize Chat History
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ============================================================
# Display Previous Messages
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ============================================================
# Chat Input
# ============================================================

question = st.chat_input("Ask a Data Engineering question...")

# ============================================================
# Generate Response
# ============================================================

if question:

    # Store User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Display User Message
    with st.chat_message("user"):
        st.markdown(question)

    # Generate AI Response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = ask_assistant(
                question=question,
                history=st.session_state.messages
            )

            st.markdown(answer)

    # Store Assistant Message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )