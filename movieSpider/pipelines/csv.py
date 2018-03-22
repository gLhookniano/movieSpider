#coding:utf-8

class writeTo(object):
    def __init__(self, settings):
        self.loc_csv=settings.get("LOC_WRITE_CSV")
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def open_spider(self, spider):
        self.fp = open(self.loc_csv, 'w')
        
    def close_spider(self, spider):
        self.fp.close()
        
    def process_item(self, item, spider):
        self.fp.write("{},{},{},{}\n".format(
            item["protocol"], 
            item["address"], 
            item["port"],
            )
        )
        return item
        
class hashWriteTo(object):
    def __init__(self, settings):
        self.loc_csv=settings.get("LOC_WRITE_CSV")
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def open_spider(self, spider):
        self.fp = open(self.loc_csv, 'w')
        
    def close_spider(self, spider):
        self.fp.close()
        
    def process_item(self, item, spider):
        ip = item["address"]
        port = item["port"]
        sum = hashlib.sha256()
        sum.update(ip + ":" + port)
        hash256 = sum.hexdigest()
        
        self.foj.write("{},{},{},{}\n".format(
            item["protocol"], 
            item["address"], 
            item["port"],
            hash256,
            )
        )
        return item