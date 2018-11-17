# -*- coding: utf-8 -*-
# Scrapy settings for myscrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

#========================scrapy_redis========================================
#队列设置PriorityQueue(默认优先级队列按照深度分级)FifoQueue(普通队列)LifoQueue(栈队列)
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
#替换调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#起始urlkey
REDIS_START_URLS_KEY = 'master:start_urls'
#设置去重类
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#redis连接"redis://user：password@address：port/db"
REDIS_URL = 'redis://auth:123456@176.122.16.139:6379/11'
#数据储存到redis库中
ITEM_PIPELINES = {
   'myscrapy.pipelines.MyscrapyPipeline': None,
   'scrapy_redis.pipelines.RedisPipeline': 300
}
#是否保存爬取指纹(去重)和请求队列
SCHEDULER_PERSIST = True
#是否启动时清楚指纹和请求队列
SCHEDULER_FLUSH_ON_START=False
#============================================================================

BOT_NAME = 'myscrapy'

SPIDER_MODULES = ['myscrapy.spiders']
NEWSPIDER_MODULE = 'myscrapy.spiders'

#日志调试等级
'''
CRITICAL - 严重错误
ERROR - 一般错误
WARNING - 警告信息
INFO - 一般信息
DEBUG - 调试信息
'''
LOG_LEVEL = 'DEBUG'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#设置请求浏览器（默认scrapy1.1 ）
USER_AGENT = 'Mozilla/5.0'

# Obey robots.txt rules
#是否遵守robots协议
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 多线程最大数量(默认为16)
CONCURRENT_REQUESTS = 20

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 设置同一网站请求的延迟时间单位：秒（默认为0）。一般为设置时间的0.5-1.5倍之间随机波动，不会固定时间。
DOWNLOAD_DELAY = 2


# The download delay setting will honor only one of:
# 下载延迟设置只有一个有效
# 并发请求单个域最大值为
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
# 并发请求单个IP最大值为
#CONCURRENT_REQUESTS_PER_IP = 16


# Disable cookies (enabled by default)
# 是否禁用cookies（默认使用）
COOKIES_ENABLED = False


# Disable Telnet Console (enabled by default)
# 是否禁用远程控制台（默认使用）
# TELNETCONSOLE_ENABLED = False


# Override the default request headers:
# 覆盖默认请求头部信息
# 默认请求头
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}


# Enable or disable spider middlewares
# 使用或禁用爬虫中间件
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# 爬虫中间件使用key中间件类：value越小越优先执行。None为禁用该中间件
# SPIDER_MIDDLEWARES = {
#    'myscrapy.middlewares.MyscrapySpiderMiddleware': 543,
# }



# Enable or disable downloader middlewares
# 使用或禁用下载中间件
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# 下载中间件使用key中间件类：value越小越优先执行。None为禁用该中间件
# DOWNLOADER_MIDDLEWARES = {
#    'myscrapy.middlewares.MyscrapyDownloaderMiddleware':None,
#    'myscrapy.middlewares.myrequest':None,
#    'scrapy.spidermiddlewares.offsite':None
# }


# Enable or disable extensions
# 启用或禁用扩展程序
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}


# Configure item pipelines
# 设置项目管道（处理数据）value越小越优先执行
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'myscrapy.pipelines.MyscrapyPipeline': 300,
# }


# Enable and configure the AutoThrottle extension (disabled by default)
# 启用并设置自动节流扩展（默认禁用）
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True

# 初始下载延迟
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5

# 高延迟下的最大延迟
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60

# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Enable showing throttling stats for every response received:
# 启用打印调节器受到开始每一个的响应数据
#AUTOTHROTTLE_DEBUG = False


# Enable and configure HTTP caching (disabled by default)
# 启用和设置HTTP缓冲（默认禁用）
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# 启用HTTP缓存
#HTTPCACHE_ENABLED = True

# 超过该时间的请求缓存将重新下载，为0时永远不过期
#HTTPCACHE_EXPIRATION_SECS = 0

# HTTP缓存文件夹
#HTTPCACHE_DIR = 'httpcache'

# 忽略GTTP代码缓存
#HTTPCACHE_IGNORE_HTTP_CODES = []

#实现缓存存储后端的类
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
