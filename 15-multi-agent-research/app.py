# ============================================================
# Project 15 - Multi-Agent Research Assistant
#
# File: app.py
#
# Purpose:
# Streamlit UI for generating research reports using
# multiple AI agents.
# ============================================================

import streamlit as st

from workflow import graph


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Multi-Agent Research Assistant")

st.write(
    """
Enter any research topic.

The AI workflow will:

🧠 Plan the research

✍️ Write the report

✅ Review and improve it
"""
)


# ============================================================
# User Input
# ============================================================

topic = st.text_input(
    "Research Topic"
)


# ============================================================
# Generate Report
# ============================================================

if st.button("Generate Report"):

    if topic.strip():

        with st.spinner("Generating report..."):

            result = graph.invoke(
                {
                    "topic": topic
                }
            )

        st.success("Report Generated Successfully!")

        st.markdown("---")

        st.subheader("📄 Final Report")

        st.write(result["final_report"])

    else:

        st.warning("Please enter a research topic.")