import streamlit as st
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
import os

st.markdown(
    """
    <h1 style='font-size:20px;'>우리 동네와 가장 비슷한 지역은 어디일까?(by 서울고 교사 석리송)</h1>
    """, 
    unsafe_allow_html=True
)

# CSV 파일 읽기
st.cache_data
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


# 지역 이름 선택 및 입력
selected_name = st.selectbox('지역명을 입력해주세요(읍면동 단위까지 가능) : ', region_names)

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
    plt.figure(figsize = (10,6), dpi=500)
    plt.style.use('ggplot')
    plt.title(selected_name + ' 지역과 인구 구조가 가장 비슷한 지역')
    plt.plot(pivot, label=selected_name)
    plt.plot(result, label=result_name)
    plt.legend()

    st.pyplot(plt)

