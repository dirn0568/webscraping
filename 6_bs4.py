import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a element 출력 
# print(soup.a.attrs) # a element 의 속성 정보를 출력
# print(soup.a["href"]) # a element 의 href 속성 '값' 정보를 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # 아랫것보다 이게 더 정확
# print(soup.find(attrs={"class":"Nbtn_upload"}))

# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print('###############################################')
# rank2 = rank1.next_sibling.next_sibling # next_sibling으로 형제노드로 한칸 갈 수 있는데 그 사이에 뭔가 다른게 있어서 그 사이로 갈수도 있음 그럴땐 next_sibling 2개 넣으면됨
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())

# rank2 = rank3.previous_sibling.previous_sibling # next_sibling과 같은 느낌인데 형제관계의 반대 방향으로 움직일때 사용
# print(rank2.a.get_text())

# print('########################################')
# print(rank1.parent) # parent 부모노드로 이동

# rank2 = rank1.find_next_sibling("li") # next_sibling을 여러개 쓰기 귀찮을때 쓰는 코드 형제 노드 중에 다음 li를 찾기
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li")) # 형제들 가져오기 rank1은 안나옴

webtoon = soup.find("a", text="더 복서-휴재 특별편 9화. 아론 타이드") # element 이름이 a 이고 text = X 인걸 찾아달라는 뜻
print(webtoon)
