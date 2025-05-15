import streamlit as st
import pandas as pd
import pickle
from utils.db import get_engine

def show():
    st.title("⚾ KBO 성적에 따른 은퇴 시기 예측")

    engine = get_engine()

    # 선수 정보 불러오기
    df = pd.read_sql("SELECT name, team, pic_url FROM kbo_final_team_2025", engine)

    # 상단 UI
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

    if search and selected_name in player_dict:
        selected_pic_url = player_dict[selected_name]

        # 선수 기록 불러오기
        stats_df = pd.read_sql(f"""
            SELECT *
            FROM kbo_active
            WHERE pic_url = '{selected_pic_url}'
            ORDER BY season DESC
        """, engine)

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

                if 'OPS' not in stats_df.columns:
                    stats_df['OPS'] = stats_df['OBP'] + stats_df['SLG']

                stats_df = stats_df.sort_values(by='season', ascending=True).reset_index(drop=True)

                sum_cols = ['G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'TB', 'RBI',
                            'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'E']
                total = stats_df[sum_cols].sum()

                total_AB = total['AB']
                total_H = total['H']
                total_BB = total['BB']
                total_HBP = total['HBP']
                total_PA = total['PA']
                total_TB = total['TB']
                total_SF = 0

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

                def highlight_last_row(row):
                    return ['font-weight: bold' if row.name == len(full_df) - 1 else '' for _ in row]

                st.dataframe(full_df.style.apply(highlight_last_row, axis=1), use_container_width=True)

            st.markdown("---")

            # ====== 예측 수행 ======

            # birth 가져오기
            birth_query = f"""
                SELECT birth FROM kbo_active
                WHERE pic_url = '{selected_pic_url}' LIMIT 1
            """
            birth_result = pd.read_sql(birth_query, engine)
            if birth_result.empty:
                st.error("선수의 생년 정보를 찾을 수 없습니다.")
                return

            birth = birth_result.iloc[0]['birth']

            # 모델 로드
            with open('kbo_xgb_model.pkl', 'rb') as f:
                model = pickle.load(f)

            # 입력 데이터 구성
            input_data = pd.DataFrame([{
                **total,
                'AVG': AVG,
                'OBP': OBP,
                'SLG': SLG,
                'OPS': OPS,
                'active_year': stats_df['season'].nunique(),
                'birth': birth
            }])

            # 전처리
            input_data = pd.get_dummies(input_data)

            model_columns = model.get_booster().feature_names
            for col in model_columns:
                if col not in input_data.columns:
                    input_data[col] = 0
            input_data = input_data[model_columns]

            # 예측
            predicted_age = model.predict(input_data)[0]
            predicted_year = int(birth + predicted_age)

            # 결과 표시
            st.subheader(f"예상 은퇴 시기 : __{predicted_year}__")
            st.caption("XGBoost 회귀 모델 기반 예측 결과입니다.")
        else:
            st.warning("해당 선수의 기록이 없습니다.")
