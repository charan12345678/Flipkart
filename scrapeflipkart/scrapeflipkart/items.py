# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapeflipkartItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
     product_name = scrapy.Field()
     price = scrapy.Field()
     rating = scrapy.Field()
     battery = scrapy.Field()
     ram = scrapy.Field()
     display = scrapy.Field()
     no_of_ratings = scrapy.Field()
     no_of_reviews = scrapy.Field()
     #processor = scrapy.Field()
     camera = scrapy.Field()     
