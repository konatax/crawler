import re
import requests
from lxml import etree
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# url = 'http://bikongge.com/chapter_1/font_3/index.html'
# resp = requests.get(url)
# resp.encoding = 'utf-8'
# tree = etree.HTML(resp.text)
# style = tree.xpath('//style/text()')[0]
# font_url = re.findall(r"src: url\('(.*?)'\)", style, re.S)[0]
# font_url = urljoin(url, font_url)
# # print(font_url)
# #下载字体文件
# font_resp = requests.get(font_url)
# with open('font.ttf', 'wb') as f:
#     f.write(font_resp.content)
"""========================================================================================"""
from fontTools.ttLib import ttFont
font = ttFont.TTFont('font.ttf')
# 转为xml文件：
# font.saveXML('file.xml')   #打开xml文件  cmap标签中 <map code="0x9476" name="glyph00006"/>
# code 格式0x  是十六进制
best_cmap = font.getBestCmap()  #获取请求到的字体code和name的对应关系
# key是编码的int型，后面要转成十六进制
# {38006: 'glyph00006', 38287: 'glyph00004', 39228: 'glyph00003', 39499: 'glyph00007', 40506: 'glyph00010', 40611: 'glyph00002', 40804: 'glyph00008', 40850: 'glyph00001', 40868: 'glyph00005', 40869: 'glyph00009'}
new_map = {}
for k in best_cmap:
    #这里是投机取巧，直接把'glyph00006'当成5，其实应该读取xml文件中，每个字符的坐标再画图，然后第三方文字识别
    value = int(re.findall('(\d+)', best_cmap[k])[0])-1
    print(value)
    # 因为0x开头的数字是十六进制，把k变成十六进制
    key = hex(k)
    new_map[key] = value
print(new_map)
# 如果字体文件不是动态的，可以直接在网页对比每个数字对应的是哪个编码
#{'0x9476': 5, '0x958f': 3, '0x993c': 2, '0x9a4b': 6, '0x9e3a': 9, '0x9ea3': 1, '0x9f64': 7, '0x9f92': 0, '0x9fa4': 4, '0x9fa5': 8}
#获取网页源代码
url = 'http://bikongge.com/chapter_1/font_3/index.html'
resp = requests.get(url)
resp.encoding = 'utf-8'
page_source = resp.text
# print(page_source)
for k in new_map:
    v = new_map[k]
    page_source = page_source.replace(k.replace('0x','&#x')+';', str(v))
# print(page_source)
# tree = etree.HTML(page_source)
# b = tree.xpath('//div[@class="card-body"]')
# print(len(b))
# for i in b:
#     title = i.xpath('./h5/text()')
#     p = i.xpath('./p[1]/text()')
#     num = i.xpath('./p[2]/text()')
#     company = i.xpath('./p[3]/text()')
#     print('title:',title, 'p:',p, 'num:', num, 'company:', company)
# print(tree.xpath('//p[@class="float-right"]/text()'))
# print(len(tree.xpath('//p[@class="float-right"]/text()')))
soup = bs(page_source, 'lxml')
# print(soup)
b = soup.find_all('div', class_="card-body")
print(b[0],len(b))