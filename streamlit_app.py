# streamlit_app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit 설정
st.title("Daily Temperature Data Visualization")
st.write("이 앱은 기온 데이터를 시각화하고 분석하는 도구입니다.")

# CSV 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # 데이터 읽기
    df = pd.read_csv(uploaded_file)
    df.columns = ['날짜', '지점', '평균기온(℃)', '최저기온(℃)', '최고기온(℃)']
    
    # 날짜 컬럼을 datetime 형식으로 변환
    df['날짜'] = pd.to_datetime(df['날짜'].str.strip())
    df.set_index('날짜', inplace=True)
    
    # 전체 데이터 표시
    st.write("업로드된 데이터:")
    st.dataframe(df)

    # 시각화 옵션 선택
    st.sidebar.header("시각화 옵션")
    chart_type = st.sidebar.selectbox("그래프 종류를 선택하세요", ("선 그래프", "히스토그램", "상자 그림"))
    
    # 날짜 범위 필터
    date_range = st.sidebar.date_input("날짜 범위를 선택하세요", [df.index.min(), df.index.max()])
    
    if len(date_range) == 2:
        filtered_df = df.loc[date_range[0]:date_range[1]]
    else:
        filtered_df = df
    
    # 선택한 차트 그리기
    if chart_type == "선 그래프":
        st.line_chart(filtered_df[['평균기온(℃)', '최저기온(℃)', '최고기온(℃)']])
    elif chart_type == "히스토그램":
        fig, ax = plt.subplots()
        ax.hist(filtered_df['평균기온(℃)'], bins=20, color='skyblue', edgecolor='black')
        ax.set_title("평균기온 히스토그램")
        ax.set_xlabel("기온 (℃)")
        ax.set_ylabel("빈도수")
        st.pyplot(fig)
    elif chart_type == "상자 그림":
        fig, ax = plt.subplots()
        filtered_df[['평균기온(℃)', '최저기온(℃)', '최고기온(℃)']].plot(kind='box', ax=ax)
        ax.set_title("기온 상자 그림")
        st.pyplot(fig)
    
    # 요약 통계
    st.write("선택된 데이터의 요약 통계:")
    st.write(filtered_df.describe())
