import streamlit as st
from scipy.optimize import minimize

def my_function(x):
    return x[0]**2 + x[1]**2

def optimize():
    st.write("Optimization App")
    st.write("----------------")

    x0 = st.number_input("Initial x0 value:", value=0)
    x1 = st.number_input("Initial x1 value:", value=0)
    res = minimize(my_function, [x0, x1])

    st.write("Minimum at:")
    st.write(res.x)

if __name__ == "__main__":
    optimize()

