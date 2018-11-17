# -*- coding: utf-8 -*-

# Define here the models for your scraped items
# 定义数据结构（类似字典）
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # 定义项目的列
    gangwei = scrapy.Field()#岗位
    yaoqiu = scrapy.Field()#要求
    xinchou = scrapy.Field()#薪酬
    zhize = scrapy.Field()#职责
    diqu = scrapy.Field()#地区
    dizhi = scrapy.Field()#地址
    gongsi = scrapy.Field()#公司
    url = scrapy.Field()#url