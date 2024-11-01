import koreanize_matplotlib
# streamlit_app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit 설정
st.title("Creative Daily Temperature Data Analysis")
st.write("이 앱은 'daily_temp.csv' 데이터를 사용하여 다양한 창의적인 분석을 제공합니다.")

# 기본 CSV 파일 읽기
try:
    df = pd.read_csv("daily_temp.csv")
    df.columns = ['날짜', '지점', '평균기온(℃)', '최저기온(℃)', '최고기온(℃)']
    df['날짜'] = pd.to_datetime(df['날짜'].str.strip())
    df.set_index('날짜', inplace=True)

    # 월별 데이터 추가
    df['월'] = df.index.month

    # 전체 데이터 표시
    st.write("기본 데이터:")
    st.dataframe(df)

    # 월별 기온 분석
    st.subheader("월별 평균 기온 분석")
    monthly_avg = df.groupby('월')[['평균기온(℃)', '최저기온(℃)', '최고기온(℃)']].mean()
    st.bar_chart(monthly_avg)

    # 가장 더운 날과 추운 날
    st.subheader("역대 가장 덥고 추웠던 날")
    hottest_day = df[df['최고기온(℃)'] == df['최고기온(℃)'].max()]
    coldest_day = df[df['최저기온(℃)'] == df['최저기온(℃)'].min()]
    st.write("가장 더운 날:", hottest_day)
    st.write("가장 추운 날:", coldest_day)

    # 일교차가 가장 큰 날 분석
    df['일교차(℃)'] = df['최고기온(℃)'] - df['최저기온(℃)']
    max_diurnal_range_day = df[df['일교차(℃)'] == df['일교차(℃)'].max()]
    st.subheader("일교차가 가장 큰 날")
    st.write(max_diurnal_range_day)

    # 히스토그램 시각화 (bins 슬라이더 포함)
    st.subheader("평균 기온 히스토그램")
    bins = st.slider("히스토그램의 bins 수를 선택하세요", min_value=5, max_value=50, value=20)
    fig, ax = plt.subplots()
    ax.hist(df['평균기온(℃)'], bins=bins, color='lightgreen', edgecolor='black')
    ax.set_title("평균 기온 히스토그램")
    ax.set_xlabel("기온 (℃)")
    ax.set_ylabel("빈도수")
    st.pyplot(fig)

    # 일교차 히스토그램
    st.subheader("일교차 히스토그램")
    diurnal_bins = st.slider("일교차 히스토그램의 bins 수를 선택하세요", min_value=5, max_value=50, value=20, key='diurnal_bins')
    fig, ax = plt.subplots()
    ax.hist(df['일교차(℃)'], bins=diurnal_bins, color='lightcoral', edgecolor='black')
    ax.set_title("일교차 히스토그램")
    ax.set_xlabel("일교차 (℃)")
    ax.set_ylabel("빈도수")
    st.pyplot(fig)

    # 월별 일교차 평균 분석
    st.subheader("월별 평균 일교차 분석")
    monthly_diurnal_avg = df.groupby('월')['일교차(℃)'].mean()
    st.line_chart(monthly_diurnal_avg)

except FileNotFoundError:
    st.error("daily_temp.csv 파일이 존재하지 않습니다. 파일을 동일한 디렉토리에 추가해주세요.")
