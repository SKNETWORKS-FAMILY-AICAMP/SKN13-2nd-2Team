# SKN13-2nd-2Team

> SK Networks AI Camp 13기  
>  
> 개발기간: 25/05/15 - 25/05/16  
<br>

# 0. 팀 소개

### ⚾ 팀명:  
**미정 (작성 시 입력해주세요)**

<br>

### ⚾ 팀원 소개  
<table align=center>
  <tbody>
   <tr>
      <td align=center><b>이유나</b></td>
      <td align=center><b>모지호</b></td>
      <td align=center><b>장시인</b></td>
      <td align=center><b>우민규</b></td>
    </tr>
    <tr>
      <td align="center">
          <img alt="Image" src="" width="200px;" alt="이유나"/>
      </td>
      <td align="center">
          <img alt="Image" src="" width="200px;" alt="모지호"/>
      </td>
      <td align="center">
        <img alt="Image" src="" width="200px;" alt="장시인" />
      </td>
      <td align="center">
        <img alt="Image" src="" width="200px;" alt="우민규"/>
      </td>
    </tr>
    <tr>
       <td align="center">
       <a href="https://github.com/yowon7">
         <img src="https://img.shields.io/badge/GitHub-yowon7-F1BFCA?logo=github" alt="이유나 GitHub"/>
       </a>
       </td>
       <td align="center">
       <a href="https://github.com/mojiho">
         <img src="https://img.shields.io/badge/GitHub-mojiho-9AC5F4?logo=github" alt="모지호 GitHub"/>
       </a>
       </td>
       <td align="center">
       <a href="https://github.com/SeanJang92">
         <img src="https://img.shields.io/badge/GitHub-SeanJang92-FFD59E?logo=github" alt="장시인 GitHub"/>
       </a>
       </td>
       <td align="center">
       <a href="https://github.com/mingyu-oo">
         <img src="https://img.shields.io/badge/GitHub-mingyu--oo-CDE990?logo=github" alt="우민규 GitHub"/>
       </a>
       </td>
    </tr>
  </tbody>
</table>
<br>

# 1. 프로젝트 개요

### ⚾ 프로젝트 명
- **현재 활동 중인 KBO 선수! 과연 은퇴 시기는 ?!**

### ⚾ 목표
- KBO 리그에서 활약했던 은퇴 타자들의 데이터를 기반으로, 현재 활동 중인 타자의 **은퇴 시점 예측 모델**을 개발한다.
- 데이터 분석 및 머신러닝(Machine Learning) 기법을 활용하여 타자의 커리어 패턴을 이해하고, 이를 바탕으로 향후 리그 이탈 가능성을 예측한다.

### ⚾ 프로젝트 배경
- 한국 프로야구(KBO)에서는 매 시즌 수많은 선수들이 은퇴하고, 또 신인이 데뷔한다.
- 선수의 은퇴는 팬들뿐 아니라 구단 운영 및 스포츠 산업 전반에도 중요한 이슈다.
- 선수 데이터를 체계적으로 분석하고 은퇴 시점을 예측함으로써, **선수 관리 전략**, **스카우팅**, **팀 운영계획 수립** 등에 활용할 수 있는 데이터 기반 인사이트를 제공하고자 한다.

### ⚾ 기대 효과
- KBO 선수의 커리어 예측이라는 현실적인 주제를 통해 **현실 데이터에 기반한 AI 적용 사례 제시**
- 선수 관리 및 팀 전력 분석에 활용 가능한 **정량적 기준 확보**
- 향후 타 종목이나 다른 예측 분야(예: 이직 예측, 커리어 전환 예측)로 **모델 확장 가능성 제시**

### ⚾ 요약
- **데이터 수집**: 은퇴한 타자들의 통산 성적을 웹 크롤링으로 수집  
- **전처리 및 EDA**: 주요 성적 지표 정제, 커리어 기간 기준 정리  
- **모델링**: 분류/회귀 모델로 은퇴 시기 예측  
- **배포**: Streamlit을 활용한 웹 서비스로 시각화 제공  
<br>

# 2. 기술 스택
>
|🛠 협업 및 문서화 |
|------------------|
|![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=Discord&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white)  |

|💻 도구  |
|----------|
|![VSCode](https://img.shields.io/badge/VScode-007ACC?style=for-the-badge&logo=Visual-Studio-Code&logoColor=white) |

|😺 형상 관리|
|------------|
|![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white)  |

|🚀 프로그래밍 언어  |
|---------------------|
|![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white)  |

|📊 데이터 분석  |
|-----------------|
|![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=Pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=NumPy&logoColor=white)  |

|🤖 머신러닝  |
|--------------|
|![Scikit-Learn](https://img.shields.io/badge/Scikit%20Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)  |

|📈 데이터 시각화  |
|-------------------|
|![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=Matplotlib&logoColor=white) ![Seaborn](https://img.shields.io/badge/Seaborn-4C8CBF?style=for-the-badge&logo=Seaborn&logoColor=white)  |

|🔗 대시보드  |
|--------------|
|![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)  |

<br>

----


---

# 3. WBS
><br>
># ✅ KBO 타자 은퇴 예측 프로젝트

## 📅 Day 1

### 오전
- 프로젝트 목표 명확화
  - 예측 목표 설정 (예: 은퇴 여부 예측 or 은퇴 시기 예측)
  - 평가 지표 설정 (정확도, MAE 등)
- 필요한 통산 기록 항목 정리
  - 예: 경기수, 타석, 타율, 홈런, 도루, WAR 등
- 크롤링 대상 사이트 구조 파악
  - KBO 기록실 홈페이지
- Kaggle에서 야구 데이터 서치

### 오후
- 타자 통산 기록 크롤링 코드 작성
  - 은퇴 타자 리스트 수집
  - 현역 타자 리스트 수집
- 은퇴 여부 or 은퇴 시점 라벨링
  - 예: 은퇴년도 존재 여부로 라벨 생성

---

## 📅 Day 2

### 오전
- 전처리 작업
  - 결측치 처리, 숫자형 변환
  - 불필요한 컬럼 제거
  - 파생 변수 컬럼 생성
- 간단한 예측 모델 개발
  - 예: Logistic Regression, RandomForestClassifier, XGBoost 등
- 훈련/검증 데이터 분리

### 오후
- 모델 평가 및 결과 시각화
  - 정확도, confusion matrix, feature importance 등
- Streamlit 또는 Jupyter Notebook으로 결과 정리
- 회고 및 발표자료 작성
  - 프로젝트 요약, 문제 해결 과정, 주요 결과 정리



# 4. 데이터 전처리 결과서 (EDA)
>
>
> **1) 데이터 내용 확인**
>
>| 변수명        | 변수 설명              | 데이터 타입 |
>|---------------|------------------------|--------------|
>| name          | 선수 이름              | text         |
>| birth         | 출생 연도              | bigint       |
>| G             | 경기 수                | bigint       |
>| PA            | 타석 수                | bigint       |
>| AB            | 타수                   | bigint       |
>| R             | 득점                   | bigint       |
>| H             | 안타                   | bigint       |
>| 2B            | 2루타                  | bigint       |
>| 3B            | 3루타                  | bigint       |
>| HR            | 홈런                   | bigint       |
>| TB            | 루타 (총 누적 베이스) | bigint       |
>| RBI           | 타점                   | bigint       |
>| SB            | 도루                   | bigint       |
>| CS            | 도루 실패              | bigint       |
>| BB            | 볼넷                   | bigint       |
>| HBP           | 사구 (몸에 맞는 공)   | bigint       |
>| SO            | 삼진                   | bigint       |
>| GDP           | 병살타                 | bigint       |
>| E             | 실책                   | bigint       |
>| active_year   | 활동 연도 수 (last - first + 1) | bigint  |
>| pic_url       | 선수 사진 URL          | text         |
>| first_year    | 데뷔 연도              | bigint       |
>| last_year     | 마지막 연도            | bigint       |
>| AVG           | 타율                   | double       |
>| OBP           | 출루율                 | double       |
>| SLG           | 장타율                 | double       |
>| OPS           | 출루율 + 장타율        | double       |

> 
>
> **2) 결측치 확인**
><br>
>
>
>
>**3) 이상치 확인 및 인코딩**
><br>
>
>
>**4) 데이터 시각화**
>
>
>

----

# 5. 인공지능 학습 결과서


---


# 6. 수행결과



---



# 7. 한 줄 회고
