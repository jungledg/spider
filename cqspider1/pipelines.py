# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import MySQLdb
from scrapy.exceptions import DropItem
from scrapy.http import Request

class Cqspider1Pipeline(object):
	pass
	# def __init__(self):
	# 	self.conn = MySQLdb.connect(user = 'nuaa',
	# 							passwd = 'ccst',
	# 							db = 'nuaa_se',
	# 							host = 'localhost',
	# 							charset="utf8",
	# 							use_unicode=True)
	# 	self.cursor = self.conn.cursor()
	#
	# def process_item(self,item,spider):
	# 	try:
	# 		self.cursor.execute("""INSERT IGNORE INTO bid_content(project_name,bid_name,bid_money,bid_time)
	# 						VALUES (%s,%s,%s)""",
	# 						(item['project_name'].encode('utf-8'),
	# 						item['bid_name'].encode('utf-8'),
	# 						item['bid_money'].encode('utf-8'),
	# 						item['bid_time'].encode('utf-8')))
	# 		self.conn.commit()
    #
	# 	except MySQLdb.Error,e:
	# 		print "Error %d: %s " %(e.args[0],e.args[1])
    #
	# 	return item
