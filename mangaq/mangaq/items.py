# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Manga(scrapy.Item):
    name = scrapy.Field()
    number = scrapy.Field()
    author = scrapy.Field()
    pages = scrapy.Field()
    img_page = scrapy.Field()
    host_name = scrapy.Field()
    
