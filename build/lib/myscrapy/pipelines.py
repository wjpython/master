# -*- coding: utf-8 -*-

# Define your item pipelines here
# 定义你的项目管道
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# 在settings里添加授权
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class MyscrapyPipeline(object):
    '''
    调用类方法from_settings(cls,settings)，返回该类的实例
    instan = MyscrapyPipeline.from_xxx(cls,settings)
    使用返回值（实例）调用process_item实例方法
    instan.process_item(item,spider)
    or

    @classmethod
    from_crawler(cls, crawler):
        return MyscrapyPipeline(value=crawler.settings.get("key"))

    打开spider时执行
    def open_spider(self, spider)
    关闭spider时执行
    def close_spider(self, spider)
    '''
    csvs = open('csv.csv','at',encoding='utf8',newline='')
    write = csv.writer(csvs)

    def __init__(self):
        pass

    #调用该类方法生成实例
    @classmethod
    def from_settings(cls,settings):
        return cls()


    def process_item(self, item, spider):
        '''
        gangwei = scrapy.Field()  # 岗位
        yaoqiu = scrapy.Field()  # 要求
        xinchou = scrapy.Field()  # 薪酬
        zhize = scrapy.Field()  # 职责
        diqu = scrapy.Field()  # 地区
        dizhi = scrapy.Field()  # 地址
        gongsi = scrapy.Field()  # 公司
        '''
        print("work!pip :process_item ","spider:",spider)
        l=['gangwei','yaoqiu','xinchou','zhize','diqu','dizhi','gongsi','url']
        lists=[item[i] for i in l]
        MyscrapyPipeline.write.writerow(lists)
        return item


