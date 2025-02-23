import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

def create_confidence_gauge(confidence_score):
    """Create a gauge chart for confidence score."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=confidence_score * 100,
        title={'text': "Confidence Score"},
        gauge={'axis': {'range': [0, 100]},
               'bar': {'color': "darkblue"},
               'steps': [
                   {'range': [0, 33], 'color': "lightgray"},
                   {'range': [33, 66], 'color': "gray"},
                   {'range': [66, 100], 'color': "darkgray"}
               ]}
    ))
    return fig

def create_results_timeline(results):
    """Create a timeline of results."""
    df = pd.DataFrame(results)
    fig = px.line(df, title="Results Timeline")
    return fig

def render_visualization():
    """Render the visualization section."""
    st.header("📊 Results & Visualization")
    
    results = st.session_state.get("results", [])
    
    if not results:
        st.info("No results to display. Try processing a query first!")
        return
    
    # Display latest result
    st.subheader("Latest Result")
    latest_result = results[-1]
    
    # Display answer
    st.markdown("### Answer")
    st.write(latest_result["answer"])
    
    # Display context
    st.markdown("### Context")
    for idx, ctx in enumerate(latest_result["context"]):
        with st.expander(f"Context {idx + 1}"):
            st.write(ctx["content"])
            st.metric("Relevance Score", f"{(1 - ctx['score']) * 100:.2f}%")
    
    # Visualizations
    st.markdown("### Visualizations")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Create and display confidence gauge
        confidence_score = 0.85  # This should come from the AI agent
        fig_gauge = create_confidence_gauge(confidence_score)
        st.plotly_chart(fig_gauge, use_container_width=True)
    
    with col2:
        # Create and display results timeline
        fig_timeline = create_results_timeline(results)
        st.plotly_chart(fig_timeline, use_container_width=True)
