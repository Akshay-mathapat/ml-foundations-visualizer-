import streamlit as st
import numpy as np
import plotly.graph_objects as go

def run():
    st.markdown('<div class="glass fade-in">', unsafe_allow_html=True)

    st.header("🔢 Vector Similarity")

    col1, col2 = st.columns(2)

    with col1:
        v1_input = st.text_input("Vector A", "1,2")

    with col2:
        v2_input = st.text_input("Vector B", "2,3")

    try:
        v1 = np.array([float(x) for x in v1_input.split(",")])
        v2 = np.array([float(x) for x in v2_input.split(",")])

        # Calculations
        dot = np.dot(v1, v2)
        cosine = dot / (np.linalg.norm(v1) * np.linalg.norm(v2))
        dist = np.linalg.norm(v1 - v2)
        angle = np.degrees(np.arccos(cosine))

        # Metrics
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Dot Product", f"{dot:.2f}")
        m2.metric("Cosine Similarity", f"{cosine:.3f}")
        m3.metric("Distance", f"{dist:.3f}")
        m4.metric("Angle (°)", f"{angle:.2f}")

        # Plot
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=[0, v1[0]], y=[0, v1[1]],
            mode='lines+markers', name='Vector A'
        ))

        fig.add_trace(go.Scatter(
            x=[0, v2[0]], y=[0, v2[1]],
            mode='lines+markers', name='Vector B'
        ))

        st.plotly_chart(fig, use_container_width=True)

    except:
        st.error("⚠️ Please enter valid numeric vectors (e.g., 1,2)")

    st.markdown('</div>', unsafe_allow_html=True)