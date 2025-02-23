import streamlit as st
from utils.ai_agent import AIAgent

def render_query_interface():
    """Render the query interface section."""
    st.header("🔍 Query Interface")
    
    query = st.text_area(
        "Enter your query",
        key="query_input",
        help="Enter your question or query here"
    )
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("Process Query", key="process_query"):
            if not query:
                st.warning("Please enter a query!")
                return
                
            if not st.session_state.get("vectorstore"):
                st.warning("Please upload documents first!")
                return
                
            with st.spinner("Processing query..."):
                try:
                    # Retrieve relevant documents
                    context = st.session_state.vectorstore.search(
                        query,
                        k=st.session_state.k_documents
                    )
                    
                    # Process with AI agent
                    agent = AIAgent()
                    result = agent.process_query(query, context)
                    
                    st.session_state.results.append(result)
                    st.success("Query processed successfully!")
                    
                except Exception as e:
                    st.error(f"Error processing query: {str(e)}")
    
    with col2:
        if st.button("Clear Results", key="clear_results"):
            st.session_state.results = []
            st.success("Results cleared!")
