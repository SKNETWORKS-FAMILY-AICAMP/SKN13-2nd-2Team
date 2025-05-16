import streamlit as st
import pandas as pd

# CSV 파일 경로 정의
TEAM_CSV = "stream_data/kbo_final_team_2025.csv"
ACTIVE_STATS_CSV = "stream_data/kbo_hitters_active_enc.csv"
PREDICTION_CSV = "stream_data/kbo_active_predict.csv"

def show():
    st.title("⚾ KBO 성적에 따른 은퇴 시기 예측")

    # 선수 정보 불러오기 (CSV)
    df = pd.read_csv(TEAM_CSV)

    # 상단 UI
    col1, col2, col3 = st.columns([3, 3, 1])
    with col1:
        teams = ['(선택)', 'KIA', 'KT', 'LG', 'NC', 'SSG', '두산', '롯데', '삼성', '키움', '한화']
        selected_team = st.selectbox("팀 선택", teams)
    with col2:
        filtered_df = df[df['team'] == selected_team] if selected_team != "(선택)" else df
        player_dict = {row["name"]: row["pic_url"] for _, row in filtered_df.iterrows()}
        selected_name = st.selectbox("이름 선택", list(player_dict.keys()) if player_dict else ["선수 없음"])
    with col3:
        st.markdown("<div style='height:25px'></div>", unsafe_allow_html=True)
        search = st.button("검색")

    if search and selected_name in player_dict:
        selected_pic_url = player_dict[selected_name]

        # 선수 기록 불러오기 (CSV)
        stats_df = pd.read_csv(ACTIVE_STATS_CSV)
        stats_df = stats_df[stats_df['pic_url'] == selected_pic_url].sort_values(by='season')

        if not stats_df.empty:
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

                stats_df['OPS'] = stats_df['OBP'] + stats_df['SLG'] if 'OPS' not in stats_df.columns else stats_df['OPS']
                stats_df = stats_df.sort_values(by='season').reset_index(drop=True)

                sum_cols = ['G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'TB', 'RBI',
                            'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'E']
                total = stats_df[sum_cols].sum()

                total_AB = total['AB']
                total_H = total['H']
                total_BB = total['BB']
                total_HBP = total['HBP']
                total_PA = total['PA']
                total_TB = total['TB']

                AVG = total_H / total_AB if total_AB else 0
                OBP = (total_H + total_BB + total_HBP) / total_PA if total_PA else 0
                SLG = total_TB / total_AB if total_AB else 0
                OPS = OBP + SLG

                total_row = {
                    'season': '통산',
                    'AVG': round(AVG, 3),
                    'OBP': round(OBP, 3),
                    'SLG': round(SLG, 3),
                    'OPS': round(OPS, 3),
                    **total
                }

                full_df = pd.concat([stats_df[stat_cols], pd.DataFrame([total_row])[stat_cols]], ignore_index=True)

                # ✅ 통산 기록 강조 적용
                def highlight_total_row(row):
                    if row.name == len(full_df) - 1:
                        return ['font-weight: bold; background-color: #f0f0f0' for _ in row]
                    else:
                        return ['' for _ in row]
                    

                def highlight_last_row(row):
                    return ['font-weight: bold' if row.name == len(full_df) - 1 else '' for _ in row]

                st.dataframe(full_df.style.apply(highlight_last_row, axis=1), use_container_width=True)

            st.markdown("---")

            # ====== 예측 수행 (CSV 기반) ======

            # 예측 결과 CSV 불러오기
            predict_df = pd.read_csv(PREDICTION_CSV)  # 경로는 알맞게 수정해줘

            # pic_url 기준으로 해당 선수의 예측 데이터 찾기
            row = predict_df[predict_df['pic_url'] == selected_pic_url]

            if not row.empty:
                predicted_year = int(row.iloc[0]['predict_year'])
                st.subheader(f"예상 은퇴 시기 : __{predicted_year}__")
                st.caption("사전 예측된 XGBoost 결과 기반입니다.")
            else:
                st.warning("예측 데이터가 없습니다.")

