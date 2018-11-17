#!/usr/bin/python3
# -*- coding:utf-8 -*-

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


process = CrawlerProcess(get_project_settings())
process.crawl('qiancheng')
# process.crawl('B_spider')
# process.crawl('C_spider')
process.start()





# # 创建爬虫程序
# process=CrawlerProcess()
# # 将爬虫加入到程序中
# process.crawl(QianchengSpider)
# # 启动程序
# process.start()




