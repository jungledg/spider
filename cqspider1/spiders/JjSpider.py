# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import re
import scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from cqspider1.FilterForJJ import FilterForJJ
from cqspider1.items import Cqspider1Item


class JjSpider(scrapy.Spider):
    name = "cqjj"
    allowed_domains = ["www.jjqjyzx.com"]
    start_urls = (
        'http://www.jjqjyzx.com/www/site/site_index_130_1.shtml',
    )
    cqs_url_begin = 'http://www.jjqjyzx.com/www/site/site_index_130_'
    page = 1
    link_extractor = {
        'content' : SgmlLinkExtractor(allow=r'\/site\/web\_show\_\d+.shtml'),
    }
    def parse(self, response):
        #content = response.body
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
            m_url = 'http://www.jjqjyzx.com/www/site/site_index_130_%d.shtml' % (self.page)
            yield Request(url=m_url,callback=self.parse_content)

    def parse_content(self,response):
        # content = response.xpath('//*[@id="content"]/a/text()').extract()
        # if content:
        #     JjSpider.page += 1
        #     m_url = 'http://www.jjqjyzx.com/www/site/site_index_130_%d.shtml' % (JjSpider.page)
        #     yield Request(url=m_url,callback=self.parse)
        for link in self.link_extractor['content'].extract_links(response):
            yield Request(url=link.url, callback=self.parse_page_content)


    def parse_page_content(self, response):
        item = Cqspider1Item()
        content = response.xpath('//*[@id="textflag"]').extract().pop()
        content = re.sub('<[^>]*>','',content)
        fil = FilterForJJ(content)

        item['project_name'] = fil.get_project_name()
        item['bid_name'] = fil.get_bid_name()
        item['bid_time'] = fil.get_bid_time()
        item['bid_money'] = fil.get_bid_money()
        return item