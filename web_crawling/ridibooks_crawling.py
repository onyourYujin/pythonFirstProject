from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()
url = "https://ridibooks.com/ebook/recommendation"
browser.get(url)
time.sleep(3)

browser.execute_script("window.scrollTo(0,1080)")
time.sleep(3) 

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

ultag = soup.find("ul",attrs={"class":"fig-1uiiegg"})
oltag = ultag.find_all("ol",attrs={"class":"fig-1smhycv"}) # attrs = {"class":["",""]}
cnt = 0

for ol in oltag:
    books = ol.find_all("li", attrs={"class": "fig-qohjhj"})
    for book in books:
        divtag = book.find("div", attrs={"class": "fig-qsaw8"})
        if divtag is not None:
            title = divtag.find("a").get_text()
            link = divtag.find("a")["href"]
            index = book
            cnt+=1
            print(f"{cnt}위. 제목 : {title}")
            print(f"링크: https://ridibooks.com/ebook/recommendation{link}")
            print("")

browser.find_element(By.XPATH, '//*[@id="__next"]/main/section[4]/div[2]/div[1]/div/ul/li[1]/ol/li[1]/div/div[3]/div/div[1]/a').click()
time.sleep(5) 

browser.quit()