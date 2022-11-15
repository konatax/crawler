import time
import execjs
import asyncio
import requests

def get_signature(url):
    node = execjs.get()
    with open('./code.js', 'r', encoding='utf-8') as f:
        code = f.read()
    xcj = node.compile(code)
    funcName = 'getSignature'
    _signature = xcj.call(funcName, url)
    print(_signature)
    return _signature

async def get_data(i):
    await asyncio.sleep(0)
    url = 'https://www.toutiao.com/api/pc/list/feed?channel_id=3189398972&refresh_count=1&category=pc_profile_channel&client_extra_params=%7B%22short_video_item%22:%22filter%22%7D&aid=24&app_name=toutiao_web'
    url = url + '&max_behot_time=' + str(i)
    _signature = get_signature(url)
    params = {
        '_signature': _signature
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    # session = requests.Session()
    # first_url = 'https://www.toutiao.com/api/pc/list/feed?channel_id=3189398999&min_behot_time=0&refresh_count=1&category=pc_profile_channel&client_extra_params=%7B%22short_video_item%22:%22filter%22%7D&aid=24&app_name=toutiao_web&_signature=_02B4Z6wo00901iasf-gAAIDCpq6FqiKRkWomiHtAAOr8vCoyT1l5wB9M3zO1-irFtLjgKgg-cdaexQUbCbGIpIiatoLjg5jWAIw-7w8DkqQbFlJbUkfU6sHsi03ZszYpmUcKk7XIUMBjszqe47'
    # session.get(first_url, headers=headers)
    resp = requests.get(url, params=params, headers=headers).json()
    print(len(resp["data"]))
    return len(resp["data"])

def get_first_data():
    url = 'https://www.toutiao.com/api/pc/list/feed?channel_id=3189398999&min_behot_time=0&refresh_count=1&category=pc_profile_channel&client_extra_params=%7B%22short_video_item%22:%22filter%22%7D&aid=24&app_name=toutiao_web'
    _signature = get_signature(url)
    params = {
        '_signature': _signature
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    # 设置超时为5秒，超过5秒没有响应就抛出异常
    resp = requests.get(url, params=params, headers=headers, timeout=5).json()
    print(len(resp["data"]))
    return len(resp["data"])

async def main():
    tasks = []
    t = []
    get_first_data()
    max_behot_time = int(time.time())
    for i in range(10):
        t.append(max_behot_time-5000)
    for i in range(10):
        coroutine = get_data(t[i])
        task = asyncio.create_task(coroutine)
        tasks.append(task)

    return await asyncio.wait(tasks)

if __name__ == '__main__':
    # python版本高 代码如下
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # 注册到异步执行对象中才会执行
    done, spending = loop.run_until_complete(main())
    for f in done:
        print(f.result())
