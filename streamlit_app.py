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
