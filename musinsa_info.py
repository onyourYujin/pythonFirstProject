# 무신사 상품 조건 크롤링

import requests
from bs4 import BeautifulSoup
import csv

def get_product_info(product):
    item_title_element = product.find("p", {"class": "item_title"})
    if item_title_element is not None:
        item_brand_element = item_title_element.find("a")
        if item_brand_element is not None:
            item_brand = item_brand_element.get_text().strip()
        else:
            item_brand = "브랜드 없음"
    else:
        item_brand = "브랜드 없음"

    item_title = product.find("p", {"class": "list_info"}).find("a").get_text().strip()
    item_price = product.find("p", {"class": "price"})

    if item_price is not None:
        item_price_text = item_price.get_text().replace("원", "").replace(",", "").strip()

        try:
            item_price_int = int(item_price_text)
        except ValueError:
            # 정수로 변환할 수 없는 경우 처리
            item_price_int = None

        return item_brand, item_title, item_price_int

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["브랜드명", "상품명", "상품 가격"])

        for item in data:
            writer.writerow(item)

def main():
    url = "https://search.musinsa.com/ranking/best?period=week&age=ALL&mainCategory=&subCategory=&leafCategory=&price=&golf=false&kids=false&newProduct=false&exclusive=false&discount=false&soldOut=false&page=1&viewType=small&priceMin=&priceMax="
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.content, "html.parser")

    ultag = soup.find("ul", {"class": "snap-article-list boxed-article-list article-list center list goods_small_media8"})
    products = ultag.findAll("li", {"class": "li_box"})

    data = []

    for product in products:
        item_brand, item_title, item_price = get_product_info(product)

        # 브랜드는 아디다스, 가격은 150,000원 이하인 상품 찾기
        if item_brand == "아디다스" and (item_price is not None) and (item_price <= 150000):
            data.append([item_brand, item_title, f"{item_price:,}원"])

    if data:
        save_to_csv(data, "musinsa_products.csv")
        print("데이터가 musinsa_products.csv 파일로 저장되었습니다.")

if __name__ == "__main__":
    main()
