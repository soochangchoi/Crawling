from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# 크롬 드라이버 설정
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 브라우저 창 없이 실행
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 웹드라이버 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 크롤링할 페이지 URL (자격뽀 네이버 카페 게시판)
url = "https://cafe.naver.com/mseller?iframe_url=/ArticleList.nhn?search.clubid=30720660&search.menuid=1&search.page=1"
driver.get(url)
time.sleep(3)  # 페이지 로딩 대기

# iframe 내부로 전환 (네이버 카페 게시글 리스트는 iframe 내부에 있음)
driver.switch_to.frame("cafe_main")  # 네이버 카페는 iframe이 포함되어 있음

# 게시글 리스트 크롤링
articles = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

data_list = []
for article in articles:
    try:
        # 게시글 제목
        title_element = article.find_element(By.CSS_SELECTOR, "td.td_article > div.board-list div.article")
        title = title_element.text.strip()

        # 게시글 링크
        link = title_element.find_element(By.TAG_NAME, "a").get_attribute("href")

        # 작성자
        writer = article.find_element(By.CSS_SELECTOR, "td.td_name").text.strip()

        # 작성 날짜
        date = article.find_element(By.CSS_SELECTOR, "td.td_date").text.strip()

        # 조회수
        views = article.find_element(By.CSS_SELECTOR, "td.td_view").text.strip()

        data_list.append([title, link, writer, date, views])
    
    except Exception as e:
        print("오류 발생:", e)

# 크롤링 데이터 저장
df = pd.DataFrame(data_list, columns=["제목", "링크", "작성자", "날짜", "조회수"])
df.to_csv("naver_cafe_articles.csv", index=False, encoding="utf-8-sig")

# 종료
driver.quit()

print("✅ 크롤링 완료! 데이터가 'naver_cafe_articles.csv' 파일로 저장되었습니다.")
