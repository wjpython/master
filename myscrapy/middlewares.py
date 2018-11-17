# -*- coding: utf-8 -*-
# Define here the models for your spider middleware
# 定义这模块与你的爬虫中间件
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from proxy.proxy import *
import scrapy



# 爬虫中间件
class MyscrapySpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    # 不是全部的方法都需要定义，如果方法没有定义。爬虫中间件则不修改传输对象。
    '''
    引擎与爬虫的中间件，控制response进入爬虫前，和爬虫解析后，异常的处理
    '''

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        # scrapy使用该方法创建爬虫
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.
        # 调用通过蜘蛛中间件并进入蜘蛛的每个响应。
        # Should return None or raise an exception.
        # 应该返回None或者抛出异常
        '''
        设置进入爬虫前的操作
        '''


        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.
        # 在处理完响应后，调用Spider返回的结果。
        # Must return an iterable of Request, dict or Item objects.
        # 必须返回可迭代的请求，字典或者Item对象
        '''
        设置爬虫解析后在进入pip前的操作，result为item的list
        '''
        for i in result:
            yield i



    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.
        # 当spider或process_spider_input（）方法（来自其他蜘蛛中间件）引发异常时调用。
        # Should return either None or an iterable of Response, dict
        # or Item objects.
        # 应该返回None和可迭代请求，字典或者Item对象
        '''
        设置爬虫解析过程发生的异常，如果该函数不处理则由errback处理
        '''

        return None

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.
        # 使用蜘蛛的启动请求前调用，并且与process_spider_output（）方法的工作方式类似，不同之处在于它没有关联响应。
        # Must return only requests (not items).
        # 必须只能返回一个请求，而不是迭代对象
        '''
        设置开始请求前的操作，为最先操作的方法
        '''

        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



# 下载中间件
class MyscrapyDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    # 不是全部的方法都需要定义，如果方法没有定义。下载中间件则不修改传输对象。
    '''
    设置从引擎进去下载器时和从下载器进入引擎时的操作，和异常时的处理
    '''

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        # 这方法用于scrapy创建你的爬虫
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        # 调用通过下载器中间件的每个请求。
        # Must either:
        # 必须其中之一
        # - return None: continue processing this request
        # - 返回None：跳过单前请求
        # - or return a Response object
        # - 或者返回一个响应对象
        # - or return a Request object
        # - 或者返回一个请求对象
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # 或者抛出IgnoreRequest异常：将调用下载中间件里的process_exception()方法
        '''
        下载请求从引擎进入下载器前的操作
        '''

        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        # 使用下载程序返回的响应调用。
        # Must either;
        # 必须一下之一
        # - return a Response object
        # - 返回一个响应对象
        # - return a Request object
        # - 返回一个请求对象
        # - or raise IgnoreRequest
        # - 或者抛出IgnoreRequest
        '''
        下载完成数据进入引擎前的操作
        '''

        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.
        # 下载控制器或者process_request（其他下载中间件）抛出异常时调用。
        # Must either:
        # 必须为以下之一
        # - return None: continue processing this exception
        # - 返回None：跳过当前异常
        # - return a Response object: stops process_exception() chain
        # - 返回一个响应对象：停止process_exception()链
        # - return a Request object: stops process_exception() chain
        # - 返回一个请求对象：停止process_exception()链
        '''
        下载器或下载器中间件发生异常时的处理，如果无处理则由errback处理
        '''

        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

# #==============================================================================================
#
# class myrequest(object):
#     queues = queue.Queue()
#     for i in getlist():
#         queues.put(i)
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         # 这方法用于scrapy创建你的爬虫
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_request(self, request, spider):
#         '''
#         下载请求从引擎进入下载器前的操作
#         '''
#         request.meta["proxy"]=myrequest.queues.get()
#
#         return None
#
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)






