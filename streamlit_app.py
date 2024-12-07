import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"あなたからの発言: {prompt}")
if prompt:
    st.write(f"トマト信者からの回答:トマトは最高にうまい")