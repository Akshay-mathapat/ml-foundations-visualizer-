import streamlit as st
from styles import load_css
import sys
import os

# Fix import path (IMPORTANT)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# Page config
st.set_page_config(
    page_title="ML Foundations Visualizer",
    page_icon="📊",
    layout="wide"
)

# Theme toggle
theme = st.sidebar.toggle("🌙 Dark Mode", value=True)

# Apply CSS
if theme:
    st.markdown(load_css(), unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    .stApp {
        background: #f5f5f5;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("""
<div class="fade-in">
    <h1 style='text-align: center;'>📊 ML Foundations Visualizer</h1>
    <p style='text-align: center; font-size:18px;'>
        Explore core Machine Learning concepts interactively 🚀
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## 🚀 Navigation")

menu = st.sidebar.radio(
    "Choose Module",
    [
        "🔢 Vector Similarity",
        "📉 Function & Derivative",
        "📊 Gradient Descent"
    ]
)

st.markdown("---")

# ✅ SAFE IMPORT METHOD (NO ERRORS)
try:
    from modules import vector_similarity, function_derivative, gradient_descent
except Exception as e:
    st.error(f"Import Error: {e}")
    st.stop()

# Load modules
if menu == "🔢 Vector Similarity":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    vector_similarity.run()
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "📉 Function & Derivative":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    function_derivative.run()
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "📊 Gradient Descent":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    gradient_descent.run()
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<hr>
<p style='text-align:center;'>
    Built with ❤️ using Streamlit | ML Foundations Visualizer
</p>
""", unsafe_allow_html=True)