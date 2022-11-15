import re
import requests
import urllib3
import execjs
import urllib

session = requests.Session()
session.cookies.update({"sessionid": "16b4oes8pdbepru5ophsbv6ln8c8d41s"})
headers = {
    'user-agent': 'yuanrenxue.project',
}

proxies={
            'http': 'http://127.0.0.1:8888',
            'https': 'http://127.0.0.1:8888'
        }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
resp = session.get('https://match.yuanrenxue.com/match/13', headers=headers)
# 用这个方法会报错，相当于没登陆，无法获取四五页的内容
# sessionid = requests.utils.dict_from_cookiejar(resp.cookies).get('sessionid')
# session.cookies.update({"sessionid": sessionid})
print(resp.text)
co = resp.text.replace(r"+';path=/';location.href=location.pathname+location.search</script>", '').replace("<script>", '')
# co = (resp.text).replace('document.cookie=', '').replace("('", '').replace("')", '').replace('+','').replace("';path=/",'')
print(co)
node = execjs.get()
code = """function getYuanrenxueCookie(text) {
    var document = {};
    return eval(text)
};"""
ctx = node.compile(code)
funcName = 'getYuanrenxueCookie'
yuan_cookie = ctx.call(funcName, co)
yuanrenxue_cookie = yuan_cookie.replace('yuanrenxue_cookie=', '')
session.cookies.update({"yuanrenxue_cookie": yuanrenxue_cookie})
# cookie['sessionid'] = requests.utils.dict_from_cookiejar(resp.cookies).get('sessionid') #如果想动态获取
# cookie['sessionid'] = 'qc9f9wv20aam1r5fmuynqqfjfbt77f6f'  # 直接用自己的就可以

session.headers=headers
result = 0
for i in range(1,6):

    url = 'https://match.yuanrenxue.com/api/match/13?page=%d' % i
    resp = session.get(url).json()
    print('resp', resp)
    data = resp["data"]
    sum = 0
    for d in data:
        value = d["value"]
        sum += value
    result += sum
print(result)


