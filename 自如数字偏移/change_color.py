import cv2
import time
import json
import base64
import requests
from aip import AipOcr
import numpy as np

# img = cv2.imread('./yellow.jpg', cv2.IMREAD_COLOR)  #[30,150,255]  BGR
# print(type(img))  #np.array
# #膨胀操作
# kernel = np.ones(shape=[3,3],dtype=np.uint8)
# img2 = cv2.dilate(img, kernel, iterations=1)
# cv2.imshow('img', img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# APP_ID = '28067874'
# API_KEY = 'l5BmOn6geHb2sw3BhS0nMylL'
# SECRET_KEY = 'hoXHVYoEm7qNoVdqdcIxMrIPUiM0fkRE'
#
# client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
# # 字体转换到图片时可以尝试几种字体大小（行索引那里，然后测试网页转换的字体正确率怎么样
# with open('red.jpg', 'rb') as f:
#     r = client.basicGeneral(f.read())
# print(r)
def base64_api(img):
    data = {"username": 'q6035945', "password": 'q6035945', "typeid": 3, "image": img}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""

with open('./yellow.jpg', 'rb') as f:
    s = f.read()
#转成base64
bs = base64.b64encode(s)
print(bs)
print(base64_api(bs.decode('utf-8')))