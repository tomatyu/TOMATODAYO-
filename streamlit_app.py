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

# ユーザーに手を選ばせる
user_choice = st.radio('あなたの手を選んでください:', choices)

# ユーザーが手を選んだ後に即座に結果を表示
if user_choice:
    # コンピュータの選択を取得
    comp_choice = computer_choice()

    # 勝敗判定
    result = determine_winner(user_choice, comp_choice)

    # 結果を表示
    st.write(f'あなたの手: {user_choice}')
    st.write(f'コンピュータの手: {comp_choice}')
    st.write(f'結果: {result}')
