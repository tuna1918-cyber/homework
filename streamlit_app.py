import streamlit as st
import pandas as pd
import datetime

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="KOSPI 실시간 대시보드",
    page_icon="📈",
    layout="wide"
)

# 2. 대시보드 제목
st.title("📈 KOSPI 실시간 대시보드")
st.markdown(f"**기준일: {datetime.date.today().strftime('%Y-%m-%d')}**")
st.caption("이 앱은 Yahoo Finance API를 통해 실시간 KOSPI 데이터를 받아옵니다.")

# 3. 데이터 로드 (yfinance)
# @st.cache_data : 데이터를 캐싱하여 앱 속도 향상
@st.cache_data
def load_data():
    # KOSPI의 Ticker(종목코드)는 '^KS11'입니다.
    ticker = yf.Ticker("^KS11")
    
    # 'period="1y"' : 최근 1년 간의 데이터를 '일(day)' 단위로 가져옵니다.
    # (옵션: "1mo", "3mo", "6mo", "1y", "2y", "5y", "max")
    data = ticker.history(period="1y", interval="1d")
    
    # 날짜 인덱스를 'Date' 컬럼으로 리셋
    data = data.reset_index()
    # 날짜(Date) 컬럼을 날짜 형식으로 변환 (시간 정보 제거)
    data['Date'] = data['Date'].dt.date
    
    return data

# 데이터 로딩 스피너
with st.spinner('KOSPI 데이터를 로딩 중입니다...'):
    df = load_data()

# 데이터 로드 실패 시 처리
if df.empty:
    st.error("데이터를 불러오는 데 실패했습니다. 네트워크 연결을 확인하거나 잠시 후 다시 시도하세요.")
    st.stop()

# 4. 주요 지표 (Metrics)
st.divider()

# 최신 데이터(오늘 또는 가장 최근 거래일)
latest_data = df.iloc[-1]
# 어제 데이터 (두 번째 최신 거래일)
yesterday_data = df.iloc[-2]

# 지수 계산
latest_close = latest_data['Close']
change = latest_close - yesterday_data['Close']
percent_change = (change / yesterday_data['Close']) * 100

# Metric 델타(변동) 색상 설정
delta_color = "inverse" # 기본값 (오르면 빨간색, 내리면 파란색)
# (참고: Streamlit의 기본 색상은 미국식(오르면 초록)입니다)
# delta_color = "normal" 

col1, col2, col3 = st.columns(3)
col1.metric(
    "KOSPI 지수", 
    f"{latest_close:,.2f} P",
    f"{change:,.2f} P ({percent_change:.2f}%)",
    delta_color=delta_color
)
col2.metric(
    "거래량 (Volume)",
    f"{latest_data['Volume']:,} 주",
    delta=int(latest_data['Volume'] - yesterday_data['Volume']),
    delta_color=delta_color
)
col3.metric(
    "당일 고가 (High)",
    f"{latest_data['High']:,.2f} P"
)

# 5. 시각화
st.divider()

# 5-1. KOSPI 지수 종가 차트 (Line Chart)
st.subheader("📊 KOSPI 지수 (최근 1년)")
st.markdown("KOSPI 지수의 종가(Close) 기준 변동 추이입니다.")

# 차트용 데이터프레임 (날짜를 인덱스로 설정해야 함)
chart_df = df.set_index('Date')
st.line_chart(chart_df['Close'], color="#FF0000") # 붉은색

# 5-2. 거래량 차트 (Bar Chart)
st.subheader("📊 거래량 (최근 1년)")
st.markdown("지수 변동과 함께 거래량(Volume)을 확인하는 것은 시장의 관심도를 파악하는 데 중요합니다.")
st.bar_chart(chart_df['Volume'], color="#0000FF") # 푸른색


# 6. 원본 데이터 보기
st.divider()
if st.checkbox("KOSPI 원본 데이터 테이블 보기"):
    st.dataframe(df, use_container_width=True)
    st.caption("출처: Yahoo Finance API (^KS11)")
