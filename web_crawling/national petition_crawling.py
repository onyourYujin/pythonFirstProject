# 국민 동의 청원, 동적인 사이트에서 페이지 넘겨 가면서 청원 제목 가져오는 크롤링 프로그램

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()

url = "https://petitions.assembly.go.kr/status/onGoing?start=1"
browser.get(url)
time.sleep(2)

for _ in range(3):
    soup = BeautifulSoup(browser.page_source, "html.parser")  # html
    tag = soup.find("div", attrs={"class": "ListDiv"}).find("ul")

    for litag in tag.find_all("li"): 
        ultag = litag.find("div", attrs={"class": "BoxWrap"})
        if ultag:  # AttributeError NoneType -> 'ultag'가 존재하는 경우에만 'a' 요소 찾기
            atag = ultag.find("a")
            if atag:  # 'a' 요소가 존재하는 경우에만 제목 가져오기
                title = atag.find("dl").find("dd").get_text()
                print(title)
    
    next_button = browser.find_element(By.XPATH, '//*[@id="contentsbody"]/div/div/div[4]/div[3]/ul/li[6]/a')
    next_button.click()
    time.sleep(2) 

browser.quit()



# ==============================================================================
page_number = 1

while True:
    url = f"https://petitions.assembly.go.kr/status/onGoing?start={page_number}"
    browser.get(url)

    time.sleep(5)
    
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    # 화면 가장 아래로 스크롤 내리기
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    tag = soup.find("div", attrs={"class": "ListDiv"}).find("ul")

    for litag in tag.find_all("li"):  # li 태그 반복
        ultag = litag.find("div", attrs={"class": "BoxWrap"})
        if ultag:  # AttributeError NoneType -> 'ultag'가 존재하는 경우에만 'a' 요소 찾기
            atag = ultag.find("a")
            if atag:  # 'a' 요소가 존재하는 경우에만 제목 가져오기
                title = atag.find("dl").find("dd").get_text()
                print(title)

    try:
        next_button = browser.find_element(By.LINK_TEXT, '다음')  # 수정된 부분
        next_button.click()
        page_number += 1

    except:
        break  # 다음 페이지가 없으면 종료

browser.quit()