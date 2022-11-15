import re
import requests
from lxml import etree
from urllib.parse import urljoin
# url = 'http://bikongge.com/chapter_1/font_2/index.html'
# resp = requests.get(url)
# print(resp.text)
# tree = etree.HTML(resp.text)
# # 字体文件链接在style里面
# style = tree.xpath('//style/text()')[0]
# # print(style)
# font_url = re.findall(', url\("(.*?woff)"\)', style, re.S)[0]
# font_url = urljoin(url, font_url)
# # print(font_url)
# # 下载字体文件
# font_resp = requests.get(font_url)
# with open('font.woff', 'wb') as f:
#     f.write(font_resp.content)
"""==========================================================================="""
# 获取字体文件的unicode
from fontTools.ttLib import ttFont
ttf = ttFont.TTFont("font.woff")  #打开字体文件
uni_list = ttf.getGlyphOrder()[2:]   #按顺序读取  #'glyph00000', 'x'这两个字符是空的可以去掉
# print(uni_list)
#字体文件中 字符的格式 "uniE7F1" 要修改成 "\uiE7F1"
uni_ok_list = []
for uni in uni_list:
    uni = uni.replace('uni', '\\u')
    uni_ok_list.append(uni)
print(uni_ok_list, len(uni_ok_list))
"""======================================================================"""
# 按照字体文件中的字形，把上述unicode画出来
# from PIL import Image
# from PIL import ImageFont
# from PIL import ImageDraw
# #创建画布
# img = Image.new('RGB', (800,800), color=(255,255,255))
# #创建画笔
# img_draw = ImageDraw.Draw(img)
# #创建字体
# img_font = ImageFont.truetype('font.woff', 40)  #字体大小40
#
# #只有10个数字，一行画完
# line = []
# for i in range(len(uni_ok_list)):
#     #字符转码，就能打印出看得懂的字
#     uni = uni_ok_list[i]
#     uni = uni.encode().decode("unicode-escape")
#     line.append(uni)
# line_s = ''.join(line)
# img_draw.text((20, 45), line_s, fill=1, font=img_font)
# img.save('tu.jpg')

"""==========================================================================================="""
#识别上面保存的图片里的文字
# from aip import AipOcr
# """ 你的 APPID AK SK """
# APP_ID = '28067874'
# API_KEY = 'l5BmOn6geHb2sw3BhS0nMylL'
# SECRET_KEY = 'hoXHVYoEm7qNoVdqdcIxMrIPUiM0fkRE'
#
# client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
# # 字体转换到图片时可以尝试几种字体大小（行索引那里，然后测试网页转换的字体正确率怎么样
# with open('./tu.jpg', 'rb') as f:
#     r = client.basicGeneral(f.read())
# print(r)
# result_list = []
# for item in r['words_result']:
#     # print(item)  #{'words': '3756480291'}
#     result_list.extend(item['words'])
# print(result_list)
# #和字体文件中的字符创建映射
# dic = dict(zip(uni_ok_list, result_list))
# print(dic)
"""========================================================================================="""
#然后获取网页源代码，替换
url = 'http://bikongge.com/chapter_1/font_2/index.html'
resp = requests.get(url)
resp.encoding = 'utf-8'
page_source = resp.text  #网页源代码中的数字&#xeb18;  是小写
#字符替换
dic = {'\\uE7F1': '3', '\\uE0FA': '7', '\\uF531': '5', '\\uEBB4': '6', '\\uED05': '4', '\\uF150': '8', '\\uEB18': '0', '\\uE8A2': '2', '\\uE68A': '9', '\\uE75D': '1'}
for k in dic:  #k是key
    v = dic[k]
    kk = k.lower().replace('\\u', '&#x')+';'
    page_source = page_source.replace(kk, v)
print(page_source)
tree = etree.HTML(page_source)
dds = tree.xpath('/html/body/dl//dd')
print(len(dds))
for dd in dds:
    title = dd.xpath('./div/div/div[1]/p[1]/a/text()')[0]
    realtime = dd.xpath('./div/div/div[2]/p[1]//text()')
    total = dd.xpath('./div/div/div[2]/p[2]//text()')
    print(title, realtime, total)