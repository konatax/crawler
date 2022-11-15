import re
import urllib
import requests
import execjs
#！！！！这里是动态获取cookie(已经保存在session中)和token，这两个必须配套

url = 'https://fanyi.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
session = requests.Session()
resp = session.get(url, headers=headers)
resp = session.get(url, headers=headers)  #第二次请求才有token
# print(resp.text)
# print(session.cookies)
cookie = requests.utils.dict_from_cookiejar(session.cookies)
# print('cookie', cookie)
cookie = (urllib.parse.urlencode(cookie)).split('&')[0]
# headers["Cookie"] = cookie
headers["Referer"] = "https://fanyi.baidu.com/"
headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
# print('cookie', cookie)
print(headers)
token = re.findall("token: '(.*?)',", resp.text)[0]
# print(token)
node = execjs.get()
with open("./code.js","r",encoding="utf-8") as f:
    code = f.read()
ctx = node.compile(code)
funcName = "getSign"
word = input("输入单词：")
sign = ctx.call(funcName, word)
data = {
    "from": "en",
    "to": "zh",
    "query": word,
    "transtype": "realtime",
    "simple_means_flag": "3",
    "sign": sign,
    "token": token,
    "domain": "common"
}
new_url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
rr = session.post(new_url, headers=headers, data=data).json()
print(rr["dict_result"]["simple_means"]["word_means"])