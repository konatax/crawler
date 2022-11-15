import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

import execjs
import requests
import json
import re

js = ""

def flush_server():
    global js
    print("加载新的js文件, 以及新的js代码")
    # 先进入首页, 获取到js的url地址
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    resp = requests.get("http://www.iwencai.com/unifiedwap/home/index", headers=headers)

    js_url_re = re.compile(r'<script type="text/javascript" src="(?P<js_code_url>.*?)"></script>', re.S)
    js_url = js_url_re.search(resp.text).group("js_code_url")
    js_url = "http:"+js_url

    js_resp = requests.get(js_url, headers=headers)
    # print(js_resp.text)

    # python基础. 字符串操作. 7
    token_server = js_resp.text[:js_resp.text.find(";") + 1]
    print(token_server)  # var TOKEN_SERVER_TIME=1663945000.422;
    f = open("抠代码.js", mode="r", encoding="utf-8")
    js = execjs.compile(token_server + "\n" + f.read())
    f.close()
    print("新的js已经加载好了.")

def normal_request():
    if not js:
        flush_server()
    hexin_v = js.call("rt.update")
    hexin_v = 'A4NMTaUy5IeqnKhzShVLfRcvEkwo-Bc6UYxbbrVg3-JZdK1yPcinimFc67_G'
    url = "http://www.iwencai.com/customized/chart/get-robot-data"
    data = {
        "question": "20220923涨停",
        "perpage": 50,
        "page": 1,
        "secondary_intent": "stock",
        "log_info": {"input_type": "typewrite"},
        "source": "Ths_iwencai_Xuangu",
        "version": "2.0",
        "query_area": "",
        "block_list": "",
        "add_info": {
            "urp": {
                "scene": 1,
                "company": 1,
                "business": 1
            },
            "contentType": "json",
            "searchInfo": True
        },
        "rsh": "Ths_iwencai_Xuangu_kinvlzk9jrc2swybeox3hyfsko52zugr"
    }

    # 这个代码. 今天跑. 没问题. 但是明天再跑就错了.
    headers = {
        "hexin-v": hexin_v,
        "Referer": "http://www.iwencai.com/unifiedwap/result?w=20220923%E6%B6%A8%E5%81%9C&querytype=stock&addSign=1663935468205",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }

    resp = requests.post(url, data=json.dumps(data), headers=headers)
    return resp.text
    # try:
    #     json.loads(resp.text)
    #     return resp.json()
    # except Exception as e:
    #     flush_server()
    #     return normal_request()

if __name__ == '__main__':
    for i in range(2):  # 最后的测试用. 写代码的时候. 别这么干
        r = normal_request()
        print(r)
