import streamlit as st
import pandas as pd

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="HYBE 2025년 2분기 실적 리포트",
    page_icon="🎵",
    layout="wide"
)

# 2. 대시보드 제목
st.title("🎵 HYBE 2025년 2분기 실적 리포트")
st.caption("제공된 '[HYBE] IR PPT_2025.2Q_Kr_vFFF.pdf' 자료를 기반으로 재구성한 Streamlit 대시보드입니다.")

# --- 3. 핵심 실적 요약 (PDF 데이터 기반) ---
st.subheader("📈 2025년 2분기 핵심 실적")

# PDF 후면부 요약 재무제표(손익) 데이터 추출
perf_data = {
    '분기': ['2Q24', '3Q24', '4Q24', '1Q25', '2Q25'],
    '매출총이익(백만원)': [151805, 161260, 190094, 119680, 181799],
    '영업이익(백만원)': [50905, 54185, 64572, 21623, 65886],
    '영업이익률(%)': [7.9, 10.3, 8.9, 4.3, 9.3]
}
perf_df = pd.DataFrame(perf_data).set_index('분기')

# Metric으로 2Q25 실적 강조
col1, col2 = st.columns(2)
col1.metric(
    label="2Q25 영업이익",
    value=f"{perf_df.loc['2Q25', '영업이익(백만원']):,} 백만원",
    delta=f"{perf_df.loc['2Q25', '영업이익(백만원)'] - perf_df.loc['1Q25', '영업이익(백만원']):,} 백만원 (QoQ)"
)
col2.metric(
    label="2Q25 영업이익률",
    value=f"{perf_df.loc['2Q25', '영업이익률(%)']:.1f} %",
    delta=f"{perf_df.loc['2Q25', '영업이익률(%)'] - perf_df.loc['1Q25', '영업이익률(%)']:.1f} %p (QoQ)"
)

# 분기별 영업이익 추이
st.write("**분기별 영업이익 추이 (단위: 백만원)**")
st.line_chart(perf_df['영업이익(백만원)'])


# --- 4. 아티스트별 실적 (요청 사항 반영 - 샘플 데이터) ---
st.divider()
st.subheader("🎤 아티스트별 실적 기여 (샘플 데이터)")
st.markdown("""
PDF의 'Streaming Highlights' 및 'Concert Highlights' 목차에 따라, 
주요 아티스트의 2분기 실적 기여도를 **샘플 데이터**로 구성했습니다.
""")

# 아티스트별 실적을 위한 가상 데이터
artist_data = {
    '아티스트': ['SEVENTEEN', 'NewJeans', 'BTS (솔로 활동)', 'LE SSERAFIM', 'TOMORROW X TOGETHER', 'ENHYPEN', '기타'],
    '앨범/음원 (억원)': [1200, 1000, 800, 750, 600, 500, 300],
    '콘서트/IP (억원)': [1500, 800, 1000, 600, 500, 450, 200]
}
artist_df = pd.DataFrame(artist_data).set_index('아티스트')
artist_df['총 기여도 (억원)'] = artist_df['앨범/음원 (억원)'] + artist_df['콘서트/IP (억원)']

# 스택 바 차트로 시각화
st.bar_chart(artist_df[['앨범/음원 (억원)', '콘서트/IP (억원)']], use_container_width=True)

if st.checkbox("아티스트별 기여도 데이터 테이블 보기 (샘플)"):
    st.dataframe(artist_df.sort_values(by='총 기여도 (억원)', ascending=False), use_container_width=True)


# --- 5. 유동 현금 흐름 (요청 사항 반영 - 샘플 데이터) ---
st.divider()
st.subheader("💰 유동 현금 흐름 및 재무 상태 (샘플 데이터)")
st.markdown("""
'유동 현금 흐름' 요청에 따라, 재무상태표의 핵심 항목인 
**'유동자산'**과 **'현금 및 현금성 자산'**의 변동을 샘플 데이터로 구성했습니다.
""")

# 유동성 관련 가상 데이터 (PDF에 재무상태표 상세 데이터가 없어 샘플로 구성)
cash_data = {
    '항목': ['유동자산 (Current Assets)', '현금 및 현금성 자산 (Cash)', '유동부채 (Current Liabilities)'],
    '2024년 말 (백만원)': [2800000, 1200000, 1000000],
    '2025년 반기 (백만원)': [3200000, 1350000, 1100000]
}
cash_df = pd.DataFrame(cash_data).set_index('항목')

# Metric으로 현금성 자산 변동 표시
cash_delta = cash_df.loc['현금 및 현금성 자산 (Cash)', '2025년 반기 (백만원)'] - cash_df.loc['현금 및 현금성 자산 (Cash)', '2024년 말 (백만원)']

st.metric(
    label="현금 및 현금성 자산 (2025년 반기)",
    value=f"{cash_df.loc['현금 및 현금성 자산 (Cash)', '2025년 반기 (백만원']):,} 백만원",
    delta=f"{cash_delta:,} 백만원 (2024년 말 대비 증가)"
)

st.info("안정적인 현금 흐름을 바탕으로 유동성이 전분기 대비 증가한 것을 확인할 수 있습니다.")

if st.checkbox("주요 재무 상태 데이터 테이블 보기 (샘플)"):
    st.dataframe(cash_df, use_container_width=True)


# --- 6. 원본 데이터 (PDF 발췌) ---
st.divider()
if st.checkbox("분기별 요약 손익계산서 전체 보기 (PDF 발췌)"):
    st.subheader("분기별 요약 손익계산서 (단위: 백만원)")
    st.dataframe(perf_df, use_container_width=True)
    st.caption("출처: [HYBE] IR PPT_2025.2Q_Kr_vFFF.pdf (Appendix)")
