import pandas as pd
import matplotlib.pyplot as plt

# 한글 폰트 설정 (Windows: Malgun Gothic, Mac: AppleGothic, Linux: NanumGothic)
plt.rc('font', family='Malgun Gothic')  # Windows



# CSV 파일 로드
file_path = "keyword_counts.csv"
df = pd.read_csv(file_path, encoding="utf-8")

# 특정 키워드 필터링 
keywords = ["빅분기", "빅데이터분석기사", "ADsP", "SQLD", "경영정보시각화"]
filtered_df = df[df.iloc[:, 0].astype(str).isin(keywords)]

# 긴 키워드는 줄바꿈 처리
label_mapping = {
    "경영정보시각화": "경영정보\n시각화",
    "빅데이터분석기사": "빅데이터\n분석기사"
}
filtered_df.iloc[:, 0] = filtered_df.iloc[:, 0].replace(label_mapping)

# 필터링된 데이터에서 키워드와 빈도수 가져오기
keywords = filtered_df.iloc[:, 0].tolist()
counts = filtered_df.iloc[:, 1].tolist()

# 막대 그래프 생성
plt.figure(figsize=(10, 6))
plt.bar(keywords, counts, color='skyblue')

# 그래프 레이블 및 제목 설정
plt.xlabel("키워드", fontsize=12)
plt.ylabel("빈도수", fontsize=12)
plt.title("자격뽀 카페", fontsize=14)
plt.xticks(rotation=30, fontsize=12)  # X축 레이블 회전 및 크기 조정

# 그래프 출력
plt.show()
