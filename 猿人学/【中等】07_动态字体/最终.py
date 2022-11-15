import re
import base64
import requests
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from fontTools.ttLib import ttFont
from aip import AipOcr

def get_woff(page):
    url = 'https://match.yuanrenxue.com/api/match/7?page=%d' % page
    headers = {
        'user-agent': 'yuanrenxue.project'
    }
    font_resp = requests.get(url, headers=headers).json()
    if font_resp.get('woff'):
        font = font_resp.get('woff')
        # base64.b64decode(font.encode()) 结果一样
        font = base64.b64decode(font)
        with open('font'+str(page)+'.woff', 'wb') as f:
            f.write(font)
    return font_resp

#获取正确字形
def get_font_img(page):
    file = 'font'+str(page)
    ttf = ttFont.TTFont(file+'.woff')
    uni_list = ttf.getGlyphOrder()
    uni_ok_list = [uni.replace('uni', '\\u') for uni in uni_list if uni != '.notdef']
    print(len(uni_ok_list))
    img = Image.new('RGB', (500,300), color=(255, 255, 255))
    img_draw = ImageDraw.Draw(img)
    img_font = ImageFont.truetype(file+'.woff', 40) #字体大小40像素
    #10个数字一行搞定
    line = [uni.encode().decode('unicode-escape') for uni in uni_ok_list]
    line_s = ''.join(line)
    img_draw.text((20, 45), line_s, fill=1, font=img_font)
    img.save(file+'.jpg')

    return uni_ok_list

def read_font_img(uni_ok_list, page):
    """ 你的 APPID AK SK """
    APP_ID = '28067874'
    API_KEY = 'l5BmOn6geHb2sw3BhS0nMylL'
    SECRET_KEY = 'hoXHVYoEm7qNoVdqdcIxMrIPUiM0fkRE'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    # 字体转换到图片时可以尝试几种字体大小（行索引那里，然后测试网页转换的字体正确率怎么样
    file = 'font' + str(page)
    with open(file+'.jpg', 'rb') as f:
        r = client.basicGeneral(f.read())
    result_list = []
    for item in r['words_result']:
        # print(item)  #{'words': '3756480291'}
        result_list.extend(item['words'])
    # print(result_list)
    # 和字体文件中的字符创建映射
    ok_list = [uni.replace('\\u', '&#x') for uni in uni_ok_list]
    font_result = dict(zip(ok_list, result_list))
    print(font_result)
    return font_result  #{'&#xe618;': '8', ...

def parse_data(font_result, font_resp, page):  #font_result是识别出来的字符和字形映射关系  font_resp是每一页对应的响应，包含动态字符信息
    html_url = 'https://match.yuanrenxue.com/match/7'
    headers = {
        'user-agent': 'yuanrenxue.project',
    }
    resp = requests.get(html_url, headers=headers).text
    # print(resp)
    names = re.findall(r"name=\[(.*?)\];", resp, re.S)
    names = names[0].replace("\'", '').split(',')
    #修改为对应数字
    data = font_resp.get('data')
    print(data)
    for d in data:
        for k in list(font_result.keys()):
            d['value'] = d['value'].replace(k, font_result[k])

    parse = []
    calculator_score = 0   #用来找出每一页最高的分数
    calculator_name = ""   #用来找出分数最高对应的姓名
    yyq = 1
    for i in range(len(data)):
        print(data[i].get('value'))
        score = int(data[i].get('value').replace(' ', ''))
        name = names[yyq + (page - 1) * 10]
        if score > calculator_score:
            calculator_score = score
            calculator_name = name
        parse.append({'name': name, 'value': score})
        yyq += 1

    return calculator_score, calculator_name, parse

def main():
    all_data = []
    max_score = 0
    max_name = ''
    for i in range(1, 6):
        font_resp = get_woff(i) #获取字体文件
        uni_ok_list = get_font_img(i)   #将字形画在图上 uni_ok_list 是 字形对应unicode编码
        font_result = read_font_img(uni_ok_list, i) #字体识别获取每个unicode编码对应数字
        # 获取每一页最高分和对应名字，以及每一页所有数据
        calculator_score, calculator_name, parse = parse_data(font_result, font_resp, i)  #处理数据
        all_data.append(parse)
        if calculator_score > max_score:
            max_score = calculator_score
            max_name = calculator_name
    print('max_score:', max_score, 'max_name:', max_name)
    print(all_data)

if __name__ == '__main__':
    main()









