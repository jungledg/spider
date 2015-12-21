# -*- coding: utf-8 -*-
import re
from items import Cqspider1Item
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
class FilterForJJ:
    '''use filter'''

    def __init__(self,str=''):
        self.str = str
        self.re_project_name = u'\u9879\u76ee\u540d\u79f0\uff1a'
        self.re_bid_name = u'\u4e2d\u6807\u5355\u4f4d\uff1a'
        self.re_bid_money = u'\u4e2d\u6807\u91d1\u989d\uff1a'
        self.re_bid_time = u'\u8bc4\u5ba1\u65e5\u671f\uff1a'
        self.find_re_bid_name = u''

    def get_item(self):
        str = self.str
        item = Cqspider1Item()
        re_project_name = u"(\u9879\u76ee\u540d\u79f0\s+[\u4e00-\u9fff]*\s)"
        re_project_name = re.compile(re_project_name)
        m_project_name = re_project_name.findall(str)
        if m_project_name:
            #for l in m_project_name:
            l = m_project_name
            l = l.decode()
            l = l.encode()
            l.replace('\r','')
            list = l.split('\n')
            count = 1
            if list[count]:
                item['project_name'] = list[count]
                item['bid_name'] = self.get_item_bid_name(list[count])
                item['bid_money'] = self.get_item_bid_money(list[count])
                item['bid_time'] = self.get_item_bid_time(list[count])
                return item
        #return item_list


    def get_item_bid_name(self,project_name):
        str = self.str
        find_re_bid = u"(?<="+project_name+self.re_project_name
        find_re_bid = re.compile(find_re_bid)
        m_find_bid_name = find_re_bid.findall(str)
        if m_find_bid_name:
            l = m_find_bid_name[0]
            re_bid_name = u"\u4e2d\u6807\u5355\u4f4d\uff1a[\u4e00-\u9fff]*"
            re_bid_name = re.compile(re_bid_name)
            m_bid_name = re_bid_name.findall(l)
            if m_bid_name:
                l = m_bid_name[0]
                l = l.decode()
                l = l.encode()
                list = l.split('\\：')
                if list[1]:
                    return list[1]


    def get_item_bid_time(self,project_name):
        str = self.str
        project_name += ')'
        find_re_bid = u"(?<="+project_name+self.re_project_name
        find_re_bid = re.compile(find_re_bid)
        m_find_bid_time = find_re_bid.findall(str)
        if m_find_bid_time:
            l = m_find_bid_time[0]
            re_bid_time = u"(\u8bc4\u5ba1\u65e5\u671f\uff1a.*\\n*\d+[\u4e00-\u9fff]\d+[\u4e00-\u9fff]\d+[\u4e00-\u9fff])"
            re_bid_time = re.compile(re_bid_time)
            m_bid_time = re_bid_time.findall(l)
            if m_bid_time:
                l = m_bid_time[0]
                l = l.decode()
                l = l.encode()
                l.replace('\r','')
                list = l.split('\n')
                if list[1]:
                    return list[1]
    def get_item_bid_money(self,project_name):
        str = self.str
        find_re_bid = u"(?<="+project_name+self.re_project_name
        find_re_bid = re.compile(find_re_bid)
        m_find_bid_money = find_re_bid.findall(str)
        if m_find_bid_money:
            l = m_find_bid_money[0]
            re_bid_money = u"(\u4e2d\u6807\u91d1\u989d\uff1a((\d{1,10})|((\d{1,3}\,{0,1})*\.\d\d))[\u4e00-\u9fff]{1,2})"
            re_bid_money = re.compile(re_bid_money)
            m_bid_money = re_bid_money.findall(l)
            if m_bid_money:
                l = m_bid_money[0][0]
                l = l.decode()
                l = l.encode()
                list = l.split('\\：')
                if list[1]:
                    return list[1]


    def get_project_name(self):
        str = self.str
        re_project_name = u"(?<=\u9879\u76ee\u540d\u79f0\uff1a).*(?=\\n)"
        re_project_name = re.compile(re_project_name)
        m_project_name = re_project_name.findall(str)
        if m_project_name:
            #for l in m_project_name:
            l = m_project_name[0]
            l = l.decode()
            l.replace('\r','')
            l.replace('\n','')
            return l


    def get_bid_name(self):
        str = self.str
        re_bid_name=u"(?<=\u4e2d\u6807\u4eba\uff1a)[\u4e00-\u9fff]+|(?<=\u6210\u4ea4\u4f9b\u5e94\u5546\uff1a)[\u4e00-\u9fff]+|(?<=\u4e2d\u6807\u4eba\uff1a)[\u4e00-\u9fff]+|(?<=\u6210\u4ea4\u5355\u4f4d\uff1a)[\u4e00-\u9fff]+"
        re_bid_name = re.compile(re_bid_name)
        m_bid_name = re_bid_name.findall(str)
        if m_bid_name:
            #for l in m_project_name:
            l = m_bid_name[0]                           #沙坝区是m_bid_name[0]
            l = l.decode()
            return l

    def get_bid_money(self):
        str = self.str
        re_bid_money = u"¥\d{1,10}\.\d\d"
        re_bid_money = re.compile(re_bid_money)
        m_bid_money = re_bid_money.findall(str)
        if m_bid_money:
            #for l in m_project_name:
            l = m_bid_money[0]
            l = l.decode()
            l = l.replace('；','')
            l = l.replace('。','')
            l = l.replace('：','')
            l = l.replace('\r','')
            l = l.replace('\n','')
            l = l.replace(' ','')
            return l

    def get_bid_time(self):
        str = self.str
        re_bid_time = u"\d+[\u4e00-\u9fff]\d+[\u4e00-\u9fff]\d+[\u4e00-\u9fff]"
        re_bid_time = re.compile(re_bid_time)
        m_bid_time = re_bid_time.findall(str)
        if m_bid_time:
            #for l in m_project_name:
            l = m_bid_time[0]
            l = l.decode()
            l = l.replace('；','')
            l = l.replace('。','')
            l = l.replace('：','')
            l = l.replace('\r','')
            l = l.replace('\n','')
            l = l.replace(' ','')
            return l
