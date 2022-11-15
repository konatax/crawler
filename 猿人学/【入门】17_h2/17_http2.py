import httpx

result = 0
requests = httpx.Client(http2=True)
for i in  range(1, 6):
    url = 'https://match.yuanrenxue.com/api/match/17?page=%d' % i
    headers = {
        'user-agent': 'yuanrenxue.project',
        # 'cookie': 'sessionid=16b4oes8pdbepru5ophsbv6ln8c8d41s; yuanrenxue_cookie=1666227106|5F979yU4qpD5qLCo7CoRIwm1lZaNaLv52BNYb1rSe6mJjQOJIWj4zWbDfv0a77gi1d9agdhStu3vfWneKPvIn0syf3QU1xVpjqZdXv8hN5TxDqCr9dRffsSNqCc4Zjwx49sf6Fyn9re'
        'cookie': 'sessionid=16b4oes8pdbepru5ophsbv6ln8c8d41s'
    }
    resp = requests.get(url, headers=headers).json()
    print(resp)
    data = resp["data"]
    sum = 0
    for d in data:
        value = d["value"]
        sum += value
    result += sum
print(result)