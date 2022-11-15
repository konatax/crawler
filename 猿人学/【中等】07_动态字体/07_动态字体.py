import re
import json
import base64
import requests
from lxml import etree
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from fontTools.ttLib import ttFont

# url = 'https://match.yuanrenxue.com/match/7'  #网页源代码 是个框架
# real_url = 'https://match.yuanrenxue.com/api/match/7?page=1'  #含有字体value和字体文件 是动态的
# headers = {
#     'user-agent': 'yuanrenxue.project',
#     'cookie': 'sessionid=nyyf36pwdp7j6mx1tccfd3q7lsd1li1a'
# }
# resp = requests.get(url)
# font_resp = requests.get(real_url, headers=headers).json()
font_resp = {'woff': 'AAEAAAAKAIAAAwAgT1MvMv8TZyMAAAEoAAAAYGNtYXCHxs4CAAABpAAAAYpnbHlmk0joKQAAA0gAAAP8aGVhZBq4KkIAAACsAAAANmhoZWEGzwE0AAAA5AAAACRobXR4ArwAAAAAAYgAAAAabG9jYQTZBb4AAAMwAAAAGG1heHABGABFAAABCAAAACBuYW1lUGhGMAAAB0QAAAJzcG9zdDniZlcAAAm4AAAAiAABAAAAAQAACFSOol8PPPUACQPoAAAAANnIUd8AAAAA33+UvgAU/+wCPwLUAAAACAACAAAAAAAAAAEAAAQk/qwAfgJYAAAALQIrAAEAAAAAAAAAAAAAAAAAAAACAAEAAAALADkAAwAAAAAAAgAAAAoACgAAAP8AAAAAAAAABAIqAZAABQAIAtED0wAAAMQC0QPTAAACoABEAWkAAAIABQMAAAAAAAAAAAAAEAAAAAAAAAAAAAAAUGZFZABAo4f2lQQk/qwAfgQkAVQAAAABAAAAAAAAAAAAAAAgAAAAZAAAAlgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAMAAAAcAAEAAAAAAIQAAwABAAAAHAAEAGgAAAAWABAAAwAGo4e0icEoyEHJN+Ix5hjzUfZB9pX//wAAo4e0icEoyEHJN+Ix5hjzUfZB9pX//1x/S4A+4jfHNs0d1hnpDLIJxAltAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwBhAHcAiQCmAOQBEwFEAYUBxwH+AAEAIP/sADwAEgACAAA3MxUgHBImAAADACv/8gI5AtQAHwAsADgAAAEiBwYVFBcWFzUGBwYVFBYyNzY1NCcmJxU2NzY1NCcmBzIXFhQHBiInJjQ3NhMyFxYUBwYiJjQ3NgEndys6FSUqLDgghPQ7Wz4dQTQoEjpEZkEwMygvmS4lKyxIVzMtLTmfViI0AtQ7E2tFJyEYAQY7Oj1hbFIaYT06OwYBGCEnRWsTO0wPK3gfHh4feCsP/sooLYAfGjmALSgAAQBrAAABbgLGAAkAAAEGBgcVNjcRMxEBJRxkOm1SRALGJjcbTBle/YcCxgABAD0AAAIfAsYABgAAExUhAzMBNT0BhukuARcCxjj9cgKARgACABQAAAI/AsYACgAOAAABARUhFTM1MzUjEQcjESEBef6bAWBdbm5VCP7lAsb+IUybmz4B7XD+gwAAAgBO//ICHALUABwAKAAAASIGFRQXFjM2NjczBxQHBiMiJyMWMzY3NjU0JyYHMhcWFAYjIiY1NDYBFVtoMSpcTFYgEhIkP1NmJzoLzmlNPyxTf0wvIlNKQ1t3AtSGZno9RAc5OR10WD1xvwF/UqrJT04pMkWjYGNUQYIAAAIAPP/yAhwC1AAMABkAAAEGBwYQFxYgNzYQJyYHMhcWEAcGIicmEDc2ASeMMi0tMgEeMjExMpJXMx8fM7wPMzMPAtQBaWj+vWFsbGEBQ2hpOGdM/v1JcnJJAQNMZwABADcAAAIfAtQAHQAAASIGFzM0NzYXMhYVFAcGBwYHBhUhNSE2NzY3NjQmATNpkxpEJz0wRVlGGT59CFMBzf6CEoqOAj5uAtR+jmxFMhBVPkg9HTc3Rz9yPVpHbBRH1FsAAAIAUv/yAh8C1AAbACgAAAEiBwYVFBcWFzY2NCYjIgcGBzMnNDc2NxYXMyYDNhcWFAcGByInJjQ2ATN8RCExLIFpg2t3MTElLhASKitYgQpkEOZTNR8pM0swSSh8AtRrY72balEBAY7IfA8nMxKYSEEcHIXJ/q8OMiyiMhoEG1Z+UwABADf/8gIfAtQAKwAAASIHBgczJjYzMhcWFAYjIxUzNhYUBwYjBicmNyMGFxYXMjY1NCcmJzY1NCYBKV9HNw9YA2U6OjIlTks3QUNbID1GTR8/EkMbTElia4MXF01+hgLUOzB3VFUiK3hCSwFJbjkWGjM2UoQ/LwF0akA6IRoPfFtpAAABAEv/8gI8AsYAJAAAEwMzNDc2MzYWFRQGIyInJicjFBcWMzI3NjU0JiMGBwYHMTchNWYbWjURPERmZUNKIzkDLlMXYmNKcaNiLiowGhcBYwLG/nswFAoFSmtDWC4hIlAlTjtmU2WMCw4IIt5UAAAAEgDeAAEAAAAAAAAAFwAAAAEAAAAAAAEADAAXAAEAAAAAAAIABwAjAAEAAAAAAAMAFAAqAAEAAAAAAAQAFAAqAAEAAAAAAAUACwA+AAEAAAAAAAYAFAAqAAEAAAAAAAoAKwBJAAEAAAAAAAsAEwB0AAMAAQQJAAAALgCHAAMAAQQJAAEAGAC1AAMAAQQJAAIADgDNAAMAAQQJAAMAKADbAAMAAQQJAAQAKADbAAMAAQQJAAUAFgEDAAMAAQQJAAYAKADbAAMAAQQJAAoAVgEZAAMAAQQJAAsAJgFvQ3JlYXRlZCBieSBmb250LWNhcnJpZXIuUGluZ0ZhbmcgU0NSZWd1bGFyLlBpbmdGYW5nLVNDLVJlZ3VsYXJWZXJzaW9uIDEuMEdlbmVyYXRlZCBieSBzdmcydHRmIGZyb20gRm9udGVsbG8gcHJvamVjdC5odHRwOi8vZm9udGVsbG8uY29tAEMAcgBlAGEAdABlAGQAIABiAHkAIABmAG8AbgB0AC0AYwBhAHIAcgBpAGUAcgAuAFAAaQBuAGcARgBhAG4AZwAgAFMAQwBSAGUAZwB1AGwAYQByAC4AUABpAG4AZwBGAGEAbgBnAC0AUwBDAC0AUgBlAGcAdQBsAGEAcgBWAGUAcgBzAGkAbwBuACAAMQAuADAARwBlAG4AZQByAGEAdABlAGQAIABiAHkAIABzAHYAZwAyAHQAdABmACAAZgByAG8AbQAgAEYAbwBuAHQAZQBsAGwAbwAgAHAAcgBvAGoAZQBjAHQALgBoAHQAdABwADoALwAvAGYAbwBuAHQAZQBsAGwAbwAuAGMAbwBtAAACAAAAAAAAAA4AAAAAAAAAAAAAAAAAAAAAAAAAAAALAAsAAAEJAQoBBQEDAQsBBgEEAQgBAgEHB3VuaWI0ODkHdW5pYzkzNwd1bmllMjMxB3VuaWYzNTEHdW5pYTM4Nwd1bmljMTI4B3VuaWM4NDEHdW5pZTYxOAd1bmlmNjk1B3VuaWY2NDE=', 'status': '1', 'state': 'success', 'data': [{'value': '&#xb489 &#xe231 &#xb489 &#xc841 '}, {'value': '&#xc128 &#xa387 &#xc937 &#xf695 '}, {'value': '&#xb489 &#xf641 &#xc128 &#xe618 '}, {'value': '&#xe618 &#xc128 &#xc128 &#xa387 '}, {'value': '&#xf351 &#xa387 &#xb489 &#xf351 '}, {'value': '&#xe618 &#xe618 &#xf641 &#xe618 '}, {'value': '&#xe231 &#xf695 &#xf641 &#xa387 '}, {'value': '&#xe618 &#xc937 &#xa387 &#xa387 '}, {'value': '&#xc937 &#xc128 &#xa387 &#xa387 '}, {'value': '&#xf351 &#xc937 &#xf351 &#xe618 '}]}
# # print(font_resp)
# font_s = font_resp['woff']
# font = base64.b64decode(font_s)
# # ss = base64.b64decode(font_s.encode())  结果和上面一样
# with open('font.woff', 'wb') as f:
#     f.write(font)
#读取woff文件
ttf = ttFont.TTFont('font.woff')
uni_list = ttf.getGlyphOrder()[1:]  #第一个'.notdef'没有用
# print(uni_list)
uni_ok_list = [uni.replace('uni', '\\u') for uni in uni_list]
# print(uni_ok_list)  ['\\ue618', '\\uf695', '\\uf351', '\\uc937', '\\uf641', '\\ua387', '\\ue231', '\\uc841', '\\ub489', '\\uc128']
#创建画布
# img = Image.new('RGB', (600,200), color=(255, 255, 255))
# #创建画笔
# img_draw = ImageDraw.Draw(img)
#创建字体
# img_font = ImageFont.truetype('font.woff', 40)  #字体大小40像素
# #只有10个数字，一行搞定
# line = []
# for i in range(len(uni_ok_list)):
#     uni = uni_ok_list[i]
#     line.append(uni.encode().decode('unicode-escape'))
# line_s = ''.join(line)
# # print(line_s)  줷ꎇ졁뒉섨
# img_draw.text((20, 45), line_s, fill=1, font=img_font)
# img.save('tu.jpg')
"""==============================================================="""
#第三方识别
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
#和字体文件中的字符创建映射
# dic = dict(zip(uni_ok_list, result_list))
# print(dic)
# {'value': '&#xb489 &#xe231 &#xb489 &#xc841 '} 3236
dic = {'\\ue618': '8', '\\uf695': '1', '\\uf351': '7', '\\uc937': '4', '\\uf641': '9', '\\ua387': '0', '\\ue231': '2', '\\uc841': '6', '\\ub489': '3', '\\uc128': '5'}
font_score = json.dumps(font_resp['data'])
for k in list(dic.keys()):
    v = dic[k]
    key = k.replace('\\u', '&#x')
    dic[key] = v
    font_score = font_score.replace(key, v)
print(font_score)
d = re.findall(r'(\{.*?\})', font_score, re.S)
dd = [json.loads(item)['value'].replace(' ','') for item in d]
print(dd)
names = ['极镀ギ紬荕','爷灬霸气傀儡','梦战苍穹','傲世哥','мaη肆風聲','一刀メ隔世','横刀メ绝杀','Q不死你R死你','魔帝殤邪','封刀不再战','倾城孤狼','戎马江湖','狂得像风','影之哀伤','謸氕づ独尊','傲视狂杀','追风之梦','枭雄在世','傲视之巅','黑夜刺客','占你心为王','爷来取你狗命','御风踏血','凫矢暮城','孤影メ残刀','野区霸王','噬血啸月','风逝无迹','帅的睡不着','血色杀戮者','冷视天下','帅出新高度','風狆瑬蒗','灵魂禁锢','ヤ地狱篮枫ゞ','溅血メ破天','剑尊メ杀戮','塞外う飛龍','哥‘K纯帅','逆風祈雨','恣意踏江山','望断、天涯路','地獄惡灵','疯狂メ孽杀','寂月灭影','骚年霸称帝王','狂杀メ无赦','死灵的哀伤','撩妹界扛把子','霸刀☆藐视天下','潇洒又能打','狂卩龙灬巅丷峰','羁旅天涯.','南宫沐风','风恋绝尘','剑下孤魂','一蓑烟雨','领域★倾战','威龙丶断魂神狙','辉煌战绩','屎来运赚','伱、Bu够档次','九音引魂箫','骨子里的傲气','霸海断长空','没枪也很狂','死魂★之灵']
page = 1
yyq = 1
calculator_score = 0   #胜点为0
name = ""
result = []
for i in range(len(dd)):
    append_data = {'name': names[yyq+(page-1)*10], 'value': int(dd[i])}
    if append_data['value'] > calculator_score:
        calculator_score = append_data['value']
        name = append_data['name']
    result.append(append_data)
    yyq += 1
print(result)
print(calculator_score)
print(name)