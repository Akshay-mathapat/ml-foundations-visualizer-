import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

def function(x):
    return x**2

def derivative(x):
    return 2*x

def run():
    st.markdown('<div class="glass fade-in">', unsafe_allow_html=True)

    st.header("📊 Gradient Descent Simulation")

    col1, col2, col3 = st.columns(3)

    with col1:
        lr = st.slider("Learning Rate", 0.001, 1.0, 0.1)

    with col2:
        iterations = st.slider("Iterations", 1, 100, 20)

    with col3:
        x = st.number_input("Starting Point", value=5.0)

    run_btn = st.button("🚀 Start Optimization")

    if run_btn:
        xs, ys = [], []

        plot_placeholder = st.empty()
        loss_placeholder = st.empty()

        for i in range(iterations):
            xs.append(x)
            y = function(x)
            ys.append(y)

            x = x - lr * derivative(x)

            # Function plot
            X = np.linspace(-10, 10, 100)
            Y = function(X)

            fig, ax = plt.subplots()
            ax.plot(X, Y)
            ax.scatter(xs, ys)
            ax.plot(xs, ys, linestyle="--")
            ax.set_title(f"Step {i+1}")

            plot_placeholder.pyplot(fig)

            # Loss plot
            fig2, ax2 = plt.subplots()
            ax2.plot(range(len(ys)), ys)
            ax2.set_title("Loss vs Iterations")

            loss_placeholder.pyplot(fig2)

            time.sleep(0.2)

        st.success("✅ Optimization Complete")

        c1, c2 = st.columns(2)
        c1.metric("Final x", f"{x:.4f}")
        c2.metric("Final Loss", f"{function(x):.4f}")

    st.markdown('</div>', unsafe_allow_html=True)