import streamlit as st
import time

# 初期化: session_stateに数字が保存されていない場合、初期値を設定
if 'number' not in st.session_state:
    st.session_state.number = 1  # 初期値として1を設定

# ユーザーからの数字入力を受け取る
user_input = st.number_input("数字を入力してください:", min_value=1, value=st.session_state.number)

# 数字が変更された場合、その値をセッション状態に保存
if user_input != st.session_state.number:
    st.session_state.number = user_input

# 数字を永遠に2倍して表示
while True:
    st.write(f"現在の数字: {st.session_state.number}")
    st.session_state.number *= 2
    time.sleep(1)  # 1秒待機
