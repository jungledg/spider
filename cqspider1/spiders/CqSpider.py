#coding=utf-8
import scrapy
import re
from cqspider1.items import Cqspider1Item
from scrapy.http import FormRequest,Request
from cqspider1.FilterForCQS import FilterForCQS

class CqzbSpider(scrapy.Spider):
    name = "cqzh"
    allowed_domains = ["www.cqzb.com"]
    start_urls = [
    "http://www.cqzb.com/ciiccms/content/list-zfcg.action?categoryId=8af652c33947c9ae013947d9cd24000c"
    ]
    
    headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
    "Connection": "keep-alive",
    "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
    }    
    
    def parse(self,response):
        num = response.xpath('//*[@id="search_form"]/div[3]/text()[1]').extract()
        pat = '共'.decode("utf8")
        pat = pat+'(\d+)'
        pagenum = re.search(pat,num[0],re.M|re.I|re.U)
        pagenum = pagenum.group(1).encode('utf8')
        pagenum = int(pagenum) + 1
        x = 1
        while x <= pagenum :
            yield FormRequest( self.start_urls[0],
                            formdata = {
                            'content.contentTitle':'',
                            'content.projectNo':'',
                            'page.pageSize':'10',
                            'page.pageNo': str(x)
                            },
                            callback = self.get_link
                            )
            x += 1

    def get_link(self,response):
        linklist = response.xpath('//td/a/@href').extract()
        for    link in linklist :
            yield Request(url = link, callback = self.parse_page_content)

    def parse_page_content(self,response):
        item = Cqspider1Item()
        page_content = response.xpath('//*[@id="bulletinContent"]/tbody').extract().pop()
        page_content = re.sub('<[^>]+>',' ',page_content)
        fil = FilterForCQS(page_content)
        item['project_name'] = fil.get_project_name()
        item['bid_name'] = fil.get_bid_name()
        item['bid_time'] = fil.get_bid_time()
        item['bid_money'] = fil.get_bid_money()
        return item
