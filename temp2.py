# streamlit_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# Load the data
data = pd.read_csv('daily_temp.csv')

# Clean up the data
data['날짜'] = pd.to_datetime(data['날짜'].str.strip(), errors='coerce')
data = data.dropna(subset=['날짜'])

# Streamlit app layout
st.title("기온 데이터 분석")
st.sidebar.header("옵션")

# Sidebar options
selected_date_range = st.sidebar.date_input("날짜 범위 선택", [data['날짜'].min(), data['날짜'].max()])
if len(selected_date_range) == 2:
    data = data[(data['날짜'] >= pd.Timestamp(selected_date_range[0])) & (data['날짜'] <= pd.Timestamp(selected_date_range[1]))]

# Main content
st.write("선택한 데이터 미리보기")
st.dataframe(data)

# Line plot for temperature trends
st.subheader("기온 변화 추이")
plt.figure(figsize=(12, 6))
plt.plot(data['날짜'], data['평균기온(℃)'], label='평균기온(℃)')
plt.plot(data['날짜'], data['최저기온(℃)'], label='최저기온(℃)', linestyle='--')
plt.plot(data['날짜'], data['최고기온(℃)'], label='최고기온(℃)', linestyle='--')
plt.xlabel("날짜")
plt.ylabel("기온 (℃)")
plt.title("날짜별 기온 변화")
plt.legend()
plt.grid(True)

st.pyplot(plt)

# Additional interaction - temperature comparison
st.subheader("기온 비교 분석")
selected_columns = st.multiselect("비교할 기온 선택", ['평균기온(℃)', '최저기온(℃)', '최고기온(℃)'], default=['평균기온(℃)'])
if selected_columns:
    st.line_chart(data.set_index('날짜')[selected_columns])

st.write("분석 완료!")
