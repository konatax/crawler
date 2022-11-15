import pymysql
import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor, as_completed

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

def get_data(url):
    page_source = get_page_source(url)
    data = parse_html(page_source)
    return data

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

def main():
    lst = [str(i) for i in range(1994, 2023)]
    dd = []
    # 线程池并发数为5
    pool = ThreadPoolExecutor(5)
    all_task = [pool.submit(get_data, f'http://www.boxofficecn.com/boxoffice{year}') for year in lst]
#     统一放入线程池使用
#     先完成的任务会先返回给主线程
    for future in as_completed(all_task):
        data = future.result()
        dd.append(data)

    for i in range(len(dd)):
        to_sql(dd[i])



if __name__ == '__main__':
    main()