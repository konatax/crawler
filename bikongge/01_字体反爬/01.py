import re
import requests
from lxml import etree
from urllib.parse import urljoin

# url = 'http://bikongge.com/chapter_1/font_1/index.html'
# # 本案例可以不加请求头
# resp = requests.get(url)
# resp.encoding = 'utf-8'
# # print(resp.text)
# # 获取style.css文件
# tree = etree.HTML(resp.text)
# href = tree.xpath('//link/@href')[0]
# href = urljoin(url, href)  #http://bikongge.com/chapter_1/font_1/css/style.css
# # 获取字体文件链接
# font_resp = requests.get(href)
# print(font_resp.text)
# font_url = re.findall(r'src: url\("(.*?)"\);', font_resp.text, re.S)[0]  #../font/ae0f8407.woff
# # 由于链接是在css文件中，所以要跟css文件的url拼接
# font_url = urljoin(href, font_url)  #http://bikongge.com/chapter_1/font_1/font/ae0f8407.woff
# # 下载字体文件
# font_resp = requests.get(font_url)
# with open('font.woff', 'wb') as f:
#     f.write(font_resp.content)
# # 字体文件可用font-creator打开查看

"""==========================================================="""
# 字体文件中  unicode编码"\ue0df"=》”店“ （直接打印是不认识的字）
# 要把文件中对应的字符画出来，然后通过AI识别
# # 获取字体文件中的unicode
from fontTools.ttLib import ttFont

ttf = ttFont.TTFont('font.woff') #打开字体文件
uni_list = ttf.getGlyphOrder()[2:]  #按顺序读取
# print(uni_list) #'glyph00000', 'x' 前两个字符是没有用的，去掉这两个就可以
#字体文件中 字符的格式 "uniebc6" 要修改成 "\uiebc6"
uni_ok_list = []
for uni in uni_list:
    uni = uni.replace('uni', '\\u')
    uni_ok_list.append(uni)
print("uni_ok_list",len(uni_ok_list))
print(uni_ok_list)  #['\\uebc6', '\\ue118', '\\ue315', '\\ue419', '\\uf275'....
"""======================================================================"""
# 按照字体文件中的字形，把上述unicode画出来
# from PIL import Image
# from PIL import ImageFont
# from PIL import ImageDraw
# # 创建图片                 宽    高  画布大小需要规划
# img = Image.new("RGB", (1800, 1000), color=(255,255,255))
# # 创建可以在该图上画画的画笔
# img_draw = ImageDraw.Draw(img)
# # 创建画图的字体
# img_font = ImageFont.truetype("font.woff", 40) #字体大小40像素
# # 准备文字
# # 一行40个字 根据识别效果不断调整
# # 索引号从1开始   索引 % 40 == 0 就换行
# # 行号          索引 // 40 + 1
# line_length = 43   #需要不断调整 先定下一行40字
# new_line = []      #用来一行字符
# for i in range(len(uni_ok_list)):
#     # 攒满一行了再画到画布上面
#     uni = uni_ok_list[i]
#     # 把\\uxxxx修改成unicode码 编码转换
#     uni = uni.encode().decode('unicode-escape')
#     if i % line_length == 0 and i != 0:
#         # 该换行了，写入该行
#         new_line_s = "".join(new_line)
#         # 画图      xy坐标 留一些页边距20像素 y坐标就是第n行*字体大小（可比字体大）只要所有字体在画布内就可以
#         img_draw.text((20, (i//line_length) * 50), new_line_s, fill=1, font=img_font)
#         new_line = [uni] #这个字符是留到下一行再画的
#     else:   #还没到换行的时候，先攒一行字
#         new_line.append(uni)
# # if new_line:   #判断最后一行有没有字符
# #     new_line_s = "".join(new_line)
# # #     可以画到画布上了
# if new_line: #最后一行
#     new_line_s = "".join(new_line)
#     # 这里的行号应该是math.ceil 向上取整 只要有余数，行索引就加1
#     img_draw.text((20, (len(uni_ok_list)//line_length+1)*50), new_line_s, fill=1, font=img_font)
# # 完成上述画布只是再内存中画了一张图，需要保存到磁盘上
# img.save("tu5.jpg")
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = 'xxxx'
API_KEY = 'xxxx'
SECRET_KEY = 'xxxxxxxxx'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
# 字体转换到图片时可以尝试几种字体大小（行索引那里，然后测试网页转换的字体正确率怎么样
with open('./tu4.jpg', 'rb') as f:
    r = client.basicGeneral(f.read())
# print(r)
# {'words_result': [{'words': '1234567890店中美家馆小车大市公酒行国品发电金心业商司超生装园场食有新限天面工'}, {'words': '服海华水房饰城乐汽香部利子老艺....
result_list = []
for item in r['words_result']:
    # 在列表末尾一次性追加另一个序列中的多个值
    result_list.extend(item['words'])
# print(result_list)  #['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '店', '中', '美', '家'...............
print('result_list',len(result_list))
#这里的长度必须和uni_ok_list长度一致
#把unicode对应的word进行映射  => 字典
dic = dict(zip(uni_ok_list, result_list))
# print(dic)
#{'\\uebc6': '1', '\\ue118': '2', '\\ue315': '3', '\\ue419': '4', '\\uf275': '5', ....

#替换
#获取页面源代码
import requests
url = 'http://bikongge.com/chapter_1/font_1/index.html'
# 本案例可以不加请求头
resp = requests.get(url)
resp.encoding = 'utf-8'
# print(resp.text)
page_source = resp.text  #&#xe9b1; 源代码中的字符是这种格式
for k in dic:
    #k:\\uxxxx,v是字
    v = dic[k]
    #把unicode换成源代码字符的格式，就能找到对应的字
    kk = k.replace("\\u", "&#x")+";"
    page_source = page_source.replace(kk, v)
print(page_source)
from lxml import etree
tree = etree.HTML(page_source)
divs = tree.xpath('//div[@class="wrapper-item"]')
print(len(divs))
for div in divs:
    tt = div.xpath('.//text()')
    # print(tt)
    print((''.join(tt)).replace('\r\n', '').replace('    ', ''))
    print('\n')
