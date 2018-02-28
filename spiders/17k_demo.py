# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from k17_CrawlSpiders.items import *
class TencentSpider(CrawlSpider):
    name = '17k_demo'
    # allowed_domains = ['http://www.17k.com/']
    start_urls=['http://www.17k.com/','http://top.17k.com/','http://all.17k.com/lib/book.html']
    conten=LinkExtractor(allow=(r'\d+/\d+.html'))
    Book=LinkExtractor(allow=(r'book/\d+.html'))
    booklist=LinkExtractor(allow=(r'list/\d+.html'))
    rules = (
        Rule(conten ,callback='parse_item', follow=True),
        Rule(Book,callback='parse_Boke',follow=True),
        Rule(booklist,callback='parse_booklist',follow=True)
    )
    data={
        'userName':'13524873489',
        'password':'WANGJING130',
        'verificationCode':'',
        'isCode':'0',
        'isAutoLogin':'true',
        'postCallback':'parent.Q.post_artwc_callback'
    }
    def start_requests(self):
        url = 'http://passport.17k.com/login.action?jsonp=true'
        return [scrapy.FormRequest(url=url,formdata=self.data, callback=self.login_response)]
    def login_response(self,response):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)
    def parse_item(self,response):
        try:
            itme=chapters()
            itme['chapter'] = response.xpath('//h1/text()').extract()[0]
            itme['bookid']=response.xpath('//div[@class="infoPath"]/span/text()|//div[@class="infoPath"]/div[2]/span/text()').extract()[0]
            itme['newstime']=response.xpath('//div[@title="更新日期"]/text()').extract()[0]
            itme['conten']=response.xpath('//div[@class="p"]').extract()[0]
            yield itme
        except:
            pass
    def parse_Boke(self,response):
        itme=books()
        itme['imgurl']=response.xpath('//img[@class="book"]/@src').extract()[0]
        itme['bookname']= response.xpath('//a[re:test(@href,"/book/\d+.html")]/text()').extract()[0]  # 使用了正则的xpath
        itme['bookid']= response.xpath('//div[@class="infoPath"]/div/span/text()').extract()[0]
        itme['bookype']=response.xpath('//a[re:test(@href,"http://all.17k.com/lib/book/.*?.html")]/text()').extract()[0]
        yield itme

    def parse_booklist(self,response):
        # print(response.text)
        pass
