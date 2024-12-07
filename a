import streamlit as st
import random

# ゲームの選択肢
choices = ['グー', 'チョキ', 'パー']

# コンピュータの手をランダムに選択
def computer_choice():
    return random.choice(choices)

# 勝敗判定
def determine_winner(user, computer):
    if user == computer:
        return '引き分け'
    elif (user == 'グー' and computer == 'チョキ') or \
         (user == 'チョキ' and computer == 'パー') or \
         (user == 'パー' and computer == 'グー'):
        return 'あなたの勝ち'
    else:
        return 'コンピュータの勝ち'

# ストリームリットのUI部分
st.title('じゃんけんゲーム')

# セッションステートの初期化
if 'user_choice' not in st.session_state:
    st.session_state.user_choice = None

# ボタンを使って選択
col1, col2, col3 = st.columns(3)

with col1:
    if st.button('グー'):
        st.session_state.user_choice = 'グー'

with col2:
    if st.button('チョキ'):
        st.session_state.user_choice = 'チョキ'

with col3:
    if st.button('パー'):
        st.session_state.user_choice = 'パー'

# ユーザーが手を選んだ後に即座に結果を表示
if st.session_state.user_choice:
    # コンピュータの選択を取得
    comp_choice = computer_choice()

    # 勝敗判定
    result = determine_winner(st.session_state.user_choice, comp_choice)

    # 結果を表示
    st.write(f'あなたの手: {st.session_state.user_choice}')
    st.write(f'コンピュータの手: {comp_choice}')
    st.write(f'結果: {result}')
