# Streamlit 애플리케이션 코드
import streamlit as st
import pandas as pd
import plotly.express as px
import koreanize_matplotlib

# 데이터 로드 및 전처리
file_path = 'daily_temp.csv'
data = pd.read_csv(file_path)
data['날짜'] = pd.to_datetime(data['날짜'].str.strip())
data['연도'] = data['날짜'].dt.year
data['월'] = data['날짜'].dt.month

# 봄과 가을의 평균기온 분석
spring_months = [3, 4, 5]
fall_months = [9, 10, 11]

spring_data = data[data['월'].isin(spring_months)].groupby('연도')['평균기온(℃)'].mean().reset_index()
fall_data = data[data['월'].isin(fall_months)].groupby('연도')['평균기온(℃)'].mean().reset_index()

# 스트림릿 인터페이스
st.title("봄과 가을의 길이 변화 분석")
st.markdown("""
**주제**: 봄과 가을이 줄어들고 있는지 연도별 기온 추세를 통해 분석합니다.
""")

# 봄과 가을의 기온 변화 시각화
st.header("1. 봄의 평균기온 변화")
fig_spring = px.line(spring_data, x='연도', y='평균기온(℃)', title="봄(3~5월)의 연도별 평균기온 변화")
st.plotly_chart(fig_spring)

st.header("2. 가을의 평균기온 변화")
fig_fall = px.line(fall_data, x='연도', y='평균기온(℃)', title="가을(9~11월)의 연도별 평균기온 변화")
st.plotly_chart(fig_fall)

# 결과 해석
st.header("결과 해석")
st.markdown("""
연도별 봄과 가을의 평균기온 변화를 통해 계절의 길이가 줄어들고 있는지 관찰할 수 있습니다.
- **봄의 평균기온**: 연도별 상승하는 경향이 있다면 봄이 빨리 찾아오거나 짧아지고 있음을 시사할 수 있습니다.
- **가을의 평균기온**: 비슷하게 가을의 평균기온이 상승하는 경우 가을이 짧아지거나 늦게 시작될 수 있습니다.

이 데이터 분석을 통해 연도별 기온 추세를 관찰하며 기후 변화에 따른 계절의 변화를 파악할 수 있습니다. 더 나아가 특정 연도의 기온 변화가 급격하다면, 해당 연도의 기후 패턴이나 이상기후 현상이 있었는지 추가 분석이 필요합니다.
""")
