#coding:utf-8
import urllib2
import gevent
from gevent import monkey, queue
monkey.patch_all()

proxy_file = 'proxy.txt'

refer = "http://jupaijituan.veigou.com/s/activity/vote/1420?from=groupmessage&isappinstalled=0"
url = "http://jupaijituan.veigou.com/s/activity/save/1420?from=groupmessage&isappinstalled=0"
data = "data%5B%5D=5"

def vote(proxy, url, refer):
    enable_proxy = True
    proxy_handler = urllib2.ProxyHandler({"http" : 'http://%s' % proxy})
    null_proxy_handler = urllib2.ProxyHandler({})
     
    if enable_proxy:
        opener = urllib2.build_opener(proxy_handler)
    else:
        opener = urllib2.build_opener(null_proxy_handler)

    urllib2.install_opener(opener)

    req = urllib2.Request(url,data)
    req.add_header("User-Agent", 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.18) Gecko/20110614 Firefox/3.6.18')
    req.add_header( "Referer", refer)
    res = urllib2.urlopen( req )
    html = res.read()
    res.close()
    #return html
    print proxy, html

def worker(n):
    while True:
        proxy = q.get()
        try:
            vote(proxy, url, refer)
        except:
            pass
        finally:
            q.task_done()

q = queue.JoinableQueue()
num_worker_threads = 40

proxys = open(proxy_file).readlines()
for p in proxys:
    q.put(p.strip())

for i in range(num_worker_threads):
    gevent.spawn(worker, i)

q.join()
