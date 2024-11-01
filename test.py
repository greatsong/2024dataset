import streamlit as st

# 제목
st.title("MBTI 성향 및 궁합 테스트")

# 사이드바에 설명 추가
st.sidebar.header("MBTI 테스트에 대해")
st.sidebar.write("이 앱은 간단한 MBTI 성향 테스트 및 결과를 보여줍니다.")

# 사용자 입력
name = st.text_input("이름을 입력하세요:")
mbti = st.selectbox("MBTI 타입을 선택하세요:", ['ENTJ', 'ISTJ', 'INTJ', 'ENFP', 'INFJ'])

# 버튼으로 결과 표시
if st.button("결과 보기") and name and mbti:
    st.subheader(f"{name}님의 MBTI 성향")
    st.write(mbti + '스러운 성격입니다')

    # MBTI별 추가 설명
    if mbti == 'ENTJ':
        st.success("리더십과 전략적 사고에 강한 타입입니다.")
    elif mbti == 'ISTJ':
        st.info("실용적이며 책임감이 높은 성격입니다.")
    elif mbti == 'INTJ':
        st.warning("창의적이면서도 분석적인 성향을 가졌습니다.")
    elif mbti == 'ENFP':
        st.error("창의적이고 활발하며 열정이 넘치는 성격입니다.")
    elif mbti == 'INFJ':
        st.markdown("_이해심 깊고 통찰력이 뛰어납니다._")

# 이미지 표시 (선택적)
# 이미지 파일이 있다면 경로를 지정해 표시할 수 있습니다.
# st.image('path/to/image.jpg', caption='MBTI 이미지')
