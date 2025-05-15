import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 한글 글꼴 설정 (맑은 고딕)
plt.rcParams['font.family'] = 'Malgun Gothic'

st.set_page_config(page_title="MLB 데이터 앱", layout="wide")

# 사이드바 페이지 선택
page = st.sidebar.selectbox(
    "📂 페이지 선택",
    ("📊 선수은퇴나이 예측", "📈 Info", "ℹ️ 팀소개")
)


# 페이지 1: 통산 기록 보기
if page == "📊 선수은퇴나이 예측":
    st.title("📊 선수은퇴나이 예측")

    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # 👇 작은 크기의 그래프 + 한글 글꼴 적용됨
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.plot(x, y, label='사인 함수', color='blue')
    ax.set_title("사인 곡선")
    ax.set_xlabel("X 값")
    ax.set_ylabel("Y 값")
    ax.legend()

    st.pyplot(fig)

    # 그래프 별 예제 코드
    # 예제 데이터 
    # np.random.seed(42)
    # x = np.arange(1, 11)
    # y1 = np.random.randint(10, 100, size=10)
    # y2 = np.random.randint(50, 150, size=10)

    # df = pd.DataFrame({
    #     "X": x,
    #     "A 그룹": y1,
    #     "B 그룹": y2
    # })

    # # 선 그래프
    # st.subheader("📊 선 그래프")
    # st.line_chart(df.set_index("X"))

    # # 바 그래프
    # st.subheader("📊 바 그래프")
    # st.bar_chart(df.set_index("X"))

    # # 산점도 (Matplotlib 사용)
    # st.subheader("📌 산점도 (Matplotlib)")
    # fig, ax = plt.subplots()
    # ax.scatter(df["A 그룹"], df["B 그룹"], color='tomato')
    # ax.set_xlabel("A 그룹")
    # ax.set_ylabel("B 그룹")
    # ax.set_title("A vs B 산점도")
    # st.pyplot(fig)


# 페이지 2: 시각화
elif page == "📈 모델설명":
    st.title("📈 모델설명")


# 페이지 3: 소개
elif page == "ℹ️ 소개":
    st.title("ℹ️ 프로젝트 소개")
    st.markdown("""
    이 앱은 MLB 선수들의 통산 기록 데이터를 탐색하고 시각화하기 위해 만들어졌습니다.

    **기능:**
    - 통산 기록 테이블 페이지네이션
    - 주요 지표 시각화
    - 스트림릿 사이드바 기반 페이지 전환

    **제작:** 당신의 이름 😊
    """)