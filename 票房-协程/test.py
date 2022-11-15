import time
import asyncio
# http://t.zoukankan.com/callyblog-p-11216961.html
async def run(url):
    print("开始向'%s'要数据……"%(url))
    # 向百度要数据，网络IO
    await asyncio.sleep(5)
    data = "'%s'的数据"%(url)
    print("给你数据")
    return data

# 定义一个回调函数
def call_back(future):
    print("call_back:", future.result())

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
coroutine = run("百度")
# 创建一个任务对象
task = asyncio.ensure_future(coroutine, loop=loop)

# 给任务添加回调，在任务结束后调用回调函数
task.add_done_callback(call_back)
loop.run_until_complete(task)
print(task.result())
