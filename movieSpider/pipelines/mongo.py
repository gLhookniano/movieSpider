#coding:utf-8

import pymongo

class writeTo(object):
    def __init__(self, settings):
        self.mongo_uri = settings["MONGO_DB"]["host"]
        self.mongo_port = settings["MONGO_DB"]["port"]
        self.mongo_usr = settings["MONGO_DB"]["username"]
        self.mongo_pw = settings["MONGO_DB"]["passwd"]
        self.mongo_db = settings["MONGO_DB"]["database_name"]
        self.mongo_clc = settings["MONGO_DB"]["collection_name"]

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler.settings
        )

    def open_spider(self, spider):
        url = "mongodb://"+self.mongo_usr+':'+self.mongo_pw+'@'+self.mongo_uri+':'+self.mongo_port
        self.client = pymongo.MongoClient(url)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.mongo_clc].insert_one(dict(item))
        return item