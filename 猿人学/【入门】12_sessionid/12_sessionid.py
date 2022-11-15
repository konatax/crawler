import requests
import base64
import urllib

result = 0
for i in range(1,6):
    headers = {
        'user-agent': 'yuanrenxue.project',
        'cookie': 'sessionid=qc9f9wv20aam1r5fmuynqqfjfbt77f6f'
    }
    m = base64.b64encode(('yuanrenxue' + str(i)).encode()).decode()
    m = urllib.parse.quote(m)
    url = 'https://match.yuanrenxue.com/api/match/12?page=%d&m=%s' % (i, m)
    # print(url)
    resp = requests.get(url, headers=headers).json()
    data = resp["data"]
    sum = 0
    for d in data:
        value = d["value"]
        sum += value
    result += sum
print(result)