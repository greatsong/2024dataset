import streamlit as st
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

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

# 지역 이름 입력받기
name = st.text_input('(2024년 기준) 궁금한 지역 이름을 입력해주세요 :')

if name:
    pivot = []
    for row in data:
        if name in row[0]:
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
        if s < mn and (name not in row[0]):
            mn = s
            result = []
            for i in range(3, len(row)):
                result.append(row[i] / row[2])
            result_name = row[0]

    # 시각화
    plt.figure(dpi=300)
    plt.style.use('ggplot')
    plt.title(name + ' 지역과 인구 구조가 가장 비슷한 지역')
    plt.plot(pivot, label=name)
    plt.plot(result, label=result_name)
    plt.legend()

    st.pyplot(plt)
