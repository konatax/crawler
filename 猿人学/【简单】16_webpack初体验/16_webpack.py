import requests
import execjs
import time

values = []
for i in range(1, 6):
    p_s = int(time.time())*1000
    node = execjs.get()
    with open('./test.js', 'r', encoding='utf-8') as f:
        code = f.read()
    ctx = node.compile(code)
    funcName = 'getM'
    m = ctx.call(funcName, str(p_s))
    print(m)
    params = {
        'page': str(i),
        'm': m,
        't': str(p_s)
    }
    url = 'https://match.yuanrenxue.com/api/match/16'
    headers = {
        'User-Agent': 'yuanrenxue.project',
        'cookie': 'sessionid=263me1ydxd8xwrwsvn7bz5m0gv5rw1s3'
    }
    resp = requests.get(url, headers=headers, params=params)
    print(resp.text)
    values += [_.get('value') for _ in resp.json().get('data')]
print(sum(values))
