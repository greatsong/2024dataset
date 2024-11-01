<<<<<<< HEAD
import streamlit as st
import random

=======
>>>>>>> parent of ead6259 (Update test.py)
st.title("MBTI 성향 및 궁합 테스트")
st.header("당신의 성격과 완벽한 궁합을 찾으세요!")

name = st.text_input("이름을 입력하세요:")
mbti = st.selectbox("MBTI 타입을 선택하세요:", ['ENTJ', 'ISTJ', 'INTJ', 'ENFP', 'INFJ', 'ISFP', 'ESTP'])

# 궁합 데이터베이스 (간단한 재미 요소)
mbti_matches = {
    'ENTJ': 'INTP',
    'ISTJ': 'ESFP',
    'INTJ': 'ENFP',
    'ENFP': 'INTJ',
    'INFJ': 'ENFJ',
    'ISFP': 'ESTJ',
    'ESTP': 'ISFJ'
}

fun_traits = [
    "대단히 창의적이에요!",
    "분석적 사고의 달인입니다!",
    "리더십이 넘치는 성격이에요!",
    "항상 새로운 모험을 추구해요!"
]

if name and mbti:
    st.subheader(f"{name}님의 MBTI 성향")
    st.write(f"{mbti}스러운 성격입니다. {random.choice(fun_traits)}")

    # 궁합 정보 제공
    best_match = mbti_matches.get(mbti, "모두와 잘 어울려요!")
    st.subheader("궁합 테스트 결과")
    st.write(f"{name}님과 가장 잘 어울리는 MBTI 타입은 **{best_match}**입니다.")
    
    st.balloons()  # 결과가 나올 때 재미 요소로 풍선 효과 추가
