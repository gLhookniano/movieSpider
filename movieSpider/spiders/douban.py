# coding: utf-8
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from lxml import etree

from scrapy_redis.spiders import RedisCrawlSpider
from redis import Redis
from movieSpider.items import movieItem

class doubanSpider(RedisCrawlSpider):
    name = "douban"
    #start_urls = ["https://movie.douban.com/{}".format(i) for i in ["", "chart", "top250"]]
    redis_key = "douban:start_urls"

    movie_lx = LinkExtractor(
        allow=(r"https://movie.douban.com/subject/[0-9]*/",r"https://movie.douban.com/subject/[0-9]*/?from=[a-z-]*"),
        deny=tuple(
            [r"https://https://movie.douban.com/subject/[0-9]*/{}/.*".format(i) for i in ["discussion", "questions"]] + [r"https://{}.douban.com/.*".format(j) for j in ["book", "read", "time", "market", ]]
            ),
        unique=True
    )
    rules = (
        Rule(movie_lx, callback='movie_parse', follow=True),
    )
    
    def movie_parse(self, response):
        item = movieItem()
        
        item["name"] = response.xpath("//span[@property='v:itemreviewed']/text()").extract_first()
        item["year"] = response.xpath("//span[@class='year']/text()").extract_first()
        item["score"] = response.xpath("//div[@class='rating_self clearfix']/strong/text()").extract_first()
        yield item