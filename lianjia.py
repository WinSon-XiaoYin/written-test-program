# -*- coding: utf-8 -*-

import requests
from lxml import etree
import time

urls = []
for i in xrange(1, 101):
    url = "http://wh.lianjia.com/ershoufang/pg{page}/".format(page=i)
    urls.append(url)

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/56.0.2924.76 Chrome/56.0.2924.76 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive"
}

for url in urls:
    html = requests.get(url, headers=headers)
    print "状态: {status}".format(status=html.status_code)
    temps = etree.HTML(html.text).xpath('/html/body/div[4]/div[1]/ul/li')
    for temp in temps:
        title = temp.xpath('div/div/a/text()')[0]
        address1 = temp.xpath('div/div[2]/div/a/text()')[0]
        address2 = temp.xpath('div/div[2]/div/text()')[0]
        flood1 = temp.xpath('div/div[3]/div/text()')[0]
        flood2 = temp.xpath('div/div[3]/div/a/text()')[0]
        followInfo = temp.xpath('div/div[4]/text()')[0]
        tag1 = temp.xpath('div/div[5]/span[1]/text()')[0]
        tag2 = temp.xpath('div/div[5]/span[2]/text()')[0]
        address = address1 + address2
        flood = flood1 + flood2
        tag = tag1 + tag2
        with open('./data.txt', 'a') as data:
            print "开始写数据"
            data.write(title.encode('utf-8'))
            data.write('\n')
            data.write(address.encode('utf-8'))
            data.write('\n')
            data.write(flood.encode('utf-8'))
            data.write('\n')
            data.write(followInfo.encode('utf-8'))
            data.write('\n')
            data.write(tag.encode('utf-8'))
            data.write('\n')
            data.write('\n')
    print "爬完一页"
    time.sleep(2)


