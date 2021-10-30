import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30"}

for i in range(1, 6):
    print("페이지", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor=".format(i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    #print(res.text)
    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    # print(items[0].find("div", attrs={"class":"name"}).get_text())
    for item in items:

        # 광고 제품은 제외
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            continue

        name = item.find("div", attrs={"class":"name"}).get_text() # 제품명

        # 애플 제품 제외
        if "Apple" in name:
            continue

        price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격
        
        rate = item.find("em", attrs={"class":"rating"}) # 평점
        if rate:
            rate = rate.get_text()
        else:
            rate = "평점 없음"
            continue

        rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) # 평점 수
        if rate_cnt:
            rate_cnt = rate_cnt.get_text() # 예 : (26)
            rate_cnt = rate_cnt[1:-1]
        else:
            rate_cnt = "평점 수 없음"
            continue
        
        link = item.find("a", attrs={"class":"search-product-link"})["href"]
        # link = item.a["href"]

        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            # print(name, price, rate, rate_cnt)
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_cnt}개)")
            print(f"https://www.coupang.com{link}")
            print("-"*100) #줄긋기