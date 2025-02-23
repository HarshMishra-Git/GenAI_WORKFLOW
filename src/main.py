import streamlit as st
import os
from components.sidebar import render_sidebar
from components.document_upload import render_document_upload
from components.query_interface import render_query_interface
from components.visualization import render_visualization

def init_session_state():
    """Initialize session state variables."""
    if 'documents' not in st.session_state:
        st.session_state.documents = []
    if 'vectorstore' not in st.session_state:
        st.session_state.vectorstore = None
    if 'current_query' not in st.session_state:
        st.session_state.current_query = ""
    if 'results' not in st.session_state:
        st.session_state.results = []

def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(
        page_title="GenAI Workflow System",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    init_session_state()

    # Theme selector
    theme = st.sidebar.radio(
        "Theme",
        ["Light", "Dark", "System"],
        key="theme"
    )
    
    if theme == "Dark":
        st.markdown("""
            <style>
                [data-testid="stAppViewContainer"] {
                    background-color: #1E1E1E;
                    color: #FFFFFF;
                }
            </style>
        """, unsafe_allow_html=True)
    elif theme == "Light":
        st.markdown("""
            <style>
                [data-testid="stAppViewContainer"] {
                    background-color: #FFFFFF;
                    color: #000000;
                }
            </style>
        """, unsafe_allow_html=True)

    st.title("🤖 GenAI Workflow System")
    st.markdown("""
    ## About This Project
    
    The GenAI Workflow System is an advanced document processing and question-answering platform that leverages RAG (Retrieval-Augmented Generation) and AI capabilities to help you extract insights from your documents.
    
    ### Why Use This Project?
    - 📚 **Document Processing**: Easily upload and process multiple documents
    - 🔍 **Smart Search**: Uses RAG to find relevant information from your documents
    - 🤖 **AI-Powered Answers**: Get intelligent responses based on your document context
    - 📊 **Visual Analytics**: View confidence scores and result timelines
    - 📤 **Export Capability**: Export results in various formats (CSV, JSON, Excel)
    
    ### How to Use:
    1. **Upload Documents**: Start by uploading your text or PDF files
    2. **Configure Settings**: Adjust RAG and AI settings in the sidebar
    3. **Ask Questions**: Enter your queries in the Query Interface
    4. **Analyze Results**: View answers, context, and visualizations
    5. **Export Data**: Export your results using the sidebar option
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