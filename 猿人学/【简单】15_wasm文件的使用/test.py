import requests
import random
import math
import time
import pywasm
import urllib

def get_m():
    # t1 = parseInt(Date.parse(new Date()) / 1000 / 2);
    # t2 = parseInt(Date.parse(new Date()) / 1000 / 2 - Math.floor(Math.random() * (50) + 1));
    t1 = int(time.time())*1000 // (1000*2)
    t2 = int(time.time())*1000 // (1000*2) - math.floor(random.random() * 50 + 1)
    vm = pywasm.load("./main.wasm")
    result = vm.exec("encode", [t1, t2])
    return str(result) + '|' + str(t1) + '|' + str(t2)

def main():
    result = 0
    for i in range(1,6):
        m = get_m()
        print(m)
        params = {
            'm': m,
            'page': i
        }
        url = 'https://match.yuanrenxue.com/api/match/15'
        headers = {
            'user-agent': 'yuanrenxue.project',
            # 'cookie': 'sessionid=16b4oes8pdbepru5ophsbv6ln8c8d41s; yuanrenxue_cookie=1666227106|5F979yU4qpD5qLCo7CoRIwm1lZaNaLv52BNYb1rSe6mJjQOJIWj4zWbDfv0a77gi1d9agdhStu3vfWneKPvIn0syf3QU1xVpjqZdXv8hN5TxDqCr9dRffsSNqCc4Zjwx49sf6Fyn9re'
            'cookie': 'sessionid=16b4oes8pdbepru5ophsbv6ln8c8d41s'
        }
    #     resp = requests.get(url, headers=headers,params=params).json()
    #     data = resp['data']
    #     sum = 0
    #     for d in data:
    #         value = d["value"]
    #         sum += value
    #     result += sum
    # print(result)
# print(random.random())
# print(math.floor(1.5))
# t1 = int(time.time()) * 1000 // (1000 * 2)
# t2 = int(time.time())*1000 // (1000*2) - math.floor(random.random() * 50 + 1)
# print(t1, t2)
# m = get_m()
# print(m)
if __name__ == '__main__':
    main()