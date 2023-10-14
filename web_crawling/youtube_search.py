from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()


SEARCH_KEYWORD = "크리스마스 playlist".replace(" ","+")
URL = "https://www.youtube.com/results?search_query=" + SEARCH_KEYWORD
browser.get(URL)
time.sleep(5)
    
soup = BeautifulSoup(browser.page_source, 'html.parser')


# 이용약관 동의 
reject = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[1]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()

    
content_atag = soup.find_all('a', {'id': 'video-title'})
content_data = []

for link in content_atag[:5]:
    content_title = link.get('title')
    content_link = "https://youtube.com" + link.get("href")

    content_data.append({'title': content_title, 'link': content_link})

df = pandas.DataFrame(content_data)
df.to_csv("content.csv",encoding="utf-8-sig")
        
browser.quit()