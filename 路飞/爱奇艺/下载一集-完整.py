import re
import requests

url = 'https://cache.video.iqiyi.com/dash?tvid=302725300&bid=500&vid=0851504882b92df334914b356703014d&src=01010031010000000000&vt=0&rs=1&uid=&ori=pcw&ps=1&k_uid=9b8284417ba081b09f720d19d3bdf26b&pt=0&d=0&s=&lid=&cf=&ct=&authKey=46ded889ee4fe9550e5b4ce66d00ceba&k_tag=1&dfp=a016018eda2e924312a9d7df99dce308d6d0c24c33de26e9721fd5cfd034f8703f&locale=zh_cn&prio=%7B%22ff%22%3A%22f4v%22%2C%22code%22%3A2%7D&pck=&k_err_retries=0&up=&qd_v=2&tm=1661352503853&qdy=a&qds=0&k_ft1=706436220846084&k_ft4=1161084347621380&k_ft5=262145&bop=%7B%22version%22%3A%2210.0%22%2C%22dfp%22%3A%22a016018eda2e924312a9d7df99dce308d6d0c24c33de26e9721fd5cfd034f8703f%22%7D&ut=0&vf=8b3d39c30e67f1d2b1d5f34e28701088'
data = requests.get(url).json()
print(data,'\n',type(data))
urls = data['data']['program']['video'][3]['m3u8']
print(urls,'\n',len(urls),type(urls))
ts_url = re.findall('(http:.*?=0)',urls)
print(ts_url,'\n',len(ts_url))
for u in url:
    ts_data = requests.get(u).content
    with open('柯南01.mp4','ab') as f:
        f.write(ts_data)