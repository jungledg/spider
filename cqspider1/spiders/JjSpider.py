# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import re
import scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from cqspider1.items import Cqspider1Item
from cqspider1.FilterForJJ import FilterForJJ


class JjSpider(scrapy.Spider):
    name = "cqjj"
    allowed_domains = ["www.jjqjyzx.com"]
    start_urls = (
        'http://www.jjqjyzx.com/www/site/site_index_130_1.shtml',
    )
    cqs_url_begin = 'http://www.jjqjyzx.com/www/site/site_index_130_'
    page = 1
    cqs_url_end = '.shtml'
    link_extractor = {
        'content' : SgmlLinkExtractor(allow=r'\/site\/web\_show\_\d+.shtml'),
    }
    def parse(self, response):
        content = response.xpath('//*[@id="content"]/a/text()').extract()
        if content:
            JjSpider.page += 1
            m_url = '%s%d%s' % (JjSpider.cqs_url_begin,JjSpider.page,JjSpider.cqs_url_end)
            yield Request(url=m_url,callback=self.parse)
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