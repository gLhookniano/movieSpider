#!python3
#coding:utf-8
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from movieSpider.spiders.douban import doubanSpider
from movieSpider.spiders.imdb import imdbSpider
from movieSpider.spiders.maoyan import maoyanSpider

if __name__ == '__main__':
    runner = CrawlerProcess(get_project_settings())
    runner.crawl(doubanSpider)
    runner.crawl(imdbSpider)
    runner.crawl(maoyanSpider)
    runner.start()
    