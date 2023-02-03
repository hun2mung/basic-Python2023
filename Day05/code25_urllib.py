# urllib 패키지 불러오기

from urllib.request import Request, urlopen

req = Request('https://www.naver.com')         # 생성자
res = urlopen(req)
print(res.status)

