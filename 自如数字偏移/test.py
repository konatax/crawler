import re
# import ddddocr
import requests
from aip import AipOcr
from lxml import etree

def get_num(path):

    # 识别前面保存的图片里的文字
    # """ 你的 APPID AK SK """
    APP_ID = 'xxxx'
    API_KEY = 'xxxx'
    SECRET_KEY = 'xxxx'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    # 字体转换到图片时可以尝试几种字体大小（行索引那里，然后测试网页转换的字体正确率怎么样
    with open(path, 'rb') as f:
        r = client.basicGeneral(f.read())
    print(r)
    r_list = []
    for item in r['words_result']:
        try:
            # print(item)
            r_list.extend(item['words'])
            return r_list
        except Exception as e:  #如果r['words_result']报错应该是网络问题，重新识别
            get_num(path)
    # 百度ocr接口无法识别黄色数字
    # ocr = ddddocr.DdddOcr()
    #
    # res = requests.get('https://' + img_src, headers=headers)
    # # print(res.content)
    # # with open('./images/num_img1.png','wb') as f:
    # #     f.write(res.content)
    # res = ocr.classification(res.content)
    # print(res)
def main():

    url = 'https://www.ziroom.com/z/z1-p2/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    resp = requests.get(url, headers=headers)
    tree = etree.HTML(resp.text)
    items = tree.xpath('/html/body/section/div[3]/div[2]//div[@class="item"]')
    if not items:                                                                         #先判断是否抓到数据
        print('爬取失败')
        return
    # 拿到红字和黄字图片链接
    price_red = tree.xpath('.//div[@class="price red"]/span[2]/@style')
    price_yellow = tree.xpath('.//div[@class="price "]/span[2]/@style')
    price_red_url = 'https:' + re.findall(r'(//static8.*?png)', price_red[0])[0]
    price_yellow_url = 'https:' + re.findall(r'(//static8.*?png)', price_yellow[0])[0]
    red_content = requests.get(price_red_url, headers=headers).content
    yellow_content = requests.get(price_yellow_url, headers=headers).content
    with open('./red.jpg', 'wb') as f:
        f.write(red_content)
    with open('./yellow.jpg', 'wb') as f:
        f.write(yellow_content)

    #识别数据
    red_num = get_num('./red.jpg')
    yellow_num = get_num('./yellow.jpg')

    titles = []
    nums = []
    for item in items:
        price_style = item.xpath('./div[@class="info-box"]/div[2]/@class')
        # print(title, price_style)
        positions = item.xpath('./div[@class="info-box"]/div[2]//span[@class="num"]/@style')
        # print(positions)
        color = item.xpath('./div[@class="info-box"]/div[2]/@class')[0]
        if color == "price red":
            num = ''  # 每个数字坐标  px
            for positon in positions:
                p = re.findall('position: -(.*?)px', positon, re.S)
                num += red_num[int(p[0])//20]
            nums.append(num)
        else:
            nums.append('')
            # num = ''
            # for positon in positions:
            #     p = re.findall('position: -(.*?)px', positon, re.S)
            #     num += yellow_num[int(float(p[0])//21.4)]

        title = item.xpath('./div[@class="info-box"]/h5/a/text()')
        titles.append(title[0])
    for i, t in enumerate(zip(titles, nums)):
        print(t)


if __name__ == '__main__':
    main()