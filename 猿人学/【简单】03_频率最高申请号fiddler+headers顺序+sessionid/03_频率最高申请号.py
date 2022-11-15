import requests
import urllib3
#第一页 https://match.yuanrenxue.com/api/match/3
#第二页 https://match.yuanrenxue.com/api/match/3?page=2


# headers通过fiddler抓包查看  顺序不能变
headers = {
    'Host': 'match.yuanrenxue.com',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    # 因为第四第五页浏览器无法查看
    'User-Agent': 'yuanrenxue.project',
    'sec-ch-ua-platform': "Windows",
    'Accept': '*/*',
    'Origin': 'https://match.yuanrenxue.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://match.yuanrenxue.com/match/3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cookie': 'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1666144656; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1666144656; qpfccr=true; no-alert3=true; sessionid=; tk=1292553875106502182; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1666146598; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1666147394'
    # 'Cookie': 'sessionid=;'
}
proxies = {
    "http": "http://localhost:8888",
    "https": "http://localhost:8888",
}
session = requests.Session()
# session.headers 里面参数顺序就不会变了
session.headers = headers
session.cookies['Cookie'] = ''
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# 由于请求头是在fiddler获取，因此需要加上fiddler的代理
data_list = []
for i in range(1,6):
    url = 'https://match.yuanrenxue.com/api/match/3?page=%d' % i
    session.post('https://match.yuanrenxue.com/jssm', proxies=proxies, verify=False)
    response = requests.utils.dict_from_cookiejar(session.cookies)
    sessionid = response['sessionid']
    session.headers['sessionid'] = sessionid
    print(sessionid)
    resp = session.get(url, proxies=proxies, verify=False).json()
    for d in resp["data"]:
        data_list.append(d["value"])
max_count = max(data_list,key=data_list.count)  #关键词是列表中元素出现的次数
print(max_count)
# {'sessionid': '15388a737blg2cvkikr2ieg0r1e7gifr'}