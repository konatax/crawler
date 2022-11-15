import pymysql
import requests
from lxml import etree
import asyncio

# url = f'http://www.boxofficecn.com/boxoffice{year}'   year=1994~2022

def get_page_source(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    return resp.text

def parse_html(html):
    try:
        tree = etree.HTML(html)
        trs = tree.xpath('//table/tbody/tr')[1:]
        year = tree.xpath('/html/body/div[2]/div/div/div/article/header/h1/text()')[0][:4]
        result = []
        for tr in trs:
            # 有些年份是标红的无法取到，因此直接从标题获取年份
            # year = tr.xpath('./td[2]//text()')
            # year = year[0] if year else ""
            name = tr.xpath('./td[3]//text()')
            name = name[0] if name else ""
            money = tr.xpath('./td[4]//text()')
            money = money[0] if money else ""
            money = money.strip()
            d = (year, name, money)
            if any(d):   #any()  判断给定的可迭代参数 只要有一个为True,就返回True
                result.append(d)
        return result
    except Exception as e:
        print(e)

async def get_data(url):
    # 加上这一句就不会报错
    await asyncio.sleep(0)
    page_source = get_page_source(url)
    data = parse_html(page_source)
    return data

def call_back(future):

    return future.result()

def to_sql(data):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='mytestdb'
    )
    cursor = conn.cursor()
    # print(data)
    # 要确保创建表格时设置的字符长度足够，否则写不进去
    sql = """
        insert into movie4(年份, 电影名称, 票房收入) values (%s,%s,%s)
    """
    try:
        result = cursor.executemany(sql, data)
        conn.commit()
        print(result)
    except:
        conn.rollback()
    cursor.close()
    conn.close()

async def main():

    tasks = []  #包含多个任务对象的列表

    for year in range(1994, 2023):
        coroutine = get_data(f'http://www.boxofficecn.com/boxoffice{year}')
        # 开启消息循环
        task = asyncio.create_task(coroutine)
        # task = asyncio.ensure_future(coroutine,loop=loop)
        # task.add_done_callback(call_back)
        tasks.append(task)
        # 任务函数注册到消息循环上  tasks是列表 asyncio.wait(tasks)是对象
        # asyncio.wait将任务结果收集起来，返回两个值 done（已完成的协程），spending（未完成的协程）
    return await asyncio.wait(tasks)

    # for i in range(len(dd)):
    #     to_sql(dd[i])



if __name__ == '__main__':
    # python版本高 代码如下
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # 注册到异步执行对象中才会执行
    done, spending = loop.run_until_complete(main())
    for f in done:
        print(f.result())