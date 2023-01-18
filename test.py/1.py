import streamlit as st
from scipy.optimize import minimize

def rosen(x):
    """ローゼンブロック関数"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

st.title("ローゼンブロック関数最適化")

# ユーザーからの入力を取得
x0 = st.number_input("初期x値を入力してください:")
y0 = st.number_input("初期y値を入力してください:")

# 最適化を実行
res = minimize(rosen, [x0, y0])

st.write("最適化結果:")
st.write("x =", res.x[0])
st.write("y =", res.x[1])
