# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class chapters(scrapy.Item):
    chapter=scrapy.Field()
    conten=scrapy.Field()
    bookid=scrapy.Field()
    newstime=scrapy.Field()
class books(scrapy.Item):
    bookname=scrapy.Field()
    imgurl=scrapy.Field()
    bookid=scrapy.Field()
    bookype=scrapy.Field()


