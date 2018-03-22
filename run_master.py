#coding:utf-8
import logging
from redis import Redis
from movieSpider.settings import REDIS_URL, REDIS_HOST, REDIS_PORT

logger = logging.getLogger(__name__)

class master(object):
    def __init__(self, host=None, port=None, url=None, database_name=0, start_urls):
        try:
            self.start_urls = start_urls
            if url:
                self.r = Redis(url)
            elif not url:
                self.r = Redis(host=host, port=port, password=passwd, db=database_name)
        except Exception as err:
            logger.msg(err)

    def process(self):
        p = self.r.pipeline()
        for i in [*start_urls]:
            for j in start_urls[i]:
                p.lpush(i, j)
        p.execute()
        return item

if __name__ == "__main__":
    start_urls = {
        'douban:start_urls':["https://movie.douban.com/{}".format(i) for i in ["", "chart", "top250"]],
        'imdb:start_urls':["https://www.imdb.com/chart/{}?".format(i) for i in ["boxoffice", "moviemeter", "top", "toptv", "top-english-movies", "top-reted-indian-movies", "bottom"]],
        'maoyan:start_urls':[r"https://maoyan.com/films"] + [r"https://maoyan.com/films?showType={}".format(i) for i in range(1,4)],
    }
    master(REDIS_HOST, REDIS_PORT, REDIS_URL, 0, start_urls).process()