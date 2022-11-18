import time
import random
import execjs
import requests
while True:
    url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Referer': 'https://fanyi.youdao.com/',
        'Cookie': 'xxxxxxxxxxxxxxxxxx'
    }
    e = input('enter a English word:')
    if e == 'q':
        break
    r = str(int(time.time()*1000))                     #时间戳以毫秒为单位
    i = r + str(int(random.random()*10))               #时间戳加噪声 比时间戳多一位 random.random() 产生0~1随机浮点数
    with open('js_code.js','r',encoding='utf-8') as f:
        code = f.read()
    node = execjs.get()
    ctx = node.compile(code)
    funcName = 'getSign("{0}","{1}")'.format(e,i)
    sign = ctx.eval(funcName)
    # print(sign)
    form_data = {
        "i": e,                                        #输入的单词
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": i,                                    #
        "sign": sign,
        "lts": r,
        "bv": "50b61ff102560ebc7bb0148b22d7715c",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }

    # result = requests.post(url,headers=headers,data=form_data)
    # print(result,type(result),type(result.json())) 
    # <Response [200]> <class 'requests.models.Response'> <class 'dict'>
    try:
        result_parser = requests.post(url,headers=headers,data=form_data).json()   #解析为字典
        result = result_parser['smartResult']['entries'][1]
        print(result)
    except:
        print('plz enter a corret English word')
        continue
