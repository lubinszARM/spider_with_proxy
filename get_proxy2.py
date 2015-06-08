#coding:utf-8

import urllib2
from lxml import etree, html

urls = [
        'http://spys.ru/en/http-proxy-list/',
        'http://spys.ru/en/http-proxy-list/1/',
        'http://spys.ru/en/http-proxy-list/2/',
        'http://spys.ru/en/http-proxy-list/3/',
    ]

def getproxy(url):
    try:
        rs = urllib2.urlopen(url).read()
    except:
        return
    tree = html.fromstring(rs)
    ip = tree.xpath('//td/font[@class="spy14"]')
    for i in ip:
        print i.next.text


getproxy('http://spys.ru/en/http-proxy-list/')
#for i in range(1,26):
#    getproxy(url % i)
