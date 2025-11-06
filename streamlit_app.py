import streamlit as st
import pandas as pd
import numpy as np
import datetime

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="KOSPI 외국인 유동 자금 대시보드",
    page_icon="KRW", # 🇰🇷
    layout="wide"
)

# --- 2. 가상 데이터 생성 (yfinance 불필요) ---
# (실제 데이터 파일이 없으므로, 최근 30일간의 가상 데이터를 생성합니다)
@st.cache_data
def create_sample_data():
    today = datetime.date.today()
    # freq='B'는 Business day(영업일) 기준
    dates = pd.date_range(end=today, periods=30, freq='B')
    
    # 가상 KOSPI 지수 (2500pt 근방에서 무작위 변동)
    kospi_index = (np.random.randn(30).cumsum() * 15) + 2500
    
    # 가상 외국인 순매수 (억 원 단위, 0을 기준으로 +/- 5000억)
    foreign_net = (np.random.randn(30) * 2000)
    
    df = pd.DataFrame({
        'KOSPI 지수': kospi_index,
        '외국인 순매수(억 원)': foreign_net
    }, index=dates)
    
    df.index.name = '날짜'
    return df

# 데이터 로드
df = create_sample_data()
# ----------------------------------------

# 3. 대시보드 제목
st.title("📈 KOSPI 외국인 유동 자금 대시보드 (샘플)")
st.markdown(f"**기준일: {datetime.date.today().strftime('%Y-%m-%d')}**")
st.info("이 앱은 `yfinance` 없이 **가상의 샘플 데이터**로 실행되고 있습니다.")

# 4. 주요 지표 (Metrics)
st.divider()
today_data = df.iloc[-1] # 오늘(최신) 데이터
yesterday_data = df.iloc[-2] # 어제 데이터

# KOSPI 지수 변동
kospi_delta = today_data['KOSPI 지수'] - yesterday_data['KOSPI 지수']
# 외국인 순매수 변동
foreign_delta = today_data['외국인 순매수(억 원)'] - yesterday_data['외국인 순매수(억 원)']

col1, col2, col3 = st.columns(3)
col1.metric(
    "KOSPI 지수", 
    f"{today_data['KOSPI 지수']:.2f} P",
    f"{kospi_delta:.2f} P (전일 대비)"
)
col2.metric(
    "당일 외국인 순매수",
    f"{today_data['외국인 순매수(억 원)']:,.0f} 억 원",
    f"{foreign_delta:,.0f} 억 원 (전일 대비)"
)
col3.metric(
    "최근 30일 누적 순매수",
    f"{df['외국인 순매수(억 원)'].sum():,.0f} 억 원"
)

# 5. 시각화
st.divider()
st.subheader("📊 최근 30영업일 외국인 순매수 (유동 자금)")
st.markdown("양수(+)는 순매수(자금 유입), 음수(-)는 순매도(자금 유출)를 의미합니다.")
st.bar_chart(df['외국인 순매수(억 원)'], color="#FF0000") # 붉은색 계열

st.subheader("📈 KOSPI 지수 및 외국인 누적 순매수 추이")
st.markdown("외국인 자금 유입이 KOSPI 지수에 어떤 영향을 주는지 비교해볼 수 있습니다.")

# 누적 순매수 계산
df['외국인 누적 순매수(억 원)'] = df['외국인 순매수(억 원)'].cumsum()

# KOSPI와 누적 순매수 비교
col_left, col_right = st.columns(2)
with col_left:
    st.write("**KOSPI 지수 추이**")
    st.line_chart(df['KOSPI 지수'])

with col_right:
    st.write("**외국인 누적 순매수 추이**")
    st.line_chart(df['외국인 누적 순매수(억 원)'])


# 6. 원본 데이터 보기
st.divider()
if st.checkbox("샘플 데이터 원본 테이블 보기"):
    st.dataframe(df, use_container_width=True)
