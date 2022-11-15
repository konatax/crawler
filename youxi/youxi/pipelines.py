# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class YouxiPipeline:
    # xiaoyouxi.py返回一次数据，这里就执行一次
    # spider是xiaoyouxi.py中class XiaoyouxiSpider  可通过spider.name获取名字
    # 可传递多个不同spider
    def process_item(self, item, spider):
        # print(item)
        with open('./data.csv','a',encoding='utf-8') as f:
            f.write('%s, %s, %s\n' % (item['title'], item['src'], item['date']))
        #     把数据传递给下一个管道，可在settings文件中设置多个管道，通过优先级决定数据库存储的数据 （mysql,redis,mongodb等
        # 这里没有return的话，下一个管道拿到的数据是空的
        return item

#     举例，需要到settings中添加管道
class ZhouPipeline:
    def process_item(self, item, spider):
        # print(item)
        with open('./data.csv','a',encoding='utf-8') as f:
            f.write('%s, %s, %s\n' % (item['title'], item['src'], item['date']))
        #     把数据传递给下一个管道，可在settings文件中设置多个管道，通过优先级决定数据库存储的数据 （mysql,redis,mongodb等
        return item
