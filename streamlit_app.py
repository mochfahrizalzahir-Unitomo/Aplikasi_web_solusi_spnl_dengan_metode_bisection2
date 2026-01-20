import streamlit as st
from sympy import sympify, symbols, lambdify

st.title("Input & Parsing")

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
a = st.sidebar.number_input("Batas Bawah (a):", value=1.0)
b = st.sidebar.number_input("Batas Atas (b):", value=2.0)

if st.sidebar.button("Jalankan Bisection"):
    fa, fb = f(a), f(b)
    
    if fa * fb >= 0:
        st.error("Syarat f(a)*f(b) < 0 tidak terpenuhi. Akar mungkin tidak ada di rentang ini.")
    else:
        c = (a + b) / 2
        st.success(f"Iterasi 1 berhasil: Titik tengah awal adalah {c}")
        import pandas as pd

data_iterasi = []
tol = 0.001
for i in range(1, 11): 
    c = (a + b) / 2
    fc = f(c)
    data_iterasi.append({"Iterasi": i, "a": a, "b": b, "c": c, "f(c)": fc})
    
    if abs(fc) < 1e-15 or abs(b-a) < tol:
        break
    if f(a) * fc < 0:
        b = c
    else:
        a = c

df = pd.DataFrame(data_iterasi)
st.table(df)
import matplotlib.pyplot as plt
import numpy as np

st.subheader("Visualisasi Grafik")
x_vals = np.linspace(a - 1, b + 1, 100)
y_vals = f(x_vals)

fig, ax = plt.subplots()
ax.plot(x_vals, y_vals, label="f(x)")
ax.axhline(0, color='black', linewidth=1) # Garis x=0
ax.scatter([c], [f(c)], color='red', label='Akar') # Titik Akar
ax.legend()
st.pyplot(fig)
