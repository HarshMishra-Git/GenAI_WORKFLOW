import streamlit as st
from utils.document_processor import DocumentProcessor
from utils.vector_store import VectorStore

def render_document_upload():
    """Render the document upload section."""
    st.header("📄 Document Upload")

    uploaded_files = st.file_uploader(
        "Upload your documents",
        type=["txt", "pdf"],
        accept_multiple_files=True,
        help="Upload text or PDF files for processing"
    )

    if uploaded_files:
        with st.spinner("Processing documents..."):
            try:
                processor = DocumentProcessor()
                vectorstore = VectorStore()

                for file in uploaded_files:
                    documents = processor.process_file(file)
                    vectorstore.add_documents(documents)

                st.session_state.vectorstore = vectorstore
                st.success(f"Successfully processed {len(uploaded_files)} documents!")

            except Exception as e:
                st.error(f"Error processing documents: {str(e)}")

__all__ = ['render_document_upload']