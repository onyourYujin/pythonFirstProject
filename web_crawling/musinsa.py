# bs4라는 라이브러리에서 BeautifulSoup이라는 함수를 불러오겠다는 뜻

import requests
from bs4 import BeautifulSoup

url = "https://search.musinsa.com/ranking/best?period=week&age=ALL&mainCategory=&subCategory=&leafCategory=&price=&golf=false&kids=false&newProduct=false&exclusive=false&discount=false&soldOut=false&page=1&viewType=small&priceMin=&priceMax="
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.content, "html.parser")

ultag = soup.find("ul",{"class":"snap-article-list boxed-article-list article-list center list goods_small_media8"})
products = ultag.findAll("li",{"class":"li_box"})

for product in products:
    item_brand = product.find("p",{"class":"item_title"}).find("a").get_text().strip()
    item_title = product.find("p",{"class":"list_info"}).find("a").get_text().strip()
    item_price = product.find("p",{"class":"price"})

    item_price_text = item_price.get_text().replace("원", "").replace(",", "")

    # 브랜드는 아디다스, 가격은 150,000원 이하인 상품 찾기
    if item_brand == "아디다스" and int(item_price_text)<=150000:
        print("브랜드명:", item_brand)
        print("상품명:", item_title)
        print("상품 가격:", item_price.get_text().strip())
        print()