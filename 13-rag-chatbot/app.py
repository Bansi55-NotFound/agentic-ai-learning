# ----------------------------------------------------
# Import required libraries
# ----------------------------------------------------
import streamlit as st

from rag import ask_question

# ----------------------------------------------------
# Configure the Streamlit page
# ----------------------------------------------------
st.set_page_config(
    page_title="Employee Handbook Chatbot",
    page_icon="🤖"
)

# ----------------------------------------------------
# Page Title
# ----------------------------------------------------
st.title("🤖 Employee Handbook Chatbot")

st.write(
    "Ask questions about the Employee Handbook."
)

# ----------------------------------------------------
# Text input for user question
# ----------------------------------------------------
question = st.text_input(
    "Ask your question:"
)

# ----------------------------------------------------
# Generate answer when button is clicked
# ----------------------------------------------------
if st.button("Ask"):

    if question.strip():

        with st.spinner("Searching handbook..."):

            answer = ask_question(question)

        st.success(answer)

    else:

        st.warning("Please enter a question.")