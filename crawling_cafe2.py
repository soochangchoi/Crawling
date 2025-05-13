from bs4 import BeautifulSoup
import time
from selenium import webdriver
import csv

# -----------------------------
# 1. 네이버 카페 크롤링 결과 저장
# -----------------------------
with open("naver_cafe.txt", mode='w', encoding='utf-8') as file:
    for page in range(1, 50):
        driver = webdriver.Chrome()
        driver.get(
            f'https://cafe.naver.com/sqlpd?iframe_url=/ArticleList.nhn%3Fsearch.clubid=21771779%26search.menuid=2%26userDisplay'
            f'=50%26search.boardtype=L%26search.specialmenutype=%26search.totalCount=501%26search.cafeId=21771779%26search.page={page}'
        )

        # iframe 전환
        driver.switch_to.frame("cafe_main")
        time.sleep(2)  # 페이지 로딩 대기

        soup = BeautifulSoup(driver.page_source, "html.parser")

        # 크롤링한 제목 리스트 선택
        titles = soup.select('a.article')

        for title in titles:
            title_text = title.text.strip()
            print(title_text)  # 콘솔 출력 확인
            file.write(title_text + "\n")  # 텍스트 파일에 저장

        driver.quit()  # 브라우저 종료
        time.sleep(1)  # 페이지 변경 간격 조절

print("\n크롤링 완료! 'naver_cafe.txt' 파일로 저장되었습니다.")

# ----------------------------------------
# 2. 키워드 등장 횟수 분석 및 CSV 파일 생성
# ----------------------------------------
# 분석할 키워드 목록 설정
keywords = ['빅데이터 분석가', '빅분기', 'SQLD', 'ADsP', 'ADP', '경영정보시각화']
keyword_counts = {keyword: 0 for keyword in keywords}

# 크롤링 결과 파일 읽기
with open("naver_cafe.txt", mode='r', encoding='utf-8') as file:
    for line in file:
        for keyword in keywords:
            keyword_counts[keyword] += line.count(keyword)

# 콘솔에 결과 출력
for keyword, count in keyword_counts.items():
    print(f"{keyword}: {count}")

# 결과를 CSV 파일로 저장
with open("keyword_counts.csv", mode='w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Keyword", "Count"])  # CSV 헤더 작성
    for keyword, count in keyword_counts.items():
        writer.writerow([keyword, count])

print("CSV 파일 'keyword_counts.csv'로 저장되었습니다.")
