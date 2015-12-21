# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.http import Request
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from cqspider1.FilterForQJ import FilterForQJ
from cqspider1.items import Cqspider1Item


class QjspiderSpider(scrapy.Spider):
    name = "QjSpider"
    allowed_domains = ["www.qjdtc.com"]
    start_urls = (
        'http://www.qjdtc.com/html/zfcg/zfcgzbgs/',
    )
    url = "http://www.qjdtc.com/html/zfcg/zfcgzbgs/"
    page = 1
    flag = 0
    link_extractor = {
        'content' : SgmlLinkExtractor(allow=r'\/html\/zfcg\/zfcgzbgs\/\d+\/\d+\/\d+\.html'),
    }
    def parse(self, response):
        for element in response.xpath('//*[@class="page"]/a').extract():
            element = element.encode('utf-8')
            pos = element.find('下一页')
            if pos > -1:
               QjspiderSpider.page = QjspiderSpider.page + 1
               m_url = "%sList_%d.html" % (QjspiderSpider.url,QjspiderSpider.page)
               yield Request(url=m_url,callback=self.parse)
        for link in self.link_extractor['content'].extract_links(response):
            yield Request(url=link.url, callback=self.parse_page_content)

    def parse_page_content(self,response):
        item = Cqspider1Item()
        content = response.xpath('//*[@class="text"]').extract().pop()
        content = re.sub('<br>','\n',content)
        f = open('qj6.txt','a+')
        f1 = open ('qj_data.txt','a+')
        content = re.sub('<[^>]*>','',content)
        print >> f,content
        f.close()
        fil = FilterForQJ(content)
        item['project_name'] = fil.get_project_name()
        item['bid_name'] = fil.get_bid_name()
        item['bid_time'] = fil.get_bid_time()
        item['bid_money'] = fil.get_bid_money()
        if item['bid_name']:
            print >> f1,item
        f1.close()
        return item

        # fil = FilterForQJ(content)
        #
        # item['project_name'] = fil.get_project_name()
        # item['bid_name'] = fil.get_bid_name()
        # item['bid_time'] = fil.get_bid_time()
        # item['bid_money'] = fil.get_bid_money()
        # return item
