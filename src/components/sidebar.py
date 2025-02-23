import streamlit as st
import os
import pandas as pd

def render_sidebar():
    """Render the sidebar with configuration options."""
    st.sidebar.title("⚙️ Configuration")
    
    st.sidebar.markdown("""
    Configure your workflow settings below to optimize the system's performance 
    for your specific needs.
    """)
    
    st.sidebar.header("📚 RAG Settings")
    st.sidebar.markdown("*Control how documents are retrieved and processed*")
    st.sidebar.slider(
        "Number of chunks to retrieve",
        min_value=1,
        max_value=10,
        value=5,
        key="k_documents"
    )
    
    st.sidebar.header("AI Agent Settings")
    st.sidebar.selectbox(
        "Response Type",
        ["Detailed", "Concise", "Technical"],
        key="response_type"
    )
    
    st.sidebar.header("Export Settings")
    export_format = st.sidebar.selectbox(
        "Export Format",
        ["CSV", "JSON", "Excel"],
        key="export_format"
    )
    
    if st.sidebar.button("Export Results"):
        if len(st.session_state.get("results", [])) > 0:
            try:
                export_dir = "exports"
                if not os.path.exists(export_dir):
                    os.makedirs(export_dir)
                
                df = pd.DataFrame(st.session_state.results)
                filename = f"exports/results.{export_format.lower()}"
                
                if export_format == "CSV":
                    df.to_csv(filename, index=False)
                elif export_format == "JSON":
                    df.to_json(filename)
                else:  # Excel
                    df.to_excel(filename, index=False)
                    
                st.sidebar.success(f"Results exported to {filename}!")
            except Exception as e:
                st.sidebar.error(f"Export failed: {str(e)}")
        else:
            st.sidebar.warning("No results to export!")
