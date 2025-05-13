import pandas as pd
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한글 폰트 설정 (Windows용)
font_path = "C:/Windows/Fonts/malgun.ttf"  # Windows 사용자는 'Malgun Gothic'


plt.rc('font', family='Malgun Gothic')

# 파일 경로 설정
file_path = "naver_cafe.txt"

# 텍스트 파일 읽기
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# 워드클라우드 생성
wordcloud = WordCloud(
    font_path=font_path,  # 한글 폰트 적용
    width=800, 
    height=400, 
    background_color="white"
).generate(text)

# 워드클라우드 출력
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
