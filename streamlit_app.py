import koreanize_matplotlib
# streamlit_app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np

# Streamlit 설정
st.title("Enhanced Daily Temperature Data Analysis")
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

    # 월별 평균, 최저, 최고 기온 분석
    st.subheader("월별 기온 분석")
    monthly_avg = df.groupby('월')[['평균기온(℃)', '최저기온(℃)', '최고기온(℃)']].mean()
    st.line_chart(monthly_avg)

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

    # 회귀 분석
    st.subheader("회귀 분석: 날짜에 따른 평균 기온 추세")
    df['일수'] = (df.index - df.index.min()).days  # 날짜를 일수로 변환
    X = df['일수'].values.reshape(-1, 1)
    y = df['평균기온(℃)'].values
    model = LinearRegression()
    model.fit(X, y)
    df['회귀선'] = model.predict(X)

    # 회귀 분석 그래프
    fig, ax = plt.subplots()
    sns.scatterplot(x=df.index, y='평균기온(℃)', data=df, ax=ax, label='평균 기온')
    ax.plot(df.index, df['회귀선'], color='red', label='회귀선')
    ax.set_title("평균 기온 회귀 분석")
    ax.set_xlabel("날짜")
    ax.set_ylabel("평균기온 (℃)")
    ax.legend()
    st.pyplot(fig)

except FileNotFoundError:
    st.error("daily_temp.csv 파일이 존재하지 않습니다. 파일을 동일한 디렉토리에 추가해주세요.")

