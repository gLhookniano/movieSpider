#coding:utf-8
import logging

import mysql.connector
from mysql.connector import errorcode

logger = logging.getLogger(__name__)

class writeTo(object):
#mysql/mariedb数据库写入
    def __init__(self, host, port, username, passwd, database_name, table_name):
        config_args = {
            'user':username,
            'password':passwd,
            'host':host,
            'database':database_name,
            'charset':'utf8',
            'use_unicode':True,
            'raise_on_warnings':True
        }
        
        try:
            self.cnx = mysql.connector.connect(**config_args)
            self.cursor = self.cnx.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings['MYSQL_DB']['host'],
            port=crawler.settings['MYSQL_DB']['port'],
            username=crawler.settings['MYSQL_DB']['username'],
            passwd=crawler.settings['MYSQL_DB']['passwd'],
            database_name=crawler.settings['MYSQL_DB']['database_name'],
            table_name=crawler.settings['MYSQL_DB']['table_name'],
        )
        
    def close_spider(self, spider):
        self.cursor.close()
        self.cnx.close()

    def process_item(self, item, spider):
        sql ="insert into devdb.tb_ip (protocol, address, port) values('{}', '{}', {}) on duplicate key update id=id"
        sql_value = (
            item["protocol"],
            item["address"],
            item["port"],
            )
        
        self.cursor.execute(sql.format(*sql_value))
        self.cnx.commit()
        return item
