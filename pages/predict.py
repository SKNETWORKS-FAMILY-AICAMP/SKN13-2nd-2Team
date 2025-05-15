import streamlit as st
import pandas as pd
from utils.db import get_connection
import pymysql


# 메인 함수 정의
def show():
    st.title("야구선수 은퇴 예측")
    st.write("해당 야구선수가 언제 은퇴할지, 어떤 통산 기록을 가지고 은퇴할지 예측")

import streamlit as st
import pandas as pd
import pymysql
from utils.db import get_connection


# DB 연결
conn = get_connection()

# 1️⃣ 선수의 마지막 시즌 팀 추출
query = """
SELECT pic_url, name, MAX(season) AS last_season, team
FROM kbo_active
GROUP BY pic_url, name;
"""
last_team_df = pd.read_sql(query, conn)

# 2️⃣ 팀 리스트 생성
team_list = sorted(last_team_df['team'].unique())
selected_team = st.selectbox("팀 선택", team_list)

# 3️⃣ 팀에 해당하는 선수 필터링
filtered_players = last_team_df[last_team_df['team'] == selected_team]
selected_player = st.selectbox("선수 선택", filtered_players['name'] + " - " + filtered_players['pic_url'])

# 4️⃣ pic_url 기준 추출
if st.button("검색"):
    # pic_url 가져오기
    pic_url = selected_player.split(" - ")[1]

    # 해당 선수의 가장 최근 기록 가져오기
    player_stats_query = f"""
    SELECT * FROM kbo_active
    WHERE pic_url = '{pic_url}'
    ORDER BY season DESC
    LIMIT 1;
    """
    player_row = pd.read_sql(player_stats_query, conn)

    if not player_row.empty:
        st.image(pic_url, width=200)
        st.write("📊 최근 시즌 주요 스탯:")
        st.dataframe(player_row[['AVG', 'G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'SO', 'SLG', 'OBP']])
    else:
        st.warning("선수 정보를 찾을 수 없습니다.")

conn.close()
