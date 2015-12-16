# -*- coding: utf-8 -*-


import scrapy
import re
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import  Request

from cqspider1.Filter import *
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class cqspider1(CrawlSpider):
    name = 'cqspider1'
    allowed_domains = ['www.qjdtc.com']
    cqs_url = 'http://www.qjdtc.com/html/zfcg/zfcgzbgs/'
    start_urls = ['http://www.qjdtc.com/html/zfcg/zfcgzbgs/']
    page = 1


    link_extractor = {
        'content' : SgmlLinkExtractor(allow=r'\/html\/zfcg\/zfcgzbgs\/\d+\/\d+\/\d+.html$'),
    }
    def parse(self, response):
        for element in response.xpath('//td[@class="page"]/a').extract():
            element = element.encode('utf-8')
            pos = element.find('下一页')
            element = element.decode('utf-8')
            if pos > -1:

                cqspider1.page = cqspider1.page+1
                m_url = '%sList_%s.html' % (cqspider1.cqs_url,cqspider1.page)
                yield Request(url=m_url, callback=self.parse)
        #name = str(cqspider1.page-1) + '.txt'
        #f=open(name,'w')
        for link in self.link_extractor['content'].extract_links(response):
            #print >> f,link.url
            yield Request(url=link.url, callback=self.parse_page_content)
        #f.close()

        #print 'heheda'
        #i = Cqspider1Item()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #return i


    def parse_page_content(self, response):
        item = Cqspider1Item()
        content = response.xpath('/html/body/table[4]/text()').extract().pop()
        content = re.sub('<[^>]*>','',content)
        f = open('newurl.txt','a+')
        print >> f,content
        f.close()
        fil = Filter(content)

        item['project_name'] = fil.get_project_name()
        item['bid_name'] = fil.get_bid_name()
        item['bid_time'] = fil.get_bid_time()
        item['bid_money'] = fil.get_bid_money()
        return item


        #soup = BeautifulSoup(content)

    #     list = soup.find_all("span")
    #     count = 0
    #     for i in list:
    #         if count == 2:
    #             project_name = i.decode()
    #         if count == 11:
    #             year = i.decode()
    #         if count == 13:
    #             month = i.decode()
    #         if count == 15:
    #             day = i.decode()
    #         if count == 63:
    #             bid_name = i.decode()
    #         if count == 66:
    #             bid_money = i.decode()
    #         if count == 67:
    #             bid_money_type = i.decode()
    #         count += 1
    #
    #     print 'project_name='+self.get_useful_info(project_name)
    #     print 'bid_name='+self.get_useful_info(bid_name)
    #     print 'bid_money='+self.get_useful_info(bid_money)
    #     print 'bid_money_type_name='+self.get_useful_info(bid_money_type)
    #     print 'year='+self.get_useful_info(year)
    #     item['project_name'] = self.get_useful_info(project_name)
    #     item['bid_name'] = self.get_useful_info(bid_name)
    #     item['bid_money'] = self.get_useful_info(bid_money) + self.get_useful_info(bid_money_type)
    #
    #     time = self.get_useful_info(year) + '-'
    #     time = time + self.get_useful_info(month)
    #     time = time + '-'
    #     time = time + self.get_useful_info(day)
    #     item['bid_time']  = time
    #     return item
    # def get_useful_info(self,str):
    #
    #     lch = '>'
    #     rch = '<'
    #     list = str.split(lch)
    #     m_list = list[1].split(rch)
    #     print 'return='+m_list[0]
    #     return m_list[0]

