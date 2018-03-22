#coding:utf-8
import json

class dumpTo(object):
    def __init__(self, settings):
        self.loc_write_json = settings.get("LOC_WRITE_JSON")
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def open_spider(self, spider):
        self.file = open(self.loc_write_json, 'w')

    def close_spider(self, spider):
        self.file.close()
        
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item