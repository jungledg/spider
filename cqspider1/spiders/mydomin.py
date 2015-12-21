# -*- coding: utf-8 -*-
import scrapy


class MydominSpider(scrapy.Spider):
    name = "mydomin"
    allowed_domains = ["mydomain.com"]
    start_urls = (
        'http://www.mydomain.com/',
    )

    def parse(self, response):
        pass
