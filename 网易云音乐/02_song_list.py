import requests
import json
import base64
import threading
from concurrent.futures import ThreadPoolExecutor     #线程池
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# 以下是每首歌曲解密
def b(data, key):
    data = data.encode('utf-8')
    key = key.encode('utf-8')
    data = pad(data, 16)
    aes = AES.new(key=key,IV=b'0102030405060708',mode=AES.MODE_CBC)
    bs = aes.encrypt(data)
    # 此时bs是二进制  需要编码为base64格式二进制再解码为字符串
    return base64.b64encode(bs).decode()

def d(data, key):
    i = '0J2zASPj8k68yRcH'
    encText = b(data, key)
    encText = b(encText, i)
    encSecKey = '8c67f19d04950d368dc713ed0da5b5854cd7c67f423dc9b778ee62fd7dbb756260bcf42f1f760c5365a617f3e5b70263eab7523659d34b31f92eab288569bd5aafd6770a84bf7f1f23cb8afd80acbaf0db53591b2529d49168e646524b6add297b62282b9a5e6dac8220364bf92ac9e2ab9e7b7561f91b0418a70d453c50e5a1'
    return encText, encSecKey

def url_main(id,urls):
    url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=8b46f61d3cc338246866723f2ce87ce2'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    # 这里必须用两个{}
    data = f'{{"ids":"[{id}]","level":"standard","encodeType":"aac","csrf_token":"8b46f61d3cc338246866723f2ce87ce2"}}'
    print(data)
    encText, encSecKey = d(data, '0CoJUm6Qyw8W8jud')
    # print(encText,encSecKey)
    dic = {
        "params": encText,
        "encSecKey": encSecKey
    }
    resp = requests.post(url, data=dic, headers=headers).json()
    url = resp["data"][0]["url"]
    urls.append(url)

# 以下是歌曲列表解密
def o(data, key):
    key = key.encode('utf-8')
    data = data.encode('utf-8')
    data = pad(data, 16)
    aes = AES.new(key=key,IV=b"0102030405060708",mode=AES.MODE_CBC)
    bs = aes.encrypt(data)
    # 将字节编码为base64字节再解码为字符串
    return base64.b64encode(bs).decode()

def en(data, key):
    s = "adDE8czVTKXmWSOU"
    encText = o(data, key)
    encText = o(encText, s)
    encSecKey = "92061bc8eb49ced2ecb96ace64d23ea2244fbd3e76673af95ae775fafca86c7518d961ddb005781a6b3a83a17a322f47557ae7ed71cc440271a50b22175bb18966b7cad465c94e559044c4e972abc80d37bbade7373edcc9b67b377c9551c6aae114d599aca513d4e5819fc6537c4fe74021492eb1baea5b0c8680f895dfd8b0"
    return encText, encSecKey

def download(url, d):
    filename = d["name"]+".m4a"
    print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'
    }
    content = requests.get(url,headers=headers).content
    with open('./'+filename,'wb') as f:
        f.write(content)
    print(d["name"]+"下载完成")

def list_main():
    data = {
        "id": "2571114602",
        "n": 1000,
        "shareUserId": 0
    }
    data = json.dumps(data)
    encText, encSecKey = en(data, '0CoJUm6Qyw8W8jud')
    url = 'https://interface.music.163.com/weapi/v6/playlist/detail'
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'
    }
    dic = {
        "params": encText,
        "encSecKey": encSecKey
    }
    resp = requests.post(url,data=dic,headers=headers).json()
    l = resp["playlist"]["tracks"]
    ll = []
    for dic in l:
        d = {}
        d["name"] = dic["name"]
        d["id"] = dic["id"]
        ll.append(d)
    # print(ll)
    # print(len(ll))  #10
    urls = []
    for i in range(len(ll)):
        # 将id传入单首歌曲解密里的data中的id列表，就可获取每首歌的url
        # print(ll[i]["id"],type(ll[i]["id"]))  int类型
        url_main(ll[i]["id"],urls)
    print(urls,len(urls))

#     多线程下载歌曲
# 线程池 统一管理 线程   并发数5
    pool = ThreadPoolExecutor(5)
    for i in range(len(urls)):
        if urls[i]:
            # th = threading.Thread(target=download, args=(urls[i],ll[i]))
            # th.start()
            pool.submit(download, urls[i], ll[i])
        else:
            continue




if __name__ == '__main__':
    list_main()
