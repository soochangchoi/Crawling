# 📚 Cafe & Book Data Analysis Project

네이버 카페 게시글 키워드 분석 및 YES24 데이터베이스/OS 베스트셀러 도서 데이터를 크롤링하고,  
분석 및 시각화를 통해 데이터 인사이트를 제공합니다.

---

## 🛠 기술 스택

- Python 3.9
- Selenium
- BeautifulSoup4
- Pandas
- Matplotlib
- WordCloud
- PIL (Pillow)

---

## 📂 프로젝트 구성

| 구분        | 주요 기능                                        | 스크립트                    |
|-----------|--------------------------------------------|---------------------------|
| 카페 크롤링   | 네이버 카페 게시글 크롤링 및 키워드 등장 횟수 분석                | `crawling_cafe.py`, `crawling_cafe2.py`, `자격뽀.py` |
| 카페 분석    | 키워드 워드클라우드 생성, 키워드 빈도 막대그래프 시각화             | `cafe_word_cloud.py`, `데이터포럼카페.py` |
| 도서 크롤링   | YES24 OS/DB 베스트셀러 도서 크롤링 (책 제목, 저자, 출판사, 가격) | `book.py`, `book copy.py` |
| 도서 분석    | 책 제목 기반 키워드 빈도 분석, 워드클라우드 생성                 | `bookgraph.py`, `bookwordcloud.py` |

---

## ▶ 실행 순서

### 1. 카페 크롤링
```bash
cd cafe_crawling
python crawling_cafe.py
python crawling_cafe2.py
python 자격뽀.py
