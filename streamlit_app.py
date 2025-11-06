import streamlit as st
import pandas as pd
import numpy as np

# --- 1. 앱 설정 ---
st.set_page_config(
    page_title="Uber 픽업 시간대별 현황",
    page_icon="📊",
    layout="centered"
)

# --- 2. 헬퍼 함수 (데이터 로딩) ---
# 원본 파일의 load_data 함수를 그대로 사용합니다.
@st.cache_data
def load_data(nrows):
    """Uber 픽업 데이터를 로드하고 'hour' 컬럼을 추가하는 함수"""
    DATA_URL = "https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
    try:
        data = pd.read_csv(DATA_URL, nrows=nrows)
        data.rename(lambda x: str(x).lower(), axis='columns', inplace=True)
        data['date/time'] = pd.to_datetime(data['date/time'])
        # 차트 생성을 위해 'hour' 컬럼이 필수입니다.
        data['hour'] = data['date/time'].dt.hour
        return data
    except Exception as e:
        st.error(f"데이터 로딩 중 오류 발생: {e}")
        return pd.DataFrame()

# --- 3. 메인 화면 ---

st.title("🚕 뉴욕시 Uber 픽업 데이터")
st.subheader("시간대별 전체 픽업 횟수")

# 데이터 로딩 (스피너 표시)
with st.spinner('데이터 로딩 중... (약 10만 건)'):
    data = load_data(100000)

if not data.empty:
    # 원본 코드의 히스토그램 생성 로직
    # 0시부터 23시까지 총 24개의 구간(bin)으로 데이터의 'hour' 분포를 계산합니다.
    hist_values = np.histogram(
        data['hour'], bins=24, range=(0, 24)
    )[0]
    
    # st.bar_chart에 입력하기 위해 DataFrame을 생성합니다.
    hist_df = pd.DataFrame({
        'hour': range(24), 
        'pickups': hist_values
    })
    
    # 'hour' 컬럼을 인덱스로 설정하여 막대 차트를 그립니다.
    st.bar_chart(hist_df.set_index('hour'))
    
    st.caption("이 차트는 뉴욕시 Uber 픽업 데이터(약 10만 건)를 기반으로 24시간 동안의 픽업 횟수를 보여줍니다.")

else:
    # 데이터 로딩 실패 시
    st.error("데이터를 로드하지 못했습니다. 인터넷 연결을 확인해주세요.")
