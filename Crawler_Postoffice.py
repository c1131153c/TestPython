import urllib.request as req
import pandas as pd
import bs4

po_list = []
add_list = []
city_list = []

url = "https://www.post.gov.tw/post/internet/I_location/index_all.html"
request = req.Request(
    url,
    headers={
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    })
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

soup = bs4.BeautifulSoup(data, "html.parser")
adds = soup.find_all("td", class_="detail")
titles = soup.find_all("a", class_="rwd-open")
#print(adds)
#print(titles)

# 處理縣市
for city in adds:
    #print(city.string[0:3])
    city_list.append(city.string[0:3])

# 處理地址
for address in adds:
    #print(address.string)
    add_list.append(address.string)

# 處理局名
i = 0
for po in titles:
    if i % 2 != 0:
        i = i + 1
        continue
    else:
        i = i + 1
        #print(po.string)
        po_list.append(po.string)

# 存入csv
data = {'縣市': city_list, '局名': po_list, '地址': add_list}
df = pd.DataFrame(data)
df.to_csv('Crawler_Postoffice.csv', encoding="utf_8_sig")

# python3.8
# filename: Crawler_Postoffice.py
# 2021_0730