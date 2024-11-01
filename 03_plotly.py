# Streamlit 애플리케이션 코드
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 데이터 로드
file_path = 'daily_temp.csv'
data = pd.read_csv(file_path)

# 날짜 열의 전처리
data['날짜'] = pd.to_datetime(data['날짜'].str.strip())

# 사이드바 메뉴 생성
st.sidebar.header("데이터 분석 항목 선택")
options = [
    "1. 평균기온 추이",
    "2. 최고/최저 기온 비교",
    "3. 특정 연도의 월별 기온",
    "4. 특정 달의 평균기온 변화",
    "5. 특정 기간의 기온 비교",
    "6. 이상기온 탐지",
    "7. 기온의 분포 분석",
    "8. 특정 지점의 기온 변화",
    "9. 기온의 연도별 평균 비교",
    "10. 기온 변화 패턴 시각화"
]
choice = st.sidebar.selectbox("보고 싶은 분석을 선택하세요:", options)

# 분석별 코드 작성
if choice == "1. 평균기온 추이":
    st.header("1. 평균기온 추이")
    fig = px.line(data, x='날짜', y='평균기온(℃)', title="날짜별 평균기온 추이")
    st.plotly_chart(fig)

elif choice == "2. 최고/최저 기온 비교":
    st.header("2. 최고/최저 기온 비교")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['날짜'], y=data['최고기온(℃)'], mode='lines', name='최고기온'))
    fig.add_trace(go.Scatter(x=data['날짜'], y=data['최저기온(℃)'], mode='lines', name='최저기온'))
    fig.update_layout(title="최고 및 최저 기온 비교", xaxis_title="날짜", yaxis_title="기온 (℃)")
    st.plotly_chart(fig)

elif choice == "3. 특정 연도의 월별 기온":
    st.header("3. 특정 연도의 월별 기온")
    year = st.sidebar.slider("연도 선택", int(data['날짜'].dt.year.min()), int(data['날짜'].dt.year.max()))
    filtered_data = data[data['날짜'].dt.year == year]
    filtered_data['월'] = filtered_data['날짜'].dt.month
    monthly_avg = filtered_data.groupby('월')['평균기온(℃)'].mean().reset_index()
    fig = px.bar(monthly_avg, x='월', y='평균기온(℃)', title=f"{year}년 월별 평균기온")
    st.plotly_chart(fig)

elif choice == "4. 특정 달의 평균기온 변화":
    st.header("4. 특정 달의 평균기온 변화")
    month = st.sidebar.slider("월 선택", 1, 12)
    month_data = data[data['날짜'].dt.month == month]
    fig = px.line(month_data, x='날짜', y='평균기온(℃)', title=f"{month}월 평균기온 변화")
    st.plotly_chart(fig)

elif choice == "5. 특정 기간의 기온 비교":
    st.header("5. 특정 기간의 기온 비교")
    start_date = st.sidebar.date_input("시작 날짜", data['날짜'].min())
    end_date = st.sidebar.date_input("종료 날짜", data['날짜'].max())
    filtered_data = data[(data['날짜'] >= pd.to_datetime(start_date)) & (data['날짜'] <= pd.to_datetime(end_date))]
    fig = px.line(filtered_data, x='날짜', y=['평균기온(℃)', '최고기온(℃)', '최저기온(℃)'], title="특정 기간의 기온 비교")
    st.plotly_chart(fig)

elif choice == "6. 이상기온 탐지":
    st.header("6. 이상기온 탐지")
    threshold = st.sidebar.slider("이상기온 탐지 기준 (℃)", data['평균기온(℃)'].min(), data['평균기온(℃)'].max(), step=1)
    outliers = data[data['평균기온(℃)'] > threshold]
    fig = px.scatter(outliers, x='날짜', y='평균기온(℃)', color='평균기온(℃)', title="이상기온 탐지")
    st.plotly_chart(fig)

elif choice == "7. 기온의 분포 분석":
    st.header("7. 기온의 분포 분석")
    fig, ax = plt.subplots()
    ax.hist(data['평균기온(℃)'], bins=30, edgecolor='black')
    ax.set_title('평균기온의 분포')
    ax.set_xlabel('기온 (℃)')
    ax.set_ylabel('빈도')
    st.pyplot(fig)

elif choice == "8. 특정 지점의 기온 변화":
    st.header("8. 특정 지점의 기온 변화")
    station = st.sidebar.selectbox("지점 선택", data['지점'].unique())
    station_data = data[data['지점'] == station]
    fig = px.line(station_data, x='날짜', y='평균기온(℃)', title=f"지점 {station}의 평균기온 변화")
    st.plotly_chart(fig)

elif choice == "9. 기온의 연도별 평균 비교":
    st.header("9. 기온의 연도별 평균 비교")
    data['연도'] = data['날짜'].dt.year
    yearly_avg = data.groupby('연도')['평균기온(℃)'].mean().reset_index()
    fig = px.bar(yearly_avg, x='연도', y='평균기온(℃)', title="연도별 평균기온 비교")
    st.plotly_chart(fig)

elif choice == "10. 기온 변화 패턴 시각화":
    st.header("10. 기온 변화 패턴 시각화")
    fig = go.Figure(data=[
        go.Candlestick(x=data['날짜'],
                       open=data['최저기온(℃)'],
                       high=data['최고기온(℃)'],
                       low=data['최저기온(℃)'],
                       close=data['평균기온(℃)'])
    ])
    fig.update_layout(title="기온 변화 패턴", xaxis_title="날짜", yaxis_title="기온 (℃)")
    st.plotly_chart(fig)
