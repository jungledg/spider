# -*- coding=utf-8 -*-
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
p = '\u9879\u76ee\u540d\u79f0\uff1a\w\n+$'
f=open('data.txt','r')
try:
    content = f.read()
finally:
    f.close()
if content:
    print 'exist'
content=content.decode('utf8')
xx = u"(\d+[\u4e00-\u9fff]\d+[\u4e00-\u9fff]\d+[\u4e00-\u9fff])"
#pr = u'\u9879\u76ee\u540d\u79f0'
#xx = pr + u"((\\n|.)*\u4e09\u5ce1\u5e7f\u573a\u5546\u5708\u7ba1\u7406\u59d4\u5458\u4f1a\u516c\u5171\u8bbe\u65bd\u7ba1\u7406\u670d\u52a1\u4e2d\u5fc3\u91c7\u8d2d\u82b1\u8349)"
pattern = re.compile(xx)
m = pattern.findall(content)
#m = re.search(r'\s+\d+9\s+',content)
if m:
    print m


    print 'GG',m[0]
    m = m.encode()
    m = m.replace('\r','')
    #m = m.replace('\n',' ')
    list = m.split('\n')
    count = 0
    flag = 0
    print list[1]
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