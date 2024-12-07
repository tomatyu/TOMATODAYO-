import streamlit as st

# セッションステートの初期化
if 'history' not in st.session_state:
    st.session_state.history = []

# ユーザーからの入力を取得
prompt = st.chat_input("Say something")

# ユーザーが入力した場合、その内容と応答を保存
if prompt:
    # ユーザーからの発言を履歴に追加
    st.session_state.history.append(f"あなたからの発言: {prompt}")
    # ゴリ押し信者からの応答を履歴に追加
    st.session_state.history.append("ゴリ押し信者からの回答: 力こそpower")

# 履歴を表示
for message in st.session_state.history:
    st.write(message)
