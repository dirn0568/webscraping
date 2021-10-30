import requests
from bs4 import BeautifulSoup

# res = requests.get("https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=2019%EB%85%84+%EC%98%81%ED%99%94+%EC%88%9C%EC%9C%84")
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# images = soup.find_all("img", attrs={"class":"thumb_img"})

# enumerate 이미지 파일과 함꼐 순서도 매겨주는거 같음
for i in range(2019, 2015, -1):
    res = requests.get("https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q={}%EB%85%84+%EC%98%81%ED%99%94+%EC%88%9C%EC%9C%84".format(i))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})
    for idx, image in enumerate(images):
        # print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        
        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        # 이미지 파일은 글자가 아닌 데이터 = wb
        with open("movie_{}_{}.jpg".format(i,idx+1), "wb") as f:
            f.write(image_res.content)

        if idx >= 4:
            break
