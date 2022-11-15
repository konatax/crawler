import asyncio
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

import time
import execjs
import requests

node = execjs.get()
with open('./test.js', 'r', encoding='utf-8') as f:
    code = f.read()
ctx = node.compile(code)
funcName = 'getSign'
sign = ctx.call(funcName, )
url = 'http://spider.wangluozhe.com/challenge/api/3'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'cookie': 'session=7c953d82-6d7c-4830-9c4d-840fc5e5bd62.9uUpdNdw-x7pWukvWD-KUaxCLAk'
}
sign = ctx.call(funcName, )
# print(sign)
data = {
    'page': 1,
    'count': 10,
    '_signature': sign
}
resp = requests.post(url, data=data, headers=headers)
print(resp.text)