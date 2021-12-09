import urllib.request as req
import json
import pandas as pd
import bs4

library_list = []
add_list = []


# 分段, 處理智慧圖書館
def Smart_library():

    s_librarys = tbodys[0].find_all("a")
    del tbodys[0]
    # print(s_librarys)

    i = 0
    for temp in s_librarys:
        #print(temp.string)
        if temp.string == None:
            temp = str(temp)
            temp = temp.split(">")[1].split("<")[0]
            if i % 2 == 0:
                library_list.append(temp)
                i = i + 1
            else:
                add_list.append(temp)
                i = i + 1
        else:
            if i % 2 == 0:
                library_list.append(temp.string)
                i = i + 1
            else:
                add_list.append(temp.string)
                i = i + 1
    #print(library_list, len(library_list))
    #print(add_list, len(add_list))


# 分段, 處理FastBook全自動借書站
def Fast_library():

    f_librarys = tbodys[0].find_all("a")
    del tbodys[0]
    # print(f_librarys)

    i = 0
    for temp in f_librarys:
        # print(temp.string)
        if temp.string == None:
            temp = str(temp)
            temp = temp.split(">")[1].split("<")[0]
            if i % 2 == 0:
                library_list.append(temp)
                i = i + 1
            else:
                add_list.append(temp)
                i = i + 1
        else:
            if i % 2 == 0:
                library_list.append(temp.string)
                i = i + 1
            else:
                add_list.append(temp.string)
                i = i + 1


# 處理台北剩下 普通圖書館
def local_library():

    a = 1
    for a in range(12):
        l_librarys = tbodys[a].find_all("a")
        #print(l_librarys)

        i = 0
        for temp in l_librarys:
            # print(temp.string)
            if i % 2 == 0:
                library_list.append(temp.string)
                i = i + 1
            else:
                add_list.append(temp.string)
                i = i + 1


# 儲存結果
def save_data():
    # 存入csv
    data = {'圖書館': library_list, '地址': add_list}
    df = pd.DataFrame(data)
    df.to_csv(' Crawler_Library.csv', encoding="utf_8_sig")


if __name__ == '__main__':

    #建立連線網址
    url = "https://tpml.gov.taipei/News_Content.aspx?n=5319E72A2B31CC90&sms=CFFFC938B352678A&s=E997B413EC53833Cl"
    request = req.Request(
        url,
        headers={
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    soup = bs4.BeautifulSoup(data, "html.parser")

    tbodys = soup.find_all("tbody")
    Smart_library()
    Fast_library()
    local_library()
    # print(library_list)
    # print(add_list)
    save_data()

# python3.8
# filename: Crawler_Library.py
# 2021_0802