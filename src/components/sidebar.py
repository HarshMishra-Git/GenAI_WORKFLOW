import streamlit as st

def render_sidebar():
    """Render the sidebar with configuration options."""
    st.sidebar.title("⚙️ Configuration")
    
    st.sidebar.header("RAG Settings")
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
            # Add export logic here
            st.sidebar.success("Results exported successfully!")
        else:
            st.sidebar.warning("No results to export!")
