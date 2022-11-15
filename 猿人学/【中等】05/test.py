import time
import json
import execjs
import requests
node = execjs.get()
with open('./05_yrx.js', 'r', encoding='utf-8') as f:
    m_code = f.read()
ctx = node.compile(m_code)
funcName = 'getParams'

all = []
for i in range(1, 6):
    url = 'https://match.yuanrenxue.com/api/match/5?page=%d' % i
    result = ctx.call(funcName, )
    print(result)
    proxies={
                'http': 'http://127.0.0.1:8899',
                'https': 'http://127.0.0.1:8899'
            }
    params = {
        'm': result['m'],
        'f': result['f']
    }
    headers = {
        'user-agent': 'yuanrenxue.project',
        #测试过携带m就可以爬到
        'cookie': 'm='+result['cookie_m']+'; '+'RM4hZBv0dDon443M='+result['cookie_rm4']
    }
    resp = requests.get(url, params=params, headers = headers)
    print(resp.text, type(resp))
    data = (json.loads(resp.text))['data']
    all.extend(d['value'] for d in data)

all.sort(reverse=True)
print(all)
total = sum(all[:5])
print(total)


