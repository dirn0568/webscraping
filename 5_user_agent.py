import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
# User-Agent가 있어야 페이지 정보를 가져올 수 있는 사이트가 있음
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("mycoding.html", "w", encoding="utf8") as f:
    f.write(res.text)

