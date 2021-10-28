import requests
res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status()

print("응답코드:", res.status_code)

if res.status_code == requests.codes.ok:
    print("정상")
else:
    print("실패 [에러코드", res.status_code, "]")

# print(res.text)
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)

