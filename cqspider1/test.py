# -*- coding=utf-8 -*-
import re
import time,datetime
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
p = '\u9879\u76ee\u540d\u79f0\uff1a\w\n+$'
#f=open('data.txt','r')
#f=open('cqjj_data.txt','r')
f=open('cqbb_data.txt','r')
#f=open('cqddk_data.txt','r')
#f=open('cqhc_data.txt','r')
#f=open('cqyb_data.txt','r')
#f=open('cqzh_data.txt','r')
#f=open('cqqj_data.txt','r')
try:
    content = f.read()
finally:
    f.close()
if content:
    print 'exist'
content=content.decode('utf8')
xx = u"\d+\.?\d*\s*[\u4e00-\u9fff]?(?=\u5143)|\d+\.\d*(?=\s)"
#pr = u'\u9879\u76ee\u540d\u79f0'
#xx = pr + u"((\\n|.)*\u4e09\u5ce1\u5e7f\u573a\u5546\u5708\u7ba1\u7406\u59d4\u5458\u4f1a\u516c\u5171\u8bbe\u65bd\u7ba1\u7406\u670d\u52a1\u4e2d\u5fc3\u91c7\u8d2d\u82b1\u8349)"
pattern = re.compile(xx)
m = pattern.findall(content)
count = 0
# for k in m:
#     count += 1
#     #for l in m_project_name:
#     l = k
#     l = l.decode()
#     l = l.replace('；','')
#     l = l.replace('。','')
#     l = l.replace('：','')
#     l = l.replace('\r','')
#     l = l.replace('\n','')
#     l = l.replace(' ','')
#     re_money = u"\d+\u5e74\d+\u6708\d+\u65e5"
#     re_money = re.compile(re_money)
#     l = re_money.findall(l)
#     l = l[0]
#     l = time.strptime(l,u"%Y\u5e74%m\u6708%d\u65e5")
#     l = datetime.date(l.tm_year,l.tm_mon,l.tm_mday)
#     l = l.strftime("%Y-%m-%d")
#     print l
# print count
#m = re.search(r'\s+\d+9\s+',content)
if m:
    print m
    print m.__len__()
    m = m[0]
    print 'GG',m
    m = m.encode()
    m = m.replace('\r','')
    m = m.replace(' ','')
    m = m.replace('：','')
    #m = m.replace('\n',' ')
    list = m.replace('\n','')
    count = 0
    flag = 0
    print list
    # while True:
    #     if list[count]:
    #         print list[count]
    #         count += 1

else:
    print 'no match'
#print m
# import re
# text = "JGood is a handsome boy, he is cool, clever, and so on..."
# m = re.search(r'\shandsome\s', text)
# if m:
#     print m.group(0)
# else:
#     print 'not search'