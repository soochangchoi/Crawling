import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

# 한글 폰트 설정 (Windows 기준)
from matplotlib import font_manager, rc
font_path = 'C:/Windows/Fonts/malgun.ttf'  # 맑은 고딕 폰트
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 데이터 로드 (파일명을 직접 확인하여 수정)
data = pd.read_csv('yes24_os_database_bestseller_titles.csv')

# 제목에서 단어 추출 및 빈도 계산
titles = data.iloc[:, 0].astype(str)  # 제목이 있는 열 지정
words = ' '.join(titles).lower()
words = re.findall(r'\b\w+\b', words)

# 가장 많이 나온 단어 15개
word_counts = Counter(words)
common_words = word_counts.most_common(15)

# 데이터 준비
keywords, counts = zip(*common_words)

# 그래프 그리기
plt.figure(figsize=(15, 7))
plt.barh(keywords[::-1], counts[::-1], color='skyblue')
plt.xlabel('빈도수', fontsize=14)
plt.ylabel('키워드', fontsize=14)
plt.title('제목에서 자주 나온 키워드 TOP 15', fontsize=15)

# y축 글씨 크기 설정 (추가된 부분)
plt.yticks(fontsize=16)  

plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
