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
    page = 1
    link_extractor = {
        'content' : SgmlLinkExtractor(allow=r'\/html\/zfcg\/zfcgzbgs\/\d+\/\d+\/\d+\.html'),
    }
    def parse(self, response):
        page_num = 0
        content = response.xpath('//a').extract()
        for i in content:
            if u'尾页' in i or u'末页' in i:
                re_str = '.*\d+'
                re_url = re.compile(re_str)
                re_url = re_url.findall(i)
                re_url = re.findall(r'\d+(?=$)',re_url[0].decode())
                page_num = int(re_url[0])
                print 'page_num = ',page_num

        print 'page_num = ',page_num
        while self.page < page_num:
            self.page += 1
            print 'page = ',self.page
            m_url = "http://www.qjdtc.com/html/zfcg/zfcgzbgs/List_%d.html" % (self.page)
            yield Request(url=m_url,callback=self.parse_content)
        # content = response.xpath('//*[@class="sortlist"]/dl/dd/ul/li/a/text()').extract()
        # if content:
        #     self.page += 1
        #     m_url = "http://www.qjdtc.com/html/zfcg/zfcgzbgs/List_%d.html" % (self.page)
        #     yield Request(url=m_url, callback=self.parse)
        # for element in response.xpath('//*[@class="page"]/a').extract():
        #     element = element.encode('utf-8')
        #     pos = element.find('下一页')
        #     if pos > -1:
        #        QjspiderSpider.page = QjspiderSpider.page + 1
        #        m_url = "http://www.qjdtc.com/html/zfcg/zfcgzbgs/List_%d.html" % (QjspiderSpider.page)
        #        yield Request(url=m_url,callback=self.parse)
    def parse_content(self,response):
        for link in self.link_extractor['content'].extract_links(response):
             yield Request(url=link.url, callback=self.parse_page_content)

    def parse_page_content(self,response):
        item = Cqspider1Item()
        content = response.xpath('//*[@class="text"]').extract().pop()
        content = re.sub('<br>','\n',content)
        content = re.sub('<[^>]*>',' ',content)
        fil = FilterForQJ(content)
        item['project_name'] = fil.get_project_name()
        item['bid_name'] = fil.get_bid_name()
        item['bid_time'] = fil.get_bid_time()
        item['bid_money'] = fil.get_bid_money()
        return item

        # fil = FilterForQJ(content)
        #
        # item['project_name'] = fil.get_project_name()
        # item['bid_name'] = fil.get_bid_name()
        # item['bid_time'] = fil.get_bid_time()
        # item['bid_money'] = fil.get_bid_money()
        # return item
