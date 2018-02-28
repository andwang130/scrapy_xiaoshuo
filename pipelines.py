# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from k17_CrawlSpiders.settings import MongoHost,Mongoport,Mongocllo,Mongodbs
import pymongo
class chapterpipeline(object):
    def __init__(self):
        client=pymongo.MongoClient(MongoHost,Mongoport)
        db=client[Mongodbs]
        self.Artcle_chap=db[Mongocllo]
    def process_item(self, item, spider):
        item = dict(item)
        if item.get('chapter'):
            self.Artcle_chap.insert(item)
        return item
class bookspipeline(object):
    def __init__(self):
        client= pymongo.MongoClient(MongoHost, Mongoport)
        db = client[Mongodbs]
        self.Artcle_books = db.Artcle_books
    def process_item(self,item,spider):
        if item.get('imgurl'):
            self.Artcle_books.insert(item)
        return item