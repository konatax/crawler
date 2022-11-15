#http://www.iwencai.com/unifiedmobile/?q=20221110%E6%B6%A8%E5%81%9C&queryType=stock#/result?question=20221110%E6%B6%A8%E5%81%9C&queryType=stock&sign=1668151275358
#旧版网页才是对的
#hexin-v 参数逆向
import json
import execjs
import requests

node = execjs.get()
with open("./ttt.js", "r", encoding="utf-8") as f:
    code = f.read()
ctx = node.compile(code)
funcName = "getHexinV"
hexinV = ctx.call(funcName,)
# print(hexinV)
hexinV = 'A4NMTaUy5IeqnKhzShVLfRcvEkwo-Bc6UYxbbrVg3-JZdK1yPcinimFc67_G'
url = "http://www.iwencai.com/customized/chart/get-robot-data"
headers = {
    "hexin-v": hexinV,
    "Referer": "http://www.iwencai.com/unifiedwap/result?w=20221110%E6%B6%A8%E5%81%9C&querytype=stock&addSign=1668148009045",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }

data = {
        "question": "20221110涨停",
        "perpage": 68,
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
        "rsh": "Ths_iwencai_Xuangu_lii2u6z2rb88kfq23k9usy1m8eqhslr0"
    }

resp = requests.post(url, data=json.dumps(data), headers=headers)
print(resp.text)