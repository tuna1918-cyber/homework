import streamlit as st
import pandas as pd

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="SHIFT UP 실적 대시보드",
    page_icon="📈",
    layout="wide"
)

# 2. 대시보드 제목
st.title("📊 시프트업(SHIFT UP) 2025년 2분기 실적 요약")
st.caption("이 앱은 제공된 '[실적자료] 2025년 2분기 실적' PDF를 기반으로 합니다.")

# 3. 데이터 준비 (PDF Page 5 '실적요약' 표 기반)
data = {
    '분기': ['2Q24', '3Q24', '4Q24', '1Q25', '2Q25'],
    '영업수익 (백만원)': [65202, 58018, 63490, 42235, 112383],
    '영업이익 (백만원)': [45007, 35577, 46157, 26251, 68215],
    '분기순이익 (백만원)': [40260, 23484, 59530, 26846, 51306],
    '승리의 여신: 니케 (백만원)': [38467, 34231, 42356, 32311, 45112],
    '스텔라 블레이드 (백만원)': [25863, 22584, 19615, 7012, 65719]
}
perf_df = pd.DataFrame(data).set_index('분기')

# --- 4. 대시보드 시각화 ---

# 4-1. 주요 실적 추이 (영업수익, 영업이익)
st.subheader("📈 분기별 주요 실적 추이")
st.markdown("2025년 2분기에 영업수익과 영업이익이 크게 증가했습니다.")

# 라인 차트로 영업수익과 영업이익 표시
st.line_chart(perf_df[['영업수익 (백만원)', '영업이익 (백만원)']])

# 4-2. IP별 영업수익
st.subheader("🎮 IP별 분기 영업수익")
st.markdown("<스텔라 블레이드> PC 버전 론칭 및 <승리의 여신: 니케>의 중국 시장 출시 등이 2분기 실적을 견인했습니다.")

# 스택 바 차트로 IP별 수익 표시
ip_revenue_df = perf_df[['승리의 여신: 니케 (백만원)', '스텔라 블레이드 (백만원)']]
st.bar_chart(ip_revenue_df)

# 4-3. 유동자산 현황 (PDF Page 12 '재무상태표')
st.subheader("💰 주요 재무상태 (유동자산)")

# [수정됨] "사용자님께서 요청하신" 문구 제거
st.markdown("'유동현금 흐름'과 가장 유사한 항목인 **'유동자산'**의 변화입니다.") 

# Metric 컴포넌트를 사용하여 주요 지표 강조
col1, col2, col3 = st.columns(3)
col1.metric(
    label="유동자산 (제 13 당반기)", 
    value="824,454 백만원", 
    delta="56,282 백만원"
)
col2.metric(
    label="유동자산 (제 12 전기)", 
    value="768,172 백만원"
)

st.info("제 13 당반기(2025년 반기) 유동자산이 전기(2024년 말) 대비 증가했습니다.")


# 4-4. 원본 데이터 테이블
st.divider()
if st.checkbox("전체 실적 요약 테이블 보기 (PDF Page 5)"):
    st.subheader("분기별 실적 요약 (단위: 백만원)")
    st.dataframe(perf_df, use_container_width=True)
    st.caption("출처: [실적자료] 2025년 2분기 실적 시프트업_250811.pdf (Page 5)")
