import base64
import requests

for i in range(1,6):
    url = 'http://43.138.37.199:12345/jsfuck/api?page=%d' % i
    sign = base64.b64encode(('/jsfuck/api?page=%d' % i).encode('utf-8'))
    sign = sign.decode('utf-8')
    headers = {
        'user-agent': 'apecome.com',
        'sign': sign
    }
    resp = requests.get(url, headers=headers).json()
    msg = resp['msg']
    print(msg)
