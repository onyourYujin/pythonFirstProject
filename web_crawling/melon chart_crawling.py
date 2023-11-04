from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()

URL = "https://www.melon.com/chart/index.htm"
browser.get(URL)
time.sleep(5)

trtags = browser.find_elements(By.CLASS_NAME, 'lst50')  # 여러 요소 -> find_elements

for j,i in enumerate(trtags[:10]): 
    song_info = i.find_elements(By.TAG_NAME, "td")[5]
    title = song_info.find_element(By.CLASS_NAME, "ellipsis.rank01").find_element(By.TAG_NAME, "a").text
    artist = song_info.find_element(By.CLASS_NAME, "ellipsis.rank02").find_element(By.TAG_NAME, "a").text
    like = i.find_elements(By.TAG_NAME, "td")[7].find_element(By.CLASS_NAME, "cnt").text

    print(f"{j+1}위")
    print(f"노래 제목: {title}")
    print(f"가수: {artist}")
    print(f"좋아요 수: {like[:2]}")
    print("         ")