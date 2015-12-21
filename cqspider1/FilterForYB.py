# coding=utf-8
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
class FilterForYB:
    def __init__(self,str = ''):
        self.str = str
    def get_project_name(self):
        str = self.str
        re_project_name = u"(?<=\u9879\u76ee\u540d\u79f0.)\s*([\u4e00-\u9fff]+\([\u4e00-\u9fff]+\)[\u4e00-\u9fff]*|[\u4e00-\u9fff]+)"
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
        re_bid_name=u"(?<=\u5019\u9009\u4eba)：?\s*[\u4e00-\u9fff]+|(?<=\u6210\u4ea4\u4eba)：?\s*[\u4e00-\u9fff]+|(?<=\u4e2d\u6807\u4eba)：?\s*[\u4e00-\u9fff]+|(?<=\u4f9b\u5e94\u5546\u4e3a)\s*[\u4e00-\u9fff]+|(?<=\u4e2d\u6807\u5355\u4f4d\u4e3a)：?\s*[\u4e00-\u9fff]+|(?<=\u4f9b\u5e94\u5546\u540d\u79f0)：?\s*[\u4e00-\u9fff]+"
        re_bid_name = re.compile(re_bid_name)
        m_bid_name = re_bid_name.findall(str)
        if m_bid_name:
            l = m_bid_name[0]
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
        re_bid_money = u"(?<=\u62a5\u4ef7\u4e3a)\s*\d+|(?<=\u6210\u4ea4\u91d1\u989d).\s*.+|(?<=\u4e2d\u6807\u91d1\u989d\u4e3a)\s*\d+\s*[\u4e00-\u9fff]*|(?<=\u4e2d\u6807\u4ef7\u683c\u4e3a).\s*\d+\s*[\u4e00-\u9fff]*|(?<=\u0020\u6210\u4ea4\u7ed3\u679c)：?\s*.*|(?<=\u62a5\u4ef7)：?\s*\d+[\u4e00-\u9fff]+"
        re_bid_money = re.compile(re_bid_money)
        m_bid_money = re_bid_money.findall(str)
        if m_bid_money:
            #for l in m_project_name:
            l = m_bid_money[0]
            l = l.decode()
            l = l.replace(u'\xa0', u' ')
            l = l.replace('；','')
            l = l.replace('。','')
            l = l.replace('：','')
            l = l.replace('\r','')
            l = l.replace('\n','')
            l = l.replace(' ','')
            return l
    def get_bid_time(self):
        str = self.str
        re_bid_time = u"(?<=\u6210\u4ea4\u4eba\u65e5\u671f).\s*\d+\s*\u5e74\s*\d+\s*\u6708\s*\d+\s*\u65e5|(?<=\u8bc4\u5ba1\u65e5\u671f).\s*\d+\s*\u5e74\s*\d+\s*\u6708\s*\d+\s*\u65e5|(?<=\u8bc4\u5ba1\u65e5\u671f).\s*\d+\s*-\s*\d+\s*-\s*\d+"
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