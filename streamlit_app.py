import streamlit as st
import time

# 初期化: session_stateに数字が保存されていない場合、初期値を設定
if 'number' not in st.session_state:
    st.session_state.number = 1  # 初期値を1に設定

# ユーザーからの入力を受け取る
user_input = st.number_input("数字を入力してください:", min_value=1, value=max(st.session_state.number, 1))

# 数字が変更された場合、その値をセッション状態に保存
if user_input != st.session_state.number:
    st.session_state.number = user_input

# 数字を表示するためのエリアを作成
display_area = st.empty()

# 数字を永遠に2倍して1行に表示
while True:
    # 表示エリアを更新
    display_area.write(f"現在の数字: {st.session_state.number}")
    
    # 数字を2倍にする
    st.session_state.number *= 2
    
    # 1秒間待機
    time.sleep(1)
