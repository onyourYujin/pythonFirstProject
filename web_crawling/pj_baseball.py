import csv
import requests
from bs4 import BeautifulSoup

url = "https://sports.news.naver.com/kbaseball/record/index?category=kbo&year=2023&type=batter&playerOrder=hra"

filename = "KBO 리그 기록.csv"
f = open(filename, "w", encoding= "utf-8-sig", newline="") 
writer = csv.writer(f)
title = "팀 경기수 승 패 무 승률 게임차 연속 출루율 장타율 최근10경기".split(" ")
writer.writerow(title)

res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")
data_rows = soup.find("div",attrs={"class":"tbl_box"}).find("tbody").find_all("tr")


for row in data_rows:
    columns = row.find_all("td")
    data = [column.get_text() for column in columns]
    writer.writerow(data)
    