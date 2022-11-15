import requests

url = 'https://match.yuanrenxue.com/static/match/match15/main.wasm'
headers = {
        'user-agent': 'yuanrenxue.project',
        # 'cookie': 'sessionid=16b4oes8pdbepru5ophsbv6ln8c8d41s; yuanrenxue_cookie=1666227106|5F979yU4qpD5qLCo7CoRIwm1lZaNaLv52BNYb1rSe6mJjQOJIWj4zWbDfv0a77gi1d9agdhStu3vfWneKPvIn0syf3QU1xVpjqZdXv8hN5TxDqCr9dRffsSNqCc4Zjwx49sf6Fyn9re'
        'cookie': 'sessionid=16b4oes8pdbepru5ophsbv6ln8c8d41s'
    }
resp = requests.get(url, headers=headers)
# print(resp.text)
# 这种方式存的文件也可以调用
# with open('./ttt.wasm', 'wb') as f:
#     f.write(resp.content)

# 这种方式保存是乱码
# with open('./tttt.txt','w',encoding='utf-8') as f:
#     f.write(resp.text)

with open('./ta.wat','w',encoding='utf-8') as f:
    f.write(resp.text)