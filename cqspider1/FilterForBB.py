# coding=utf-8
import re
import sys
class FilterForBB:
    def __init__(self,str = ''):
        self.str = str
    def get_project_name(self):
        str = self.str
        re_project_name = u"(?<=\u9879\u76ee\u540d\u79f0).+(?=\u9879\u76ee)|(?<=\u9879\u76ee\u540d\u79f0).+"
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
    def get_bid_name(self):
        str = self.str
        re_bid_name=u"(?<=\u6210\u4ea4\u4f9b\u5e94\u5546).+|(?<=\u4e2d\u6807\u516c\u53f8).+"
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
        re_bid_money = u"(?<=\u6210\u4ea4\u4ef7\u683c).+"
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
        re_bid_time = u"\d+\s*\u5e74\s*\d+\s*\u6708\s*\d+\s*\u65e5"
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