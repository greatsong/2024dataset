# streamlit_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# Load the data
data = pd.read_csv('daily_temp.csv')
data['날짜'] = pd.to_datetime(data['날짜'].str.strip(), errors='coerce')
data = data.dropna(subset=['날짜'])

# Streamlit app layout
st.set_page_config(page_title="기온 데이터 분석", layout="wide")
st.title("🌤️ 기온 데이터 분석")
st.sidebar.header("옵션")

# Sidebar options
selected_date_range = st.sidebar.date_input("날짜 범위 선택", [data['날짜'].min(), data['날짜'].max()])
if len(selected_date_range) == 2:
    data = data[(data['날짜'] >= pd.Timestamp(selected_date_range[0])) & (data['날짜'] <= pd.Timestamp(selected_date_range[1]))]

# Summary cards
st.subheader("📊 요약 통계")
col1, col2, col3 = st.columns(3)
col1.metric("평균 기온 (℃)", f"{data['평균기온(℃)'].mean():.2f}℃")
col2.metric("최저 기온 (℃)", f"{data['최저기온(℃)'].min():.2f}℃")
col3.metric("최고 기온 (℃)", f"{data['최고기온(℃)'].max():.2f}℃")

# Temperature filter
st.sidebar.subheader("기온 범위 필터")
min_temp, max_temp = st.sidebar.slider(
    "기온 범위 선택 (℃)",
    float(data['평균기온(℃)'].min()),
    float(data['평균기온(℃)'].max()),
    (float(data['평균기온(℃)'].min()), float(data['평균기온(℃)'].max()))
)
filtered_data = data[(data['평균기온(℃)'] >= min_temp) & (data['평균기온(℃)'] <= max_temp)]

# Main content
st.write("선택한 데이터 미리보기")
st.dataframe(filtered_data)

# Line plot for temperature trends
st.subheader("📈 기온 변화 추이")
plt.figure(figsize=(12, 6))
plt.plot(filtered_data['날짜'], filtered_data['평균기온(℃)'], label='평균기온(℃)', color='blue')
plt.plot(filtered_data['날짜'], filtered_data['최저기온(℃)'], label='최저기온(℃)', color='green', linestyle='--')
plt.plot(filtered_data['날짜'], filtered_data['최고기온(℃)'], label='최고기온(℃)', color='red', linestyle='--')
plt.xlabel("날짜")
plt.ylabel("기온 (℃)")
plt.title("날짜별 기온 변화")
plt.legend()
plt.grid(True)

st.pyplot(plt)

# Date picker for individual analysis
selected_date = st.date_input("개별 날짜 선택", data['날짜'].min())
selected_row = data[data['날짜'] == pd.Timestamp(selected_date)]
if not selected_row.empty:
    st.write("선택한 날짜의 기온 데이터")
    st.write(selected_row)
else:
    st.write("선택한 날짜의 데이터가 없습니다.")
