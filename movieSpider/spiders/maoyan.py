# coding: utf-8
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from lxml import etree

from scrapy_redis.spiders import RedisCrawlSpider
from redis import Redis
from movieSpider.items import movieItem

class maoyanSpider(RedisCrawlSpider):
    name = "maoyan"
    #start_urls = [r"https://maoyan.com/films"] + [r"https://maoyan.com/films?showType={}".format(i) for i in range(1,4)]
    redis_key = "maoyan:start_urls"

    movie_lx = LinkExtractor(
        allow=(r"https://maoyan.com/films/[0-9]*"),
        deny=tuple(
            [r"https://maoyan.com/{}/.*".format(j) for j in ["new", "cinemas", "time", "app", ]]
            ),
        unique=True
    )
    rules = (
        Rule(movie_lx, callback='movie_parse', follow=True),
    )
    
    
    def movie_parse(self, response):
        item = movieItem()
        
        item["name"] = response.xpath('//h3[@class="name"]/text()').extract_first()
        item["year"] = response.xpath('//div[@class="movie-brief-container"]/ul/li[position()=3]/text()').extract_first()
        item["score"] = response.xpath('//span[@class="stonefont"]/text()').extract_first()
        yield item