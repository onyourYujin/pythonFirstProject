from tkinter import *
import requests
from bs4 import BeautifulSoup

url ="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%9C%A0%EB%A1%9C"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

won_naver_str = soup.find("div",attrs={"class":"price_info"}).find("strong").get_text()
won_naver_str = won_naver_str.replace(",", "")  # str인 ","가 들어오면 int나 float로 변경 불가
won_naver = float(won_naver_str)

def money_convert():
    euro = int(EURO_input.get())  # type : str => float으로 바꿔주기
    money_calculate = euro * won_naver
    result.config(text=f"{money_calculate:.2f}")  # 숫자를 label에 넣으려면 str 형태로 바꿔야 함

# 새로운 window 화면 설정
window = Tk()
window.title("EURO to WON converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Entry
EURO_input = Entry(width=7)
EURO_input.grid(column=1, row=0)


# Labels
euro = Label(text="EURO")
euro.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

won = Label(text="WON")
won.grid(column=2,row=1)

result = Label(text="0")
result.grid(column=1,row=1)


# Buttons
calculate_button = Button(text="Calculate", command=money_convert)  # 괄호 안에 함수를 넣을 때 괄호 빼고(클릭 했을 때만 메소드 호출)
calculate_button.grid(column=1, row=2)


window.mainloop()