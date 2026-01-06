import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy import sympify, symbols, lambdify

st.set_page_config(page_title="Kalkulator Bisection SPNL", layout="wide")

st.title("🧮 Aplikasi Web Solusi SPNL: Metode Bisection")
st.markdown("""
Aplikasi ini membantu mencari akar persamaan non-linear $f(x) = 0$ menggunakan metode bagi dua (Bisection).
""")

st.sidebar.header("Input Parameter")
fungsi_str = st.sidebar.text_input("Masukkan Fungsi f(x):", value="x^3 - x - 2")
a_input = st.sidebar.number_input("Batas Bawah (a):", value=1.0)
b_input = st.sidebar.number_input("Batas Atas (b):", value=2.0)
tol = st.sidebar.number_input("Toleransi Error:", value=0.001, format="%.4f")
max_iter = st.sidebar.slider("Maksimal Iterasi:", 5, 100, 20)

x_sym = symbols('x')
try:

    expr = sympify(fungsi_str)
    f = lambdify(x_sym, expr, 'numpy')

    if st.sidebar.button("Hitung Sekarang"):

        fa = f(a_input)
        fb = f(b_input)

        if fa * fb >= 0:
            st.error(f"❌ Syarat f(a)*f(b) < 0 tidak terpenuhi! f(a)={fa:.4f}, f(b)={fb:.4f}")
        else:

            data_iterasi = []
            a, b = a_input, b_input
            
            for i in range(1, max_iter + 1):
                c = (a + b) / 2
                fc = f(c)
                error = abs(b - a)
                
                data_iterasi.append({
                    "Iterasi": i,
                    "a": a,
                    "b": b,
                    "c (Tengah)": c,
                    "f(c)": fc,
                    "Error": error
                })

                if abs(fc) < 1e-15 or error < tol:
                    break
                
                if f(a) * fc < 0:
                    b = c
                else:
                    a = c

            df = pd.DataFrame(data_iterasi)
            
            col1, col2 = st.columns([1, 1])

            with col1:
                st.subheader("📊 Hasil Perhitungan")
                st.success(f"Akar ditemukan di **x ≈ {c:.6f}**")
                st.table(df.style.format({"a": "{:.4f}", "b": "{:.4f}", "c (Tengah)": "{:.6f}", "f(c)": "{:.6e}", "Error": "{:.6f}"}))

            with col2:
                st.subheader("📈 Visualisasi Grafik")

                x_vals = np.linspace(a_input - 1, b_input + 1, 400)
                y_vals = f(x_vals)

                fig, ax = plt.subplots()
                ax.plot(x_vals, y_vals, label=f"f(x) = {fungsi_str}", color='blue')
                ax.axhline(0, color='black', lw=1) # Garis x=0
                ax.scatter([c], [f(c)], color='red', label=f'Akar ≈ {c:.4f}')
                ax.set_xlabel("x")
                ax.set_ylabel("f(x)")
                ax.legend()
                ax.grid(True, linestyle='--')
                
                st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan input: {e}")
