# -*- coding: utf-8 -*-

# Scrapy settings for movieSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'movieSpider'

SPIDER_MODULES = ['movieSpider.spiders']
NEWSPIDER_MODULE = 'movieSpider.spiders'

# Log settings
LOG_FILE=r"./log.log"
LOG_ENCODING="utf-8"
LOG_ENABLED=True

# Depth settings
DEPTH_LIMIT = 1
DEPTH_PRIORITY = 0
DEPTH_STATS = True
DEPTH_STATS_VERBOSE = True

#*************************custom settings start********************************

LOC_WRITE_JSON=r"./x.json"
LOC_WRITE_CSV=r"./x.csv"

MONGO_DB={
    "host":"192.168.63.133",
    "port":"27017",
    "username":"dev",
    "passwd":"dev",
    "database_name":"devdb",
    "collection_name":"test",
}
MYSQL_DB={
    "host":"192.168.63.131",
    "port":"3306",
    "username":"dev",
    "passwd":"dev",
    "database_name":"devdb",
    "table_name":"tb_ip",
}

#*************************custom settings end*********************************

#***************************redis config start******************************
# redis master数据库设置
#REDIS_HOST = '192.168.63.135'
#REDIS_PORT = 6379
REDIS_URL = 'redis://:123456@192.168.63.135:6379/0'
REDIS_ENCODING = 'utf-8'

# 调度器与过滤器设置
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 调度状态持久化
SCHEDULER_PERSIST = True

# 请求调度使用优先队列
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'


#***************************redis config end********************************


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'movieSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

CONCURRENT_ITEMS = 100

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 8
CONCURRENT_REQUESTS_PER_IP = 8

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   	'User-Agent' : 'Mozilla/5.0 (Windows; Windows NT 5.1; en-US; rv:1.7.8) Gecko/20050511 Firefox/1.0.4',
	'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'movieSpider.middlewares.ImdbspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#    'movieSpider.middlewares.ImdbspiderDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'movieSpider.pipelines.json.dumpTo': 300,
#    'movieSpider.pipelines.csv.writeTo': 302,
#    'movieSpider.pipelines.csv.hashWriteTo': 303,
#    'movieSpider.pipelines.mongo.writeTo': 304,
    'scrapy_redis.pipelines.RedisPipeline': 310,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
