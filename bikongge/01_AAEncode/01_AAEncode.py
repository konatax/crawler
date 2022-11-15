# -*- coding: utf-8 -*-
import re
import json
import requests
import base64
from hashlib import md5
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

for i in range(1,6):
    url = 'http://43.138.37.199:12345/aaencode/api?page=%d' % i
    obj = md5()
    m5 = obj.update(('qiaofu'+'/aaencode/api?page=%d' % i).encode('utf-8'))
    sign = obj.hexdigest()
    print(sign)
    headers = {
        'user-agent': 'apecome.com',
        'sign': sign
    }
    resp = requests.get(url, headers=headers).json()
    print(resp)
    msg = resp["msg"]
    print(msg)
    key = "00000apecome.com".encode('utf-8')
    iv = '0102030405060708'.encode('utf-8')
    data = msg.encode('utf-8')
    data = pad(data, block_size=16, style='pkcs7')
    print(data)
    b = base64.b64decode(data)
    print('b', b)
    aes = AES.new(key=key, mode=AES.MODE_CBC, IV=iv)
    # 要变成这种类型才能解密b'\xb3\xc9\xd2|}\xaa\xb4\x16\xfe\x96\x0f/\
    result = aes.decrypt(b)
    r = unpad(result, block_size=aes.block_size).decode('utf-8')
    print(type(r), r)
    d = re.findall('(\{.*?\})', r)
    print(d)
    for dd in d:
        print(dd)
        dd = json.loads(dd)
        print(dd["name"])
        dd["name"] = dd["name"].encode('utf-8').decode('utf-8')
        print(dd)
