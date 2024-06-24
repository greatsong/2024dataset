import streamlit as st
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

st.markdown(
    """
    <h1 style='font-size:20px;'>수도권 교통 카드 데이터 분석 프로젝트(by 서울고 교사 석리송 with GPT-4o)</h1>
    """, 
    unsafe_allow_html=True
)

# CSV 파일 읽기
@st.cache
def load_data(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        data = list(csv.reader(f))
    return data

data = load_data('age.csv')
header = data[0]
data = data[1:]

# 데이터 전처리
for row in data:
    for i in range(1, len(row)):
        row[i] = int(row[i])

# 지역 이름 목록 생성
region_names = [row[0] for row in data]

# Streamlit 앱 제목
st.title('우리 동네와 가장 비슷한 지역은 어디일까?(by 서울고 교사 석리송)')

# 지역 이름 선택 및 입력
input_name = st.text_input('궁금한 지역 이름을 입력하거나 선택해주세요:', '')

if input_name:
    # 입력된 텍스트에 따라 자동완성 기능 제공
    matching_names = [name for name in region_names if input_name.lower() in name.lower()]
    if matching_names:
        selected_name = st.selectbox('자동완성된 지역 목록에서 선택하세요:', matching_names)
    else:
        selected_name = input_name
else:
    selected_name = st.selectbox('지역 이름을 선택하세요:', region_names)

if selected_name:
    pivot = []
    for row in data:
        if selected_name in row[0]:
            for i in range(3, len(row)):
                pivot.append(row[i] / row[2])
            break

    mn = 1
    result = []
    result_name = ""

    for row in data:
        if row[2] == 0:
            continue
        s = 0
        for i in range(3, len(row)):
            tmp = row[i] / row[2] - pivot[i - 3]
            s = s + tmp ** 2
        if s < mn and (selected_name not in row[0]):
            mn = s
            result = []
            for i in range(3, len(row)):
                result.append(row[i] / row[2])
            result_name = row[0]

    # 시각화
    plt.figure(dpi=300)
    plt.style.use('ggplot')
    plt.title(selected_name + ' 지역과 인구 구조가 가장 비슷한 지역')
    plt.plot(pivot, label=selected_name)
    plt.plot(result, label=result_name)
    plt.legend()

    st.pyplot(plt)
