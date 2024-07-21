import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import os

# 한글 폰트 설정
plt.rcParams['font.family'] = 'NanumGothic'

st.set_page_config(page_title="인구 구조 분석", page_icon="📊", layout="wide")

st.markdown(
    """
    <h1 style='font-size:24px;'>2008년과 2024년의 인구 구조 비교 (by 서울고 교사 석리송)</h1>
    """,
    unsafe_allow_html=True
)

@st.cache_data
def load_data(file_path):
    if not os.path.exists(file_path):
        st.error(f"파일을 찾을 수 없습니다: {file_path}")
        return None
    try:
        return pd.read_csv(file_path, encoding='utf-8')
    except Exception as e:
        st.error(f"데이터 로딩 중 오류 발생: {str(e)}")
        return None

def preprocess_data(df):
    if df is None:
        return None
    df = df.set_index(df.columns[0])
    df.columns = df.columns.str.strip()
    df.index = df.index.str.strip()
    return df

# 데이터 로딩
data_2024 = load_data('age.csv')
data_2008 = load_data('age2008.csv')

# 데이터 전처리
data_2024 = preprocess_data(data_2024)
data_2008 = preprocess_data(data_2008)

if data_2024 is None or data_2008 is None:
    st.stop()

regions_2024 = data_2024.index
regions_2008 = data_2008.index

# 특정 지역 인구 구조 변화 비교
st.subheader("지역별 인구 구조 변화 비교")
input_region = st.selectbox('비교하고 싶은 지역을 선택하세요:', regions_2024)

if input_region:
    fig, ax = plt.subplots(figsize=(12, 6))
    
    if input_region in regions_2008:
        population_2008 = data_2008.loc[input_region].drop(['2008년02월_계_총인구수', '2008년02월_계_연령구간인구수'])
        population_2024 = data_2024.loc[input_region].drop(['2024년06월_계_총인구수', '2024년06월_계_연령구간인구수'])
        
        x = range(len(population_2008))
        ax.plot(x, population_2008.values, label='2008년')
        ax.plot(x, population_2024.values, label='2024년')
        
        ax.set_title(f'{input_region} 지역의 인구 구조 변화')
        ax.set_xlabel('연령대')
        ax.set_ylabel('인구수')
        ax.set_xticks(x[::5])
        ax.set_xticklabels(population_2008.index[::5])
        ax.legend()
        
        st.pyplot(fig)
    else:
        st.warning(f"{input_region} 지역은 2008년 데이터에 존재하지 않습니다.")

# 연령대별 인구 변화 분석
st.subheader("연령대별 인구 변화 분석")
age_group = st.number_input('분석하고 싶은 연령대를 입력하세요:', min_value=0, max_value=100, step=1, value=30)

age_col_2024 = f'2024년06월_계_{age_group}세'
age_col_2008 = f'2008년02월_계_{age_group}세'

if age_col_2024 in data_2024.columns and age_col_2008 in data_2008.columns:
    data_2024['Population_2024'] = data_2024[age_col_2024]
    data_2008['Population_2008'] = data_2008[age_col_2008]
    merged_data = data_2024[['Population_2024']].merge(data_2008[['Population_2008']], left_index=True, right_index=True, how='outer').fillna(0)
    merged_data['Population_Change'] = merged_data['Population_2024'] - merged_data['Population_2008']
    
    most_increase_region = merged_data['Population_Change'].idxmax()
    most_decrease_region = merged_data['Population_Change'].idxmin()
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("인구가 가장 많이 증가한 지역", most_increase_region, f"{merged_data['Population_Change'].max():.0f}")
    with col2:
        st.metric("인구가 가장 많이 감소한 지역", most_decrease_region, f"{merged_data['Population_Change'].min():.0f}")

    fig, ax = plt.subplots(figsize=(12, 8))
    merged_data_sorted = merged_data.sort_values('Population_Change')
    ax.barh(merged_data_sorted.index, merged_data_sorted['Population_Change'], color='skyblue')
    ax.set_title(f'연령대 {age_group}세의 지역별 인구 변화')
    ax.set_xlabel('인구 변화 수')
    ax.set_ylabel('지역')
    
    # y축 레이블 개수 조정
    if len(merged_data) > 20:
        ax.set_yticks(ax.get_yticks()[::3])
    
    st.pyplot(fig)
else:
    st.warning(f"연령대 {age_group}세에 대한 데이터가 존재하지 않습니다.")

# 데이터 출처 및 주의사항
st.markdown("---")
st.caption("데이터 출처: 행정안전부 주민등록 인구통계")
st.caption("주의: 이 분석은 제공된 데이터에 기반하며, 실제 상황과 차이가 있을 수 있습니다.")
