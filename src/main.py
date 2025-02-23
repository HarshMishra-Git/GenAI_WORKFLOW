import streamlit as st
from components.sidebar import render_sidebar
from components.document_upload import render_document_upload
from components.query_interface import render_query_interface
from components.visualization import render_visualization
import os

def init_session_state():
    if 'documents' not in st.session_state:
        st.session_state.documents = []
    if 'vectorstore' not in st.session_state:
        st.session_state.vectorstore = None
    if 'current_query' not in st.session_state:
        st.session_state.current_query = ""
    if 'results' not in st.session_state:
        st.session_state.results = []

def main():
    st.set_page_config(
        page_title="GenAI Workflow System",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    init_session_state()

    st.title("🤖 GenAI Workflow System")
    st.markdown("""
    Welcome to the GenAI Workflow System! This application helps you process documents,
    generate insights, and interact with AI agents using RAG capabilities.
    """)

    # Render sidebar
    render_sidebar()

    # Main content area
    col1, col2 = st.columns([1, 1])

    with col1:
        render_document_upload()
        render_query_interface()

    with col2:
        render_visualization()

if __name__ == "__main__":
    main()
