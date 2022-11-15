import time
import base64
import requests


# window._signature = btoa(Date.now())  Date.now() = 1667954735995
url = 'http://spider.wangluozhe.com/challenge/api/9'
headers = {
    # 'Host': 'spider.wangluozhe.com',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '51',
    # 'Accept': 'application/json, text/javascript, */*; q=0.01',
    # 'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Origin': 'http://spider.wangluozhe.com',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'v=A4g1_bTDf-ua1ZNF7Nga0u-AWf2fMezEzpTAvEI71rj2SCYj6kG8yx6lkEyR; session=85fa876c-984a-4e55-8426-d32588907af4.uY_ISWk0OFIYlPQBuplTQv2lyNY',
    }


t = int(time.time()*1000)
print(t)
sign = base64.b64encode(str(t).encode()).decode()
print(sign)
data = {
    'page': 3,
    'count': 10,
    '_signature': sign
}
proxies = {
    'http': 'http://127.0.0.1:8899',
    'https': 'http://127.0.0.1:8899'
}
resp = requests.post(url, headers=headers)
print(resp.status_code)

