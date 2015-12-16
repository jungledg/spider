# -*- coding: utf-8 -*-
import re
from items import Cqspider1Item
class NewFilter:
    def __init__(self,re_project_name,re_bid_name,re_bid_time,re_bid_money):
        self.re_project_name = re_project_name
        self.re_bid_name = re_bid_name
        self.re_bid_time = re_bid_time
        self.re_bid_money = re_bid_money
    def get_item(self,content):
        item = Cqspider1Item()
        rpe = self.re_project_name
        rbn = self.re_bid_name
        rbm = self.re_bid_money
        rbt = self.re_bid_time
        # find rpe
        rpe = re.compile(rpe)
        rpe = rpe.findall(content)
        if rpe:
            l = rpe[0]
            l = l.decode()
            l = l.replace('\r','')
            l = l.replace('\n','')
            item['project_name'] = l
        #find rbn
        rbn = re.compile(rbn)
        rbn = rbn.findall(content)
        if rbn:
            l = rpe[0]
            l = l.decode()
            l = l.replace('\r','')
            l = l.replace('\n','')
            item['bid_name'] = l
        #find rbm
        rbm = re.compile(rbm)
        rbm = rbm.findall(content)
        if rbm:
            l = rbm[0]
            l = l.decode()
            l = l.replace('\r','')
            l = l.replace('\n','')
            item['bid_money'] = l
        #find rbt
        rbt = re.compile(rbt)
        rbt = rbt.findall(content)
        if rbt:
            l = rbt[0]
            l = l.decode()
            l = l.replace('\r','')
            l = l.replace('\n','')
            item['bid_time'] = l
        return item