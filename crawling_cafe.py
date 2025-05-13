import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

# 네이버 로그인 정보 입력
naver_id = "chltnckd816"  # 본인의 네이버 아이디 입력
naver_pw = "tnckd0816@"  # 본인의 네이버 비밀번호 입력

# 웹드라이버 실행
driver = webdriver.Chrome()
driver.get("https://nid.naver.com/nidlogin.login")

# 로그인 입력창에 아이디 & 비밀번호 입력
time.sleep(2)  # 페이지 로딩 대기
id_input = driver.find_element(By.ID, "id")
pw_input = driver.find_element(By.ID, "pw")

id_input.send_keys(naver_id)
pw_input.send_keys(naver_pw)
pw_input.send_keys(Keys.RETURN)  # 엔터키 입력으로 로그인

time.sleep(5)  # 로그인 후 대기

# 크롤링할 네이버 카페 게시판 URL (첫 페이지로 이동)
cafe_url = "https://cafe.naver.com/sqlpd?iframe_url=/ArticleList.nhn?search.clubid=87425&search.menuid=1"
driver.get(cafe_url)
time.sleep(3)

# iframe 내부로 이동 (네이버 카페는 iframe을 사용함)
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "cafe_main")))
time.sleep(2)

# 키워드별 개수 저장
keyword_counts = {
    "빅데이터분석기사": 0,
    "ADsP": 0,
    "ADP": 0,
    "SQLD": 0,
    "빅분기": 0,
    "경영정보시각화":0
}

# CSV 파일 저장 설정
csv_filename = "naver_cafe_keywords.csv"
with open(csv_filename, mode="w", encoding="utf-8-sig", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["페이지", "빅데이터분석기사", "ADsP", "ADP", "SQLD", "빅분기"])  # CSV 헤더

    current_page = 1  # 현재 페이지 번호
    max_page = 350  # 최대 350페이지까지 크롤링

    while current_page <= max_page:
        try:
            # 페이지 HTML 파싱
            soup = BeautifulSoup(driver.page_source, "html.parser")

            # 전체 게시글 목록 가져오기
            articles = soup.select("table tbody tr")  # 게시글 목록이 있는 태그

            # 현재 페이지 키워드 개수 초기화
            page_counts = {key: 0 for key in keyword_counts.keys()}

            # 키워드 개수 세기
            for article in articles:
                title_tag = article.select_one("td.td_article")  # 게시글 제목이 있는 td 태그
                if title_tag:
                    title_text = title_tag.get_text(strip=True)

                    for keyword in keyword_counts.keys():
                        if keyword in title_text:
                            keyword_counts[keyword] += 1
                            page_counts[keyword] += 1  # 페이지별 카운트

            print(f"페이지 {current_page}: {page_counts}")

            # CSV 파일에 저장 (페이지별 데이터)
            writer.writerow([current_page] + list(page_counts.values()))

            # 다음 페이지 버튼 클릭
            try:
                next_page_button = driver.find_element(By.LINK_TEXT, str(current_page + 1))
                driver.execute_script("arguments[0].click();", next_page_button)
            except:
                # "다음" 버튼이 필요한 경우
                try:
                    next_button = driver.find_element(By.LINK_TEXT, "다음")
                    driver.execute_script("arguments[0].click();", next_button)
                except:
                    print(f"페이지 {current_page}에서 다음 페이지로 이동 불가")
                    break  # 더 이상 페이지가 없으면 종료

            time.sleep(3)  # 페이지 로딩 대기
            current_page += 1

        except Exception as e:
            print(f"Error on page {current_page}: {e}")
            driver.switch_to.default_content()  # 오류 발생 시 iframe에서 빠져나오기

# 결과 출력
print("\n총 키워드 등장 횟수:")
for keyword, count in keyword_counts.items():
    print(f"'{keyword}': {count}개")

# CSV 파일에 최종 키워드 등장 횟수 저장
with open(csv_filename, mode="a", encoding="utf-8-sig", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([])
    writer.writerow(["총합"] + list(keyword_counts.values()))

print(f"\n결과가 '{csv_filename}' 파일로 저장되었습니다.")

# 드라이버 종료
driver.quit()
