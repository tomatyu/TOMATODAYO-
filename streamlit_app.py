import streamlit as st
import random
st.title("おみくじアプリ")
if st.button("おみくじを引く"):
    a = ["大吉","中吉","小吉","吉","凶","大凶"]
    b = random.choice(a)
    st.write(f"結果:{b}")