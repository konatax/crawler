import scrapy

class XiaoyouxiSpider(scrapy.Spider):
    name = 'xiaoyouxi'
    allowed_domains = ['4399.com']  #当前爬虫允许访问的域名 防止爬到无关的页面（比如广告之类的
    start_urls = ['http://www.4399.com/flash/']

    # 默认的解析数据的位置，主要负责第一个url的解析工作
    def parse(self, response):
        # print(response.text)
        # 这里用的是scrapy自己封装的xpath，不用lxml的xpath
        li_list = response.xpath('//ul[@class="n-game cf"]/li')
        # print(li_list)
        for li in li_list:
            # 不是列表而是selector list
            title = li.xpath('./a/b/text()').extract_first()
            # extrace_first()提取一个      #extract() 提取全部
            src = 'http://www.4399.com' + li.xpath('./a/@href').extract_first()
            # 用scrapy自带的xpath可以不用判断是否空值，如果为空，结果为None，不会报错
            date = li.xpath('./em[2]/text()').extract_first()

            # 可以返回数据且不打断函数执行  （生成器，占用极小的内存空间） 比return好
            # spider must return request, item, or None,不能返回元组
            # 字典可以充当item
            # yield (title, src, date)
            # 数据会经过引擎传递给管道 需要先在settings里开启管道
            # 引擎不停地运行.next() 因此能不断取数据
            yield {
                "title": title,
                "src": src,
                "date": date
            }