import re
import requests
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from fontTools.ttLib import ttFont
from bs4 import BeautifulSoup as bs
font = ttFont.TTFont('font.ttf')
# print(font.getReverseGlyphMap())
# print(font.getGlyphNames())
# print(font.getGlyphOrder())
bestcmap = font.getBestCmap()
#{38006: 'glyph00006', 38287: 'glyph00004', 39228: 'glyph00003', 39499: 'glyph00007', 40506: 'glyph00010', 40611: 'glyph00002', 40804: 'glyph00008', 40850: 'glyph00001', 40868: 'glyph00005', 40869: 'glyph00009'}
#key转换成十六进制，然后0x换成\\u， 最后.encode().decode('escape-unicode'),就能在画布上用设置好的字体画出对应的字符
print(bestcmap)
kk = []
for k in bestcmap:
    key = hex(k)
    print(key)
    kk.append(str(key).replace('0x','\\u').encode().decode('unicode-escape'))
print(kk)  #['鑶', '閏', '餼', '驋', '鸺', '麣', '齤', '龒', '龤', '龥']
ok_list = ['\\u'+str(hex(i))[2:] for i in bestcmap.keys()]
#创建画布
# img = Image.new('RGB', (800,800), color=(255,255,255))
# #创建画笔
# img_draw = ImageDraw.Draw(img)
# # 创建字体
# img_font = ImageFont.truetype('./font.ttf', 60)  #字体大小40
# # 只有10个数字，一行画完
# line_s = ''.join(kk)
# print(line_s)
# img_draw.text((20, 45), line_s, fill=1, font=img_font)
# img.save('tu11.jpg')
"""============================================================"""
#识别上面保存的图片里的文字
from aip import AipOcr
""" 你的 APPID AK SK """
APP_ID = '28067874'
API_KEY = 'l5BmOn6geHb2sw3BhS0nMylL'
SECRET_KEY = 'hoXHVYoEm7qNoVdqdcIxMrIPUiM0fkRE'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
# 字体转换到图片时可以尝试几种字体大小（行索引那里，然后测试网页转换的字体正确率怎么样
with open('./tu11.jpg', 'rb') as f:
    r = client.basicGeneral(f.read())
print(r)
result_list = []
for item in r['words_result']:
    # print(item)  #{'words': '3756480291'}
    result_list.extend(item['words'])
print(result_list)
#和字体文件中的字符创建映射
dic = dict(zip(ok_list, result_list))
print(dic)
"""============================================================================="""
#获取网页源代码替换
url = 'http://bikongge.com/chapter_1/font_3/index.html'
resp = requests.get(url)
resp.encoding = 'utf-8'
page_source = resp.text
#替换字符  k是key
for k in dic:
    v = dic[k]
    kk = k.replace('\\u', '&#x')+';'
    page_source = page_source.replace(kk, v)
print(page_source)