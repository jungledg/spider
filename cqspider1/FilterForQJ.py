# -*- coding: utf-8 -*-
import re
from items import Cqspider1Item
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
class FilterForQJ:
    def __init__(self,str=''):
        self.str = str
    def get_project_name(self):
        str = self.str
        re_project_name = u"(?<=\u9879\u76ee\u540d\u79f0\uff1a).*(?=\\n)"
        re_project_name = re.compile(re_project_name)
        m_project_name = re_project_name.findall(str)
        if m_project_name:
            #for l in m_project_name:
            l = m_project_name[0]
            l = l.decode()
            l = l.replace('；','')
            l = l.replace('。','')
            l = l.replace('：','')
            l = l.replace('\r','')
            l = l.replace('\n','')
            l = l.replace(' ','')
            return l
    def get_project_name_old(self):
        str = self.str
        re_project_name = u"(?<=\u9879\u76ee\u540d\u79f0\uff1a).*(?=\u91c7\u8d2d)"
        re_project_name = re.compile(re_project_name)
        m_project_name = re_project_name.findall(str)
        if m_project_name:
            #for l in m_project_name:
            l = m_project_name[0]
            l = l.decode()
            l = l.replace('；','')
            l = l.replace('。','')
            l = l.replace('：','')
            l = l.replace('\r','')
            l = l.replace('\n','')
            l = l.replace(' ','')
            return l


        pass
    def get_bid_name_new(self):

        str = self.str
        re_bid_name=u"(?<=\u4e2d\u6807\u4eba\uff1a)[\u4e00-\u9fff]+|(?<=\u6210\u4ea4\u4f9b\u5e94\u5546\uff1a)[\u4e00-\u9fff]+|(?<=\u4e2d\u6807\u4eba\uff1a)[\u4e00-\u9fff]+|(?<=\u6210\u4ea4\u5355\u4f4d\uff1a)[\u4e00-\u9fff]+"
        re_bid_name = re.compile(re_bid_name)
        m_bid_name = re_bid_name.findall(str)
        if m_bid_name:
            #for l in m_project_name:
            l = m_bid_name[0]                           #沙坝区是m_bid_name[0]
            l = l.decode()
            l = l.replace('；','')
            l = l.replace('。','')
            l = l.replace('：','')
            l = l.replace('\r','')
            l = l.replace('\n','')
            l = l.replace(' ','')
            return l
    def get_bid_name(self):
        str = self.str
        re_bid_name=u"(?<=\u4e2d\u6807\u4eba\uff1a).*[\u4e00-\u9fff]+|(?<=\u4e2d\u6807\u5355\u4f4d\uff1a)[\u4e00-\u9fff]+"
        re_bid_name = re.compile(re_bid_name)
        m_bid_name = re_bid_name.findall(str)
        if m_bid_name:
            #for l in m_project_name:
            l = m_bid_name[0]                           #沙坝区是m_bid_name[0]
            l = l.decode()
            l = l.replace('；','')
            l = l.replace('。','')
            l = l.replace('：','')
            l = l.replace('\r','')
            l = l.replace('\n','')
            l = l.replace(' ','')
            return l
    def get_bid_money(self):
        str = self.str
        re_bid_money = u"(?<=\u4e2d\u6807\u91d1\u989d\uff1a).+"
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
    def get_bid_money_old(self):
        str = self.str
        re_bid_money = u"(?<=\u4e2d\u6807\u91d1\u989d)\\n*\d+(\.\d\d)(?=[\u4e00-\u9fff])"
        re_bid_money = re.compile(re_bid_money)
        m_bid_money = re_bid_money.findall(str)
        if m_bid_money:
            #for l in m_project_name:
            l = m_bid_money[0]
            l = l.decode()
            return l

    def get_bid_time_new(self):
        str = self.str
        re_bid_time = u"\d+[\u4e00-\u9fff]\d+[\u4e00-\u9fff]\d+[\u4e00-\u9fff]"
        re_bid_time = re.compile(re_bid_time)
        m_bid_time = re_bid_time.findall(str)
        if m_bid_time:
            #for l in m_project_name:
            l = m_bid_time[0]
            l = l.decode()
            return l

    def get_bid_time(self):
        str = self.str
        re_bid_time = u"(?<=\u516c\u793a\u65e5\u671f\uff1a).*\d+\u5e74\d+\u6708\d+\u65e5"
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
