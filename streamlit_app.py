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
st.caption("이 리포트는 '[HYBE] IR PPT_2025.2Q_Kr_vFFF.pdf' 자료의 데이터를 기반으로 합니다.")

# --- 3. 2Q25 핵심 실적 (PDF Page 4, 10) ---
st.subheader("📈 2025년 2분기 핵심 실적")

# [cite_start]Page 4 [cite: 29] [cite_start]및 Page 10 [cite: 214] 데이터 기반
col1, col2, col3 = st.columns(3)
col1.metric(
    label="2Q25 매출액",
    [cite_start]value="7,056 억원", # [cite: 29]
    [cite_start]delta="전분기 대비 +41.0%" # [cite: 29]
)
col2.metric(
    label="2Q25 영업이익",
    [cite_start]value="659 억원", # [cite: 29] (Page 4)
    [cite_start]delta="전분기 대비 +204.7%" # [cite: 29]
)
col3.metric(
    label="2Q25 영업이익률",
    [cite_start]value="9.3%", # [cite: 32, 214]
    [cite_start]delta="5.0%p (QoQ)" # [cite: 32]
)

# [cite_start]Page 10 '연결손익계산서' 기반 분기별 영업이익 데이터 [cite: 214]
op_profit_data = {
    '분기': ['2024.2Q', '2024.3Q', '2024.4Q', '2025.1Q', '2025.2Q'],
    '영업이익 (백만원)': [50905, 54185, 64572, 21623, 65886]
}
op_profit_df = pd.DataFrame(op_profit_data).set_index('분기')

st.write("**분기별 영업이익 추이 (단위: 백만원)**")
st.line_chart(op_profit_df['영업이익 (백만원)'])


# --- 4. 아티스트 실적 하이라이트 (PDF Page 5, 6, 7) ---
st.divider()
st.subheader("🎤 아티스트 실적 하이라이트")

# 탭 구성
tab1, tab2, tab3 = st.tabs(["스트리밍 (Page 5)", "공연 (Page 6)", "KATSEYE (Page 7)"])

with tab1:
    st.markdown("""
    [cite_start]**Streaming Highlights (Page 5)** [cite: 35]
    
    2025년 상반기 빌보드 Hot 100 성과:
    * [cite_start]**BTS**[cite: 40]:
        * [cite_start]지민, 'Who', 11주 연속 차트인 [cite: 42]
        * [cite_start]제이홉, 'LV Bag', 'Sweet Dreams', 'Mona Lisa' 각각 차트인 [cite: 43]
        * [cite_start]진, 'Don't Say You Love Me' 차트인 [cite: 44]
    * [cite_start]**Quality Control Music**[cite: 41]:
        * [cite_start]Lil Baby, 상반기 총 13곡 차트인 [cite: 45]
        * [cite_start]BigXthaPlug, 'The Largest' 18주, 'All The Way' 12주 차트인 [cite: 47, 48]
    * [cite_start]**Big Machine Label Group**[cite: 63]:
        * [cite_start]Riley Green, 'Worst Way', 21주 연속 차트인 [cite: 49]
        * [cite_start]Thomas Rhett, 'Somethin' Bout a Woman' 6주, 'After All The Bars Are Closed' 9주 연속 차트인 [cite: 65]
    """)

with tab2:
    [cite_start]st.markdown("**Concert Highlights (Page 6)** [cite: 76]")
    
    # [cite_start]Page 6 '공연 매출' 데이터 [cite: 78, 88, 89, 90, 96, 98]
    concert_revenue_data = {
        '연도': ['2020', '2021', '2022', '2023', '2024', '2025.1H'],
        '공연 매출 (십억원)': [5, 45, 258, 359, 451, 344]
    }
    concert_revenue_df = pd.DataFrame(concert_revenue_data).set_index('연도')
    
    st.write("**연도별 공연 매출 (단위: 십억원)**")
    st.bar_chart(concert_revenue_df['공연 매출 (십억원)'])

    # [cite_start]Page 6 '공연 현황' 데이터 [cite: 79, 81, 82, 83, 84, 85, 86, 91, 92, 93, 94, 95, 97]
    concert_status_data = {
        '연도': ['2021', '2022', '2023', '2024', '2025.1H'],
        '공연 진행 아티스트 (팀)': ['2팀', '4팀', '7팀', '9팀', '10팀'],
        '공연 진행 횟수': ['8회', '78회', '125회', '172회', '140회']
    }
    concert_status_df = pd.DataFrame(concert_status_data).set_index('연도')
    st.write("**연도별 공연 현황**")
    st.dataframe(concert_status_df, use_container_width=True)

with tab3:
    st.markdown("""
    [cite_start]**KATSEYE Highlights (Page 7)** [cite: 113]
    
    * [cite_start]두 번째 미니앨범 'Beautiful Chaos' 'Billboard 200' 등 4주 연속 차트인 [cite: 115]
    * [cite_start]선공개곡 'Gnarly' 'Billboard Hot 100' 3주, 'Global 200' 12주 연속 차트인 [cite: 116]
    * [cite_start]수록곡 'Gabriela' 'Billboard Hot 100' 2주, 'Global 200' 등 5주 연속 차트인 [cite: 117]
    * [cite_start]데뷔 1년 반만에 첫 투어 'The Beautiful Chaos Tour' 발표, 13개 도시 및 추가 3개 공연 전석 매진 [cite: 118, 119]
    """)

# --- 5. 유동 현금 흐름 (PDF Page 10) ---
st.divider()
st.subheader("💰 유동성 및 재무 상태 (Page 10)")
st.markdown("""
[cite_start]'유동 현금 흐름' 요청에 따라, PDF '요약재무제표'의 **'유동자산'** 항목을 기반으로 유동성을 분석합니다. [cite: 208, 211]
""")

# [cite_start]Page 10 '연결재무상태표' 데이터 [cite: 215]
balance_sheet_data = {
    '시점': ['2023.12', '2024.12', '2025.06'],
    '유동자산': [1888752, 1787699, 2302094],
    '유동부채': [1772169, 830932, 789397],
    '자산총계': [5345681, 5479187, 5642564],
    '부채총계': [2235767, 1965408, 2153242]
}
balance_sheet_df = pd.DataFrame(balance_sheet_data).set_index('시점')

# 2025년 6월 유동자산 Metric
latest_assets = balance_sheet_df.loc['2025.06', '유동자산']
prev_assets = balance_sheet_df.loc['2024.12', '유동자산']
delta_assets = latest_assets - prev_assets

st.metric(
    label="유동자산 (2025.06 기준)",
    value=f"{latest_assets:,} 백만원",
    delta=f"{delta_assets:,} 백만원 (2024년 말 대비)"
)

st.write("**주요 재무 상태 요약 (단위: 백만원)**")
st.dataframe(balance_sheet_df, use_container_width=True)


# --- 6. 상세 데이터 (PDF 발췌) ---
st.divider()
st.subheader("📋 상세 재무 데이터 (PDF 발췌)")

if st.checkbox("2분기 실적 상세 내역 보기 (Page 4)"):
    st.write("2Q25 실적 상세 (단위: 백만원)")
    # [cite_start]Page 4 테이블 데이터 [cite: 32]
    page4_data = {
        '구분': ['매출액', '직접 참여형', '  음반/음원', '  공연', '  광고, 출연료', '간접 참여형', '  MD 및 라이선싱', '  콘텐츠', '  팬클럽 등', '영업비용', '영업이익', '영업이익률(%)'],
        '2024 Q2': [640464, 423887, 249554, 143992, 30341, 216577, 109093, 83790, 23693, 589559, 50905, 7.9],
        '2025 Q1': [500613, 322524, 136524, 155152, 30848, 178090, 106401, 41231, 30457, 478991, 21623, 4.3],
        '2025 Q2': [705649, 447858, 228567, 188685, 30606, 257790, 152937, 70221, 34632, 639763, 65886, 9.3]
    }
    page4_df = pd.DataFrame(page4_data).set_index('구분')
    st.dataframe(page4_df, use_container_width=True)

if st.checkbox("요약 손익계산서 전체 보기 (Page 10)"):
    st.write("연결 손익계산서 (단위: 백만원)")
    # [cite_start]Page 10 손익계산서 데이터 [cite: 214]
    income_statement_data = {
        '항목': ['매출액', '매출원가', '매출총이익', '판관비', '영업이익', '영업외수익', '영업외비용', '법인세차감전순이익', '법인세비용', '당기순이익'],
        '2024.2Q': [640464, 394574, 245890, 194985, 50905, 24380, 41578, 33707, 23607, 10100],
        '2024.3Q': [527847, 287363, 240484, 186299, 54185, 12427, 73170, -6557, -8002, 1444],
        '2024.4Q': [726419, 430170, 296249, 231677, 64572, 42291, 135542, -28679, -2605, -26074],
        '2025.1Q': [500613, 282455, 218159, 196536, 21623, 100178, 41586, 80214, 25824, 54390],
        '2025.2Q': [705649, 421355, 284294, 218408, 65886, 65019, 99759, 31146, 15681, 15465]
    }
    income_statement_df = pd.DataFrame(income_statement_data).set_index('항목')
    st.dataframe(income_statement_df, use_container_width=True)
