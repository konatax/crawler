import requests
import urllib
import execjs
#这里是直接复制页面显示的cookie的BAIDUID和token，这两个必须配套

def get_cookie(headers):
    url = "https://fanyi.baidu.com/translate?query=&keyfrom=baidu&smartresult=dict&lang=auto2zh#en/zh/"
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    # print(resp.cookies.get_dict())
    cookie = urllib.parse.urlencode(resp.cookies.get_dict()).replace("&","; ")
    return cookie

def get_sign(word):
    node = execjs.get()
    with open("./code.js","r",encoding="utf-8") as f:
        code = f.read()
    ctx = node.compile(code)
    funcName = "getSign"
    sign = ctx.call(funcName, word)
    # print(sign)
    return sign

def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "cookie": "BAIDUID=850C02CF225E4F3E9D177CC2146F26DF:FG=1",
        "Referer": "https://fanyi.baidu.com/",
        # "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    # cookie = get_cookie(headers)
    # headers["cookie"] = cookie
    # headers["Cookie"] = "094764A058BA61B4EA052B53364FF28F:FG=1"
    # headers["Referer"] = "https://fanyi.baidu.com/"
    # headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
    # headers["Acs-Token"] = "1665126299348_1665200038642_nAu8k8agT24BDO1DHuT7sdh4Ltk/pDjtHi8U5ErCRgyPeJTU6R4fzfxggOdXI0qaGXHtGKHq9lUZXT0mBGdqJdNEIa9XG9+ch7KQaPM1JbFS6pHe2bT6ke8Vmexg0OzhCeXUMyqGPhyMU9keLPtKk0JZ77RcX8nfrMnkTJTpuD4xdzexl1Y5kXmt4r/t8YBV3QjiCDGYVrNVumMM1oj8SYRJkmuenOcrmzN/kedymxXut42Zpjfpz4yVFirApz2lX1QD2wtJlVr2eJ57YU0K35eAAYlnMJyefrqroNlZpRnCIOGFsdzBa3y/NbhzfRKA"
    # headers["Host"] = "fanyi.baidu.com"
    # print(headers)
    word = input("输入单词：")
    sign = get_sign(word)
    print(sign)
    data = {
        "from": "en",
        "to": "zh",
        "query": word,
        "transtype": "realtime",
        "simple_means_flag": "3",
        "sign": sign,
        "token": "0a79c73dce9dd314d2d1bfffd8cdb922",
        "domain": "common"
    }
    url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
    resp = requests.post(url, headers=headers, data=data)
    print(resp.text)
    print("\u672a\u77e5\u9519\u8bef".encode("utf-8").decode("utf-8"))
if __name__ == "__main__":
    main()