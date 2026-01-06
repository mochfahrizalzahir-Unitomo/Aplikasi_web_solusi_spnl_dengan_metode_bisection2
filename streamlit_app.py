import streamlit as st
from sympy import sympify, symbols, lambdify

st.title("Tahap 1: Input & Parsing")

fungsi_str = st.sidebar.text_input("Masukkan Fungsi f(x):", value="x^3 - x - 2")
x_sym = symbols('x')

try:
    expr = sympify(fungsi_str)
    f = lambdify(x_sym, expr, 'numpy')
    
    st.write(f"Fungsi yang terdeteksi: **f(x) = {expr}**")
    test_val = st.number_input("Coba masukkan nilai x untuk cek f(x):", value=1.0)
    st.write(f"Hasil f({test_val}) = {f(test_val)}")
except Exception as e:
    st.error(f"Input error: {e}")
