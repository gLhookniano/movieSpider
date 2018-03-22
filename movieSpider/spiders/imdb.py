# coding: utf-8
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from lxml import etree

from scrapy_redis.spiders import RedisCrawlSpider
from redis import Redis
from movieSpider.items import movieItem

class imdbSpider(RedisCrawlSpider):
    name = "imdb"
    #start_urls = ["https://www.imdb.com/chart/{}?".format(i) for i in ["boxoffice", "moviemeter", "top", "toptv", "top-english-movies", "top-reted-indian-movies", "bottom"]]
    redis_key = "imdb:start_urls"

    movie_lx = LinkExtractor(
        allow=(r"https://www.imdb.com/title/tt[0-9]*/"),
        deny=tuple(
            [r"https://www.imdb.com/{}/.*".format(j) for j in ["showtimes", "search", "gallery", "czone", "news"]]
            ),
        unique=True
    )
    rules = (
        Rule(movie_lx, callback='movie_parse', follow=True),
    )
    
    def movie_parse(self, response):
        item = movieItem()
        
        item["name"] = response.xpath('//h1[@itemprop="name"]/text()').extract_first()
        item["year"] = response.xpath('//span[@id="titleYear"]/text()').extract_first()
        item["score"] = response.xpath('//span[@itemprop="ratingValue"]/text()').extract_first()
        yield item