import streamlit as st
import pandas as pd
from utils.db import get_engine

def show():
    st.title("⚾ KBO 성적에 따른 은퇴 시기 예측")

    engine = get_engine()

    # 👉 전체 선수 정보 불러오기
    df = pd.read_sql("SELECT name, team, pic_url FROM kbo_final_team_2025", engine)

    # 👉 상단 영역: 팀, 선수 선택, 검색 버튼
    col1, col2, col3 = st.columns([3, 3, 1])
    with col1:
        teams = ['(선택)', 'KIA', 'KT', 'LG', 'NC', 'SSG', '두산', '롯데', '삼성', '키움', '한화']
        selected_team = st.selectbox("팀 선택", teams)
    with col2:
        if selected_team != "(선택)":
            filtered_df = df[df['team'] == selected_team]
        else:
            filtered_df = df
        player_dict = {row["name"]: row["pic_url"] for _, row in filtered_df.iterrows()}
        selected_name = st.selectbox("이름 선택", list(player_dict.keys()) if player_dict else ["선수 없음"])
    with col3:
        st.markdown("<div style='height:25px'></div>", unsafe_allow_html=True)
        search = st.button("검색")

    # 👉 검색 결과 영역
    if search and selected_name in player_dict:
        selected_pic_url = player_dict[selected_name]

        stats_df = pd.read_sql(f"""
            SELECT *
            FROM kbo_active
            WHERE pic_url = '{selected_pic_url}'
            ORDER BY season DESC
        """, engine)

        if not stats_df.empty:
            # 이미지 + 기록
            left, right = st.columns([1, 5])
            with left:
                st.write("")
                st.image(selected_pic_url, width=130, caption=f"{selected_name} 선수")
            with right:
                st.markdown("#### 통산 기록")
                stat_cols = [
                    'season', 'AVG', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'TB',
                    'RBI', 'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'SLG', 'OBP', 'OPS', 'E'
                ]

                # OPS 계산 (없을 경우 생성)
                if 'OPS' not in stats_df.columns:
                    stats_df['OPS'] = stats_df['OBP'] + stats_df['SLG']

                # 시즌 오름차순 정렬
                stats_df = stats_df.sort_values(by='season', ascending=True).reset_index(drop=True)

                # 통산 계산
                sum_cols = ['G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'TB', 'RBI',
                            'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'E']
                total = stats_df[sum_cols].sum()

                # 평균 계산용 값 추출
                total_AB = total['AB']
                total_H = total['H']
                total_BB = total['BB']
                total_HBP = total['HBP']
                total_PA = total['PA']
                total_TB = total['TB']
                total_SF = 0  # 희생플라이 없으면 0으로 가정

                # AVG, OBP, SLG, OPS 계산
                AVG = total_H / total_AB if total_AB else 0
                OBP = (total_H + total_BB + total_HBP) / total_PA if total_PA else 0
                SLG = total_TB / total_AB if total_AB else 0
                OPS = OBP + SLG

                # 통산 row 만들기
                total_row = {
                    'season': '통산',
                    'AVG': round(AVG, 3),
                    'OBP': round(OBP, 3),
                    'SLG': round(SLG, 3),
                    'OPS': round(OPS, 3),
                    **total
                }

                # 정리된 순서대로 넣기
                full_df = pd.concat([stats_df[stat_cols], pd.DataFrame([total_row])[stat_cols]], ignore_index=True)

                # 스타일링: 마지막 행 굵게
                def highlight_last_row(row):
                    return ['font-weight: bold' if row.name == len(full_df) - 1 else '' for _ in row]

                st.dataframe(full_df.style.apply(highlight_last_row, axis=1), use_container_width=True)

            # 예측 결과 (샘플)
            st.markdown("---")
            st.subheader(f"예상 은퇴 시기 : __{stats_df['season'].max() + 2}__")  # 예시
            st.caption("예상 은퇴 시기의 통산 data 예측")
        else:
            st.warning("해당 선수의 기록이 없습니다.")
