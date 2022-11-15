import requests
import time
import execjs
import urllib
#第一页 https://match.yuanrenxue.com/api/match/1?m=060d1aa8bd9757848b9470a2d3e2c653%E4%B8%A81666173661
#第二页 https://match.yuanrenxue.com/api/match/1?page=2&m=54d7fb42c2ef1fb5d0d30b9e056a8ac8%E4%B8%A81666174023
#m 的值需要逆向
# 和int(time.time()*1000)不一样
t = int(time.time())*1000 + (16798545 + -72936737 + 156138192)
print(t)
node = execjs.get()
# with open('./get_windowf.js','r',encoding='utf-8') as f:
with open('./ttt.js','r',encoding='utf-8') as f:
    code = f.read()
ctx = node.compile(code)
funcName = 'get_windowf'
ff = ctx.call(funcName, str(t))
m = ff + '丨' + str(t // (-1 * 3483 + -9059 + 13542));
print(m)
url = 'https://match.yuanrenxue.com/api/match/1'

headers = {
    'user-agent': 'yuanrenxue.project',
    }
v = 0
l = 0
for i in range(1,6):
    params = {
        "page": i,
        "m": m
    }
    resp = requests.get(url, headers=headers,params=params).json()
    data = resp["data"]
    l += len(data)
    for d in data:
        v += d["value"]

ave = v/l
print(ave)