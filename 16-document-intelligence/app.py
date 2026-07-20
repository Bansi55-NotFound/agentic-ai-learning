import os
import streamlit as st

from extractor import extract_text
from analyzer import analyze_document
from qa import answer_question

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Document Intelligence",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Document Intelligence System")

st.write("Upload any PDF document and let AI analyze it.")

# ---------------------------------------------------
# Create uploads folder
# ---------------------------------------------------

os.makedirs("uploads", exist_ok=True)

# ---------------------------------------------------
# Session State
# ---------------------------------------------------

if "document" not in st.session_state:
    st.session_state.document = None

if "analysis" not in st.session_state:
    st.session_state.analysis = None

# ---------------------------------------------------
# Upload PDF
# ---------------------------------------------------

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)

# ---------------------------------------------------
# Process Upload
# ---------------------------------------------------

if uploaded_file is not None:

    file_path = os.path.join("uploads", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ PDF uploaded successfully!")

    if st.button("Analyze Document"):

        with st.spinner("Analyzing..."):

            # Extract only once
            st.session_state.document = extract_text(file_path)

            # Analyze only once
            st.session_state.analysis = analyze_document(
                st.session_state.document
            )

# ---------------------------------------------------
# Display Analysis
# ---------------------------------------------------

if st.session_state.analysis:

    st.markdown("---")
    st.subheader("📑 Document Analysis")

    st.markdown(st.session_state.analysis)

    st.markdown("---")
    st.subheader("💬 Ask Questions About This Document")

    question = st.text_input(
        "Enter your question"
    )

    if st.button("Ask Question"):

        if question.strip():

            with st.spinner("Finding answer..."):

                answer = answer_question(
                    st.session_state.document,
                    question
                )

            st.success("Answer")

            st.write(answer)

        else:
            st.warning("Please enter a question.")