import streamlit as st
st.title("MBTI 성향 및 궁합 테스트")

name = st.text_input("이름을 입력하세요:")
mbti = st.selectbox("MBTI 타입을 선택하세요:", ['ENTJ','ISTJ','INTJ'])

if name and mbti:
    st.subheader(f"{name}님의 MBTI 성향")
    st.write(mbti+'스러운 성격입니다')
