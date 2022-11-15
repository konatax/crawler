import asyncio
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

import time
import execjs
import requests


async def get_data(ctx, funcName, page):
    await asyncio.sleep(0)
    url = 'http://spider.wangluozhe.com/challenge/api/4'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'cookie': 'session=b2546db6-5357-4116-bfcf-53a4df850b33.t5k1laa1kO3lULh4i_HyyjvzEtw'
    }
    sign = ctx.call(funcName, )
    # print(sign)
    data = {
        'page': page,
        'count': 10,
        '_signature': sign
    }
    resp = requests.post(url, data=data, headers=headers).json()
    # print(resp)
    data = resp.get('data')
    # print(type(data[0]))
    vals = []
    # print([d['value'] for d in data])
    vals.extend([d['value'] for d in data])
    # print('vals', vals)
    return vals


async def main():
    node = execjs.get()
    with open('./test.js', 'r', encoding='utf-8') as f:
        code = f.read()
    ctx = node.compile(code)
    funcName = 'getSign'
    tasks = []
    for i in range(1, 101):
        coroutine = get_data(ctx, funcName, i)
        # 开启消息循环
        task = asyncio.create_task(coroutine)
        tasks.append(task)
    return await asyncio.wait(tasks)


if __name__ == '__main__':
    start = time.time()
    # python版本高 代码如下
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # 注册到异步执行对象中才会执行
    done, spending = loop.run_until_complete(main())
    result = []
    for f in done:
        print(f.result())
        result.extend(f.result())

    print(result)
    print(sum(result))
    end = time.time()
    print('花费时间：', end-start, 's')