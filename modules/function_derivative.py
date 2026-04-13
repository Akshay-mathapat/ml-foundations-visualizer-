import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def run():
    st.markdown('<div class="glass fade-in">', unsafe_allow_html=True)

    st.header("📉 Function & Derivative Visualizer")

    x = sp.symbols('x')

    expr_input = st.text_input("Enter function", "x**2")

    try:
        expr = sp.sympify(expr_input)
        derivative = sp.diff(expr, x)

        # Display formulas
        st.latex(f"f(x) = {sp.latex(expr)}")
        st.latex(f"f'(x) = {sp.latex(derivative)}")

        f = sp.lambdify(x, expr, "numpy")
        df = sp.lambdify(x, derivative, "numpy")

        xs = np.linspace(-10, 10, 200)

        fig, ax = plt.subplots()
        ax.plot(xs, f(xs), label="f(x)")
        ax.plot(xs, df(xs), label="f'(x)")
        ax.legend()
        ax.set_title("Function & Derivative")

        st.pyplot(fig)

    except:
        st.error("⚠️ Invalid function input (example: x**2 + 3*x)")

    st.markdown('</div>', unsafe_allow_html=True)