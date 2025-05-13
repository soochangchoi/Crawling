import pandas as pd
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# CSV 파일 불러오기
df = pd.read_csv("yes24_os_database_bestseller_titles.csv", encoding='utf-8-sig')

# 텍스트 데이터 생성 (책 제목)
text_data = ' '.join(df['제목'].astype(str))

# 책 모양의 마스크 이미지 불러오기
mask = np.array(Image.open("light.png"))

# 워드클라우드 생성 (마스크 적용)
wordcloud = WordCloud(font_path='malgun.ttf',
                      width=800,
                      height=400,
                      background_color='white',
                      mask=mask).generate(text_data)

# 그래프 출력
plt.figure(figsize=(15, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
