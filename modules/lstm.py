import streamlit as st
import pandas as pd
import torch
import torch.nn as nn
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# 파일 경로 설정
TEAM_CSV = "stream_data/kbo_final_team_2025.csv"
ACTIVE_STATS_CSV = "stream_data/kbo_hitters_active_enc.csv"
MODEL_PATH = "best_lstm_model.pt"

# 특징 정의
full_features = ['AVG', 'SLG', 'OBP', 'G', 'AB', 'R', 'H', 'HR', 'RBI',
                 'age', 'career_length', 'avg_diff', 'slg_diff', 'obp_diff']

# LSTM 모델 정의
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, dropout):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers,
                            batch_first=True, dropout=dropout)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        _, (h_n, _) = self.lstm(x)
        return self.fc(h_n[-1])

# 모델 로드 함수
def load_model(path):
    model = LSTMModel(input_size=len(full_features), hidden_size=160, num_layers=2, dropout=0.2)
    model.load_state_dict(torch.load(path, map_location=torch.device('cpu')))
    model.eval()
    return model

# 예측 함수
def predict_retire_year(player_df, model):
    scaler = MinMaxScaler()
    scaler.fit(player_df[full_features])
    player_df = player_df.sort_values('season').iloc[-5:]
    player_df[full_features] = scaler.transform(player_df[full_features])
    inputs = torch.tensor(player_df[full_features].values.astype(np.float32)).unsqueeze(0)
    with torch.no_grad():
        prediction = model(inputs).item()
    last_season = player_df['season'].max()
    return round(last_season + prediction)

# Streamlit 앱 시작
def show():
    st.title("⚾ KBO 성적 기반 LSTM 은퇴 시기 예측")

    df = pd.read_csv(TEAM_CSV)

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
        stats_df = pd.read_csv(ACTIVE_STATS_CSV)
        player_df = stats_df[stats_df['pic_url'] == selected_pic_url].copy()

        # if player_df.empty or len(player_df) < 5:
        #     st.warning("해당 선수의 시즌 데이터가 5개 미만입니다.")
        #     return

        # 파생 변수 계산
        player_df['AVG'] = pd.to_numeric(player_df['AVG'], errors='coerce')
        player_df['SLG'] = pd.to_numeric(player_df['SLG'], errors='coerce')
        player_df['OBP'] = pd.to_numeric(player_df['OBP'], errors='coerce')
        player_df['age'] = player_df['season'] - player_df['birth']
        player_df['career_length'] = player_df.groupby('name')['season'].transform('count')
        player_df['avg_diff'] = player_df.groupby('name')['AVG'].diff()
        player_df['slg_diff'] = player_df.groupby('name')['SLG'].diff()
        player_df['obp_diff'] = player_df.groupby('name')['OBP'].diff()
        player_df = player_df.dropna(subset=full_features)

        # if len(player_df) < 5:
        #     st.warning("파생 변수 처리 후 유효한 데이터가 5개 미만입니다.")
        #     return

        model = load_model(MODEL_PATH)
        predicted_year = predict_retire_year(player_df, model)

        st.image(selected_pic_url, width=130, caption=f"{selected_name} 선수")
        st.subheader(f"예상 은퇴 시기 : __{predicted_year}__")
        st.caption("LSTM 모델 기반 예측 결과입니다.")
