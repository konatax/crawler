import cv2
import requests
import numpy as np


"""===============================获取背景图和滑块图==============================="""
# url = 'https://verify.snssdk.com/captcha/get?lang=zh&app_name=juejin_web&h5_sdk_version=2.23.5&sdk_version=&iid=0&did=0&device_id=0&ch=web_text&aid=2608&os_type=2&mode=&tmp=1668234783887&platform=pc&webdriver=false&fp=verify_ladjg7hl_i3DvoEEJ_iicM_4PLn_Asbt_UtmD1XRmMZCL&subtype=&challenge_code=3058&os_name=windows'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
# }
# resp = requests.get(url, headers=headers).json()
# data = resp['data']['question']
# template_jpg = data['url1']
# block_png = data['url2']
# print(template_jpg)
# print(block_png)
# with open('background.jpg', 'wb') as f:
#     f.write(requests.get(template_jpg, headers=headers).content)
# with open('block.jpg', 'wb') as f:
#     f.write(requests.get(block_png, headers=headers).content)
"""===============================模板匹配==============================="""
#导入图片
background = cv2.imread('background.jpg')
block = cv2.imread('block.jpg')
# 去除滑块周围的空白
min_x = 255
min_y = 255
max_x = 0
max_y = 0
for x in range(1, block.shape[0]):
    for y in range(1, block.shape[1]):
        t = set(block[x, y])
        if len(t) >= 2:
            if x <= min_x:
                min_x = x
            elif x >= max_x:
                max_x = x

            if y <= min_y:
                min_y = y
            elif y >= max_y:
                max_y = y
block = block[min_x:max_x, min_y: max_y]

ba_shape = background.shape
bl_shape = block.shape
# print(ba_shape, bl_shape)  #(344, 552, 3) (110, 110, 3)   高 宽 通道
# 转为灰度图
ba_gray = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
bl_gray = cv2.cvtColor(block, cv2.COLOR_BGR2GRAY)
#在背景图中匹配滑块  第一个参数是待搜索图像 第二个参数是模板图像  参数result=None 匹配结果   cv2.TM_CCOEFF_NORMED归一化相关系数匹配法
result = cv2.matchTemplate(ba_gray, bl_gray, cv2.TM_CCOEFF_NORMED)
# 获取最佳匹配结果
value = cv2.minMaxLoc(result)
print(value) #(最小值，最大值，最小值坐标，最大值坐标)
# dis = value[2:][0][0]  #最小值x坐标
# tem = value[2:][1][0]  #最大值x坐标
# print(dis, tem)
#后面画框的定点
tl = value[2]
br = (bl_shape[1]+tl[0], bl_shape[0]+tl[1])  #(x,y)
# 绘制矩形边框，将匹配区域标注出来
# target：目标图像
# tl：矩形定点
# br：矩形的宽高
# (0,0,255)：矩形边框颜色
# 1：矩形边框大小
cv2.rectangle(ba_gray, tl, br, (0, 0, 255), 2)
# cv2.imshow('Image', ba_gray)
# cv2.waitKey(0)
print(tl[0])





