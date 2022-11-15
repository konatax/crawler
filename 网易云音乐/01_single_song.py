import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import requests

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

def main():
    url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=8b46f61d3cc338246866723f2ce87ce2'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    data = '{"ids":"[1442466883,1346310082]","level":"standard","encodeType":"aac","csrf_token":"8b46f61d3cc338246866723f2ce87ce2"}'
    encText, encSecKey = d(data, '0CoJUm6Qyw8W8jud')
    # print(encText,encSecKey)
    dic = {
        "params": encText,
        "encSecKey": encSecKey
    }

    resp = requests.post(url, data=dic, headers=headers).json()
    # url = resp["data"][0]["url"]
    # print(url)
    print(resp)
#     如果data的id列表中传入多个id，那么就能得到多首歌曲的url
#     {'data': [{'id': 1442466883, 'url': 'http://m10.music.126.net/20220923175752/23a3a84193ebd175f048f6a762c7ef34/yyaac/obj/wonDkMOGw6XDiTHCmMOi/2268610298/90ee/7e21/e2da/72932e99239017ad6befa5879f1a684b.m4a', 'br': 96000, 'size': 2924549, 'md5': '72932e99239017ad6befa5879f1a684b', 'code': 200, 'expi': 1200, 'type': 'm4a', 'gain': 0.0, 'fee': 8, 'uf': None, 'payed': 0, 'flag': 260, 'canExtend': False, 'freeTrialInfo': None, 'level': 'standard', 'encodeType': 'aac', 'freeTrialPrivilege': {'resConsumable': False, 'userConsumable': False, 'listenType': None}, 'freeTimeTrialPrivilege': {'resConsumable': False, 'userConsumable': False, 'type': 0, 'remainTime': 0}, 'urlSource': 0, 'rightSource': 0, 'podcastCtrp': None, 'effectTypes': None, 'time': 240169}, {'id': 1346310082, 'url': 'http://m701.music.126.net/20220923175752/179683f16713ae9db9d07c4d2b8335a2/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/14411562479/73c1/b236/0e52/59751d5e455019bc354d165f04940b9d.m4a', 'br': 96005, 'size': 3182226, 'md5': '59751d5e455019bc354d165f04940b9d', 'code': 200, 'expi': 1200, 'type': 'm4a', 'gain': 0.0, 'fee': 0, 'uf': None, 'payed': 0, 'flag': 256, 'canExtend': False, 'freeTrialInfo': None, 'level': 'standard', 'encodeType': 'aac', 'freeTrialPrivilege': {'resConsumable': False, 'userConsumable': False, 'listenType': None}, 'freeTimeTrialPrivilege': {'resConsumable': False, 'userConsumable': False, 'type': 0, 'remainTime': 0}, 'urlSource': 0, 'rightSource': 0, 'podcastCtrp': None, 'effectTypes': None, 'time': 261306}], 'code': 200}
#
if __name__ == '__main__':
    main()