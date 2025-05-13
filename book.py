from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

# YES24 OS/데이터베이스 종합 베스트셀러 페이지 URL
base_url = "https://www.yes24.com/Product/Category/BestSeller"
category_number = "001001003025"

book_urls = []

# 1~5 페이지까지 크롤링
for page in range(1, 20):
    url = f"{base_url}?categoryNumber={category_number}&pageNumber={page}"
    print(f"현재 페이지: {page}")
    
    # HTML 가져오기
    html = urlopen(url)
    soup = bs(html, "html.parser")

    # 베스트셀러 리스트 (책 목록이 있는 ul 태그)
    table = soup.find('ul', {'id': 'yesBestList'})
    
    # 책 개별 링크 가져오기
    for cont in table.find_all('a', {'class': 'gd_name'}):
        link = 'https://www.yes24.com' + cont.get('href')
        book_urls.append(link)

    time.sleep(1)  # 페이지 변경 간격 조절 (서버 부하 방지)

# 개별 책 상세 정보 가져오기
book_data = []
for index, book_url in enumerate(book_urls):
    book_html = urlopen(book_url)
    book_soup = bs(book_html, "html.parser")

    try:
        title = book_soup.find('h2', {'class': 'gd_name'}).text.strip()
    except:
        title = "정보 없음"

    try:
        author = book_soup.find('span', {'class': 'gd_auth'}).find('a').text.strip()
    except:
        author = "정보 없음"

    try:
        pub = book_soup.find('span', {'class': 'gd_pub'}).text.strip()
    except:
        pub = "정보 없음"

    try:
        price = book_soup.find('span', {'class': 'nor_price'}).text.strip().replace(',', '').replace('원', '')
    except:
        price = "정보 없음"

    print(f"{index+1}. {title} | {author} | {pub} | {price}원")
    
    book_data.append({'제목': title, '저자': author, '출판사': pub, '가격': price, 'Link': book_url})

# 데이터프레임 생성 및 CSV 저장
df = pd.DataFrame(book_data)
df.to_csv("yes24_os_database_bestseller.csv", index=False, encoding='utf-8-sig')

print("\n크롤링 완료! 'yes24_os_database_bestseller.csv' 파일로 저장되었습니다.")
