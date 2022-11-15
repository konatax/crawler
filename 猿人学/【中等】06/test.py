import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs
import urllib
import requests

node = execjs.get()
with open('mytest.js', 'r', encoding='utf-8') as f:
    code = f.read()
ctx = node.compile(code)
funcName = 'getmt'
q = ''
headers = {
    'user-agent': 'yuanrenxue.project',
    'cookie': 'sessionid=nhu43f1nxkazixhebsbqhr3qbo0m4h54'
}
total = 0
for i in range(1, 6):
    result = ctx.call(funcName, i)
    # print(result, type(result))#结果是字典
    t = result['t']
    m = result['m']
    # 或者 q = ''  q += str(i) + '-' + str(t) + "|"都可获取到结果
    q = str(i) + '-' + str(t) + "|"
    # print('t:', t, 'm:', m, 'q:', q)
    # print(urllib.parse.quote(q))#1-1667290325000%7C2-1667290325000%7C3-1667290326000%7C4-1667290326000%7C
#直接放在params当requests.get的参数传递就不用quote
    params = {
        'page': str(i),
        'm': m,
        'q': q
    }
    print(q)
    url = 'https://match.yuanrenxue.com/api/match/6'
    resp = requests.get(url, params=params, headers=headers).json()
    print(resp)
    data = resp['data']
    # 每一期总奖金是该期三等奖的24倍，观察得到
    val = [d['value']*24 for d in data]
    total += sum(val)
print(total)  #6883344  6883344