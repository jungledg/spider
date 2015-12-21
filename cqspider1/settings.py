# -*- coding: utf-8 -*-

# Scrapy settings for cqspider1 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cqspider1'

SPIDER_MODULES = ['cqspider1.spiders']
NEWSPIDER_MODULE = 'cqspider1.spiders'

ITEM_PIPELINES = {
    'cqspider1.pipelines.Cqspider1Pipeline':300
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cqspider1 (+http://www.yourdomain.com)'
