import streamlit as st
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

st.markdown(
    """
    <h1 style='font-size:20px;'>특정 연령의 인구 비율 분석 (by 서울고 교사 석리송)</h1>
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

# 특정 연령 입력
age = st.number_input('궁금한 연령(만 나이 기준)을 입력하세요:', min_value=0, max_value=100, step=1)

# 지역 이름 선택 및 입력
input_name = st.text_input('궁금한 지역 이름을 입력하거나 선택해주세요:', '')

if age is not None:
    age_index = age + 3  # CSV에서 연령 데이터가 시작되는 열 인덱스 조정
    
    highest_ratio = -1
    lowest_ratio = float('inf')
    highest_region = ""
    lowest_region = ""
    
    filtered_data = data
    if input_name:
        filtered_data = [row for row in data if input_name.lower() in row[0].lower()]

    for row in filtered_data:
        total_population = row[2]
        if total_population == 0:
            continue
        age_population = row[age_index]
        age_ratio = age_population / total_population
        
        if age_ratio > highest_ratio:
            highest_ratio = age_ratio
            highest_region = row[0]
        
        if age_ratio < lowest_ratio:
            lowest_ratio = age_ratio
            lowest_region = row[0]
    
    st.write(f"### 연령 {age}의 비율이 가장 높은 지역: {highest_region} ({highest_ratio*100:.2f}%)")
    st.write(f"### 연령 {age}의 비율이 가장 낮은 지역: {lowest_region} ({lowest_ratio*100:.2f}%)")
    
    highest_pivot = []
    lowest_pivot = []
    for row in data:
        if highest_region in row[0]:
            highest_pivot = [row[i] / row[2] for i in range(3, len(row))]
        if lowest_region in row[0]:
            lowest_pivot = [row[i] / row[2] for i in range(3, len(row))]

    # 시각화
    plt.figure(figsize=(10, 6), dpi=300)
    plt.style.use('ggplot')
    plt.title(f'연령 {age}의 비율이 가장 높은 지역과 낮은 지역의 인구 구조 비교')
    plt.plot(highest_pivot, label=f'{highest_region} (Highest)')
    plt.plot(lowest_pivot, label=f'{lowest_region} (Lowest)')
    plt.xlabel('연령')
    plt.ylabel('비율')
    plt.legend()

    st.pyplot(plt)
