# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join

class movieItem(Item):
    # define the fields for your item here like:
    name = Field()
    year = Field()
    score = Field()
    #people_vote = Field()
    #box_office = Field()
    #country = Field()
    #style = Field()
    #director = Field()
    #screenwriter = Field()
    #Actor = Field()

class movieLoader(ItemLoader):
    default_item_class = movieItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()