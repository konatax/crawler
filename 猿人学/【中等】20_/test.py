import re
import time

import requests
import hashlib

headers = {
    "user-agent": "yuanrenxue.project",
    "cookie": "sessionid=0e99qsei657h0bfd4wi9mqptfldxenbz"
}

url = "https://match.yuanrenxue.com/api/match/20"


def main():
    num_add_total = 0

    for page_num in range(1, 6):

        timestamp = str(int(time.time() * 1000))
        sign = hashlib.md5((str(page_num) + "|" + timestamp + "D#uqGdcw41pWeNXm").encode()).hexdigest()

        params = {
            "page": page_num,
            "sign": sign,
            "t": timestamp
        }

        response = requests.get(url, headers=headers, params=params)
        print(response.text)
        num_add = 0
        for i in range(10):
            value = response.json()['data'][i]
            num = re.findall(r"'value': (.*?)}", str(value))[0]
            num_add += int(num)

        num_add_total += num_add

    print(num_add_total)


if __name__ == '__main__':
    main()