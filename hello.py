import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
# a = soup.select_one('#old_content > table > tbody > tr:nth-child(3) > td.title > div > a')
# print(a['href'])

#old_content > table > tbody > tr:nth-child(2)
#old_content > table > tbody > tr:nth-child(3) > td.title > div > a

trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    # print(tr)
    a = tr.select_one('td.title > div > a')
    # print(a)
    if a is not None:
        print(a.text)