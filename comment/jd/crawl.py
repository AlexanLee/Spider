#!/usr/bin/python
# coding:utf-8
import re
import json
import urllib2
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
file = open('jd.txt', 'w')


def crawlProductComment(url):
    page = urllib2.urlopen(url)
    html = page.read().decode('gbk')
    data0 = re.sub(u'^fetchJSON_comment98vv948\(', '', html)
    reg1 = re.compile('\);')
    data1 = reg1.sub('', data0)
    data = json.loads(data1)
    for i in data['comments']:
        file.write("{}".format(i['id']))
        file.write("|{}".format(i['guid']))
        productName = i['referenceName'].encode('utf-8')
        file.write("|{}".format(productName))
        commentTime = i['creationTime'].encode('utf-8')
        file.write("|{}".format(commentTime))
        nickname = i['nickname'].encode('utf-8')
        file.write("|{}".format(nickname))
        userLevelName = i['userLevelName'].encode('utf-8')
        file.write("|{}".format(userLevelName))
        userClientShow = i['userClientShow'].encode('utf-8')
        file.write("|{}".format(userClientShow))
        content = i['content'].encode('utf-8')
        file.write("|{}".format(content) + '\n')


for i in range(0, 300):
    print(i)
    time.sleep(5)
    url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv948&productId=100002075752&score=0&sortType=1&page=' + str(
            i) + '&pageSize=10&isShadowSku=0&fold=1'
    crawlProductComment(url)
file.close()
