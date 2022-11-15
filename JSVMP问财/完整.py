import re
import json
import execjs
import requests

ctx = ""
def flush_server():
    global ctx
    js_url = 'http://s.thsi.cn/js/chameleon/chameleon.min.1668152.js'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    resp = requests.get(js_url, headers=headers).text
    token_server_time = re.findall('(var TOKEN_SERVER_TIME.*?;)', resp, re.S)[0]
    print(token_server_time)
    node = execjs.get()
    with open('./ttt.js', 'r', encoding='utf-8') as f:
        code = f.read()
    ctx = node.compile(token_server_time+'\n'+code)

def normal_request():
    if not ctx:  #如果没有更新js代码
        flush_server()
    funcName = 'getHexinV'
    hexin_v = ctx.call(funcName,)
    url = "http://www.iwencai.com/customized/chart/get-robot-data"
    headers = {
        "hexin-v": hexin_v,
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
    try:
        return resp.json()
    except Exception as e:
        #如果报错应该是网络不好，重新请求就好了
        flush_server()
        return normal_request()

if __name__ == '__main__':
    resp = normal_request()
    datas = resp["data"]["answer"][0]["txt"][0]["content"]["components"][0]["data"]["datas"]
    print(datas)
    print(len(datas))