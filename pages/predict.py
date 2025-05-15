import streamlit as st
import pandas as pd
from utils.db import get_connection

st.title("🏟️ KBO 선수 최종 시즌 정보 조회")

# DB 연결
conn = get_connection()

# 🔍 1. 각 선수의 마지막 시즌 정보 (pic_url 기준)
query = """
SELECT t.pic_url, t.name, t.team, t.season
FROM kbo_active t
WHERE t.season = (
    SELECT MAX(t2.season)
    FROM kbo_active t2
    WHERE t2.pic_url = t.pic_url
)
"""
latest_df = pd.read_sql(query, conn)

# ✅ 팀 선택
teams = sorted(latest_df['team'].unique())
selected_team = st.selectbox("팀을 선택하세요", teams)

# ✅ 팀에 해당하는 선수 필터링
team_players = latest_df[latest_df['team'] == selected_team]
player_labels = team_players['name'] + " - " + team_players['pic_url']
selected_player_label = st.selectbox("선수를 선택하세요", player_labels)

# ✅ 검색 버튼
if st.button("검색"):
    selected_pic_url = selected_player_label.split(" - ")[1]

    # 해당 선수의 가장 최근 시즌 정보 가져오기
    stat_query = f"""
    SELECT *
    FROM kbo_active
    WHERE pic_url = '{selected_pic_url}'
    ORDER BY season DESC
    LIMIT 1
    """
    stat_df = pd.read_sql(stat_query, conn)

    if not stat_df.empty:
        st.image(selected_pic_url, width=200)
        st.markdown(f"### 🧾 {stat_df.iloc[0]['name']} 선수의 시즌 기록")

        stat_cols = ['AVG', 'G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'SO', 'SLG', 'OBP']
        st.dataframe(stat_df[stat_cols])
    else:
        st.warning("선수 정보를 찾을 수 없습니다.")

conn.close()
