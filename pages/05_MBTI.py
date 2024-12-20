import streamlit as st

st.title("MBTI 성향 및 진로/궁합 테스트")
st.header("MBTI 전문가의 구체적 설명 및 진로 가이드")

# 사용자 입력 받기
name = st.text_input("이름을 입력하세요:")
mbti = st.selectbox("MBTI 타입을 선택하세요:", [
    'ENTJ', 'ISTJ', 'INTJ', 'ENFP', 'INFJ', 'ISFP', 'ESTP', 'ESFJ', 'INFP', 'ENTP', 'ISFJ', 'ESTJ', 'ENFJ', 'ISTP', 'INTP', 'ESFP'
])

# 성향, 진로 및 궁합 설명 데이터
mbti_descriptions = {
    'ENTJ': {
        'description': "🧠 강력한 리더십과 전략적 사고가 특징입니다. 계획 수립과 목표 달성에 집중하며, 문제 해결에 능숙합니다.",
        'career_advice': "📈 관리직, 경영 컨설팅, 프로젝트 매니저, 기업가 같은 직업에서 두각을 나타낼 수 있습니다. 자신의 리더십과 조직 능력을 활용할 수 있는 환경이 적합합니다.",
        'best_match': "INTP와의 궁합이 최고의 시너지를 냅니다. 🧩 창의적인 아이디어와 체계적인 계획을 결합할 수 있습니다."
    },
    'ISTJ': {
        'description': "📊 철저한 분석과 높은 신뢰성을 가지고 있으며, 실용적이고 계획적인 성향이 강합니다. 안정성과 정확성을 중시합니다.",
        'career_advice': "💼 회계사, 관리자, 법률 전문가, 공무원 등 세부 사항과 규칙을 준수하는 직업이 적합합니다. 명확한 지침과 구조가 있는 직무에서 잘 작동합니다.",
        'best_match': "ESFP와 가장 잘 어울립니다. 🤝 ISTJ의 안정성과 ESFP의 활발함이 균형을 이룹니다."
    },
    'INTJ': {
        'description': "🔍 통찰력과 분석력이 뛰어나며, 혁신적인 아이디어를 추진하는 전략가입니다. 독립적이고 논리적 사고를 갖추고 있습니다.",
        'career_advice': "🧪 과학자, 연구원, 전략 컨설턴트, IT 전문가 등 분석적이고 창의적인 문제 해결을 요구하는 직무에 적합합니다.",
        'best_match': "ENFP와의 궁합이 매우 이상적입니다. 🌈 서로 다른 성향이지만 상호 보완적입니다."
    },
    'ENFP': {
        'description': "🌟 창의적이고 활발하며, 새로운 아이디어에 열려 있습니다. 인간관계에서 따뜻함을 나타내며 주변 사람들에게 영감을 줍니다.",
        'career_advice': "🎨 마케팅 전문가, 이벤트 플래너, 작가, 예술가 등 사람들과의 상호작용이 많은 직업에 적합합니다. 자유로운 환경이 중요합니다.",
        'best_match': "INTJ와의 조화가 뛰어납니다. 🧠 ENFP의 감성과 INTJ의 논리적 사고가 완벽하게 결합됩니다."
    },
    'INFJ': {
        'description': "💖 높은 직관력과 깊은 공감을 통해 타인의 감정을 잘 이해합니다. 다른 사람을 돕고자 하는 마음이 강합니다.",
        'career_advice': "📝 상담사, 심리학자, 사회복지사, 작가 등 타인의 발전을 돕는 직업이 적합합니다. 깊은 관계와 의미를 중시합니다.",
        'best_match': "ENFJ와 좋은 조화를 이룹니다. 🤗 둘 다 인간 중심적이며, 서로의 가치관을 잘 이해합니다."
    },
    'ISFP': {
        'description': "🎨 예술적인 성향을 가지고 있으며, 즉흥적이고 감각적입니다. 자유로운 환경에서 자신의 감정을 표현하는 것을 좋아합니다.",
        'career_advice': "🎸 디자이너, 음악가, 사진작가, 예술가 등 창의적이며 개인 표현이 중요한 직무에서 두각을 나타냅니다.",
        'best_match': "ESTJ와 잘 맞습니다. 🔗 ESTJ의 구조화된 접근 방식이 ISFP의 창의성을 보완합니다."
    },
    'ESTP': {
        'description': "⚡ 에너지 넘치고 활동적인 성격으로, 현실적인 문제 해결 능력이 탁월합니다. 모험을 즐기며 대담한 성향을 보입니다.",
        'career_advice': "🏃‍♂️ 판매원, 기업가, 스포츠 코치, 리스크 매니저 등 빠르게 변하는 환경에서 문제를 해결하는 직무에 적합합니다.",
        'best_match': "ISFJ와의 관계가 이상적입니다. 🤝 ESTP의 활발함과 ISFJ의 헌신이 균형을 이룹니다."
    },
    'ESFJ': {
        'description': "🤗 친근하고 타인의 필요를 잘 이해하며 협력을 중시합니다. 안정적이고 따뜻한 리더십을 보입니다.",
        'career_advice': "👩‍🏫 교사, 간호사, 인사 담당자 등 사람과의 소통과 협력이 중요한 직업에 적합합니다.",
        'best_match': "ISFP와 잘 어울립니다. 🎨 서로의 감정과 가치를 잘 이해할 수 있습니다."
    },
    'INFP': {
        'description': "🌱 이상적인 세상을 꿈꾸며, 창의적이고 개방적인 사고를 합니다. 내면의 가치를 중요하게 생각합니다.",
        'career_advice': "🖋️ 작가, 예술가, 상담사, 인권운동가 등 자신의 가치와 신념을 표현할 수 있는 직무가 적합합니다.",
        'best_match': "ENFJ와 좋은 조화를 이룹니다. 🤝 서로의 감정과 깊은 생각을 공유할 수 있습니다."
    },
    'ENTP': {
        'description': "💡 창의적이고 논쟁을 즐기며, 새로운 아이디어에 도전하는 것을 좋아합니다. 전략적 사고를 잘합니다.",
        'career_advice': "🌐 창업가, 광고 기획자, 마케팅 전문가 등 빠르게 변하는 환경에서 혁신을 이끌어낼 수 있는 직무가 적합합니다.",
        'best_match': "INFJ와 좋은 조화를 이룹니다. 💖 서로의 차이점을 통해 배울 수 있습니다."
    },
    'ISFJ': {
        'description': "🛡️ 헌신적이며 타인을 돕는 것을 즐깁니다. 세심하고 책임감이 강하며 전통적인 가치를 존중합니다.",
        'career_advice': "👨‍⚕️ 간호사, 교사, 관리자 등 타인을 돕고 안정된 환경에서 일할 수 있는 직업에 적합합니다.",
        'best_match': "ESTP와의 관계가 이상적입니다. ⚡ 서로의 장점을 보완할 수 있습니다."
    },
    'ESTJ': {
        'description': "🏗️ 실용적이고 조직적인 성향이 있으며, 효율적인 계획과 실행을 중시합니다. 강한 리더십을 발휘합니다.",
        'career_advice': "🛠️ 관리자, 군인, 사업가 등 체계적이고 책임감이 필요한 직무가 적합합니다.",
        'best_match': "ISFP와 잘 맞습니다. 🎨 서로의 다른 성향이 좋은 균형을 이룹니다."
    },
    'ENFJ': {
        'description': "🌍 따뜻하고 카리스마 넘치는 리더입니다. 타인의 성장과 협력을 이끌어내며 감정적 지지가 뛰어납니다.",
        'career_advice': "🎤 상담사, 강사, 사회복지사 등 사람을 돕고 영감을 주는 직업이 적합합니다.",
        'best_match': "INFP와 잘 어울립니다. 🌱 서로의 감정을 이해하고 배려할 수 있습니다."
    },
    'ISTP': {
        'description': "🔧 실용적이고 논리적인 성향으로 문제 해결을 즐깁니다. 조용하지만 도전적인 일을 선호합니다.",
        'career_advice': "🔨 엔지니어, 기술자, 파일럿 등 손과 머리를 동시에 쓰는 직무에 적합합니다.",
        'best_match': "ESTJ와의 조화가 뛰어납니다. 🏗️ 서로의 기술적 접근과 조직력이 균형을 이룹니다."
    },
    'INTP': {
        'description': "🧩 지적 호기심이 많고 논리적 사고를 즐깁니다. 복잡한 문제 해결에 몰두하며 독립적입니다.",
        'career_advice': "🖥️ 개발자, 데이터 분석가, 학자 등 분석적이고 깊이 있는 사고를 요구하는 직무에 적합합니다.",
        'best_match': "ENTJ와 좋은 궁합을 가집니다. 🧠 전략적 사고와 창의성을 결합할 수 있습니다."
    },
    'ESFP': {
        'description': "🎉 활발하고 사교적이며, 타인과의 교류에서 에너지를 얻습니다. 순간을 즐기고 따뜻한 마음을 가지고 있습니다.",
        'career_advice': "🎭 배우, 이벤트 플래너, 여행 가이드 등 사람들과 교류하고 즐거움을 주는 직업이 적합합니다.",
        'best_match': "ISTJ와 잘 어울립니다. 📊 ISTJ의 안정성과 ESFP의 활발함이 좋은 균형을 만듭니다."
    }
}

if st.button("확인✅") and name and mbti:
    st.subheader(f"{name}님의 MBTI 성향")
    mbti_info = mbti_descriptions.get(mbti, None)
    
    if mbti_info:
        st.write(f"{name}님은 {mbti_info['description']}")
        st.write(f"**진로 참고점:** {mbti_info['career_advice']}")
        st.subheader("궁합 테스트 결과")
        st.write(f"{name}님과 가장 잘 어울리는 MBTI 타입은 **{mbti_info['best_match']}**입니다.")
    else:
        st.write("해당 MBTI에 대한 설명이 아직 준비되지 않았습니다.")
    
    st.info("이 테스트는 일반적인 MBTI 해석을 기반으로 제공되며, 개인의 고유한 성격과 경험에 따라 결과가 다를 수 있습니다.")
    st.balloons()  # 결과가 나올 때 재미 요소로 풍선 효과 추가
