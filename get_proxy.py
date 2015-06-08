#coding:utf-8

import urllib2
from lxml import etree, html

url = "http://www.samair.ru/proxy/proxy-%d.htm"

def getproxy(url):
    try:
        rs = urllib2.urlopen(url).read()
    except:
        return
    tree = html.fromstring(rs)
    ip = tree.xpath('//table[@class="tablelist"]/tr/td')
    for i in ip:
        if i.text and ':' in i.text:
            print i.text


#getproxy('http://www.samair.ru/proxy/proxy-25.htm')
for i in range(1,26):
    getproxy(url % i)
