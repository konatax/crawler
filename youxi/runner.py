from scrapy.cmdline import execute

if __name__ == '__main__':
    # 要注意所在文件夹内不要有code.py文件，否则报错   所有py文件都不要叫做code.py
    execute("scrapy crawl xiaoyouxi".split())
