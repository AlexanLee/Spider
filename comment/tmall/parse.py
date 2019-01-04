# _*_:coding:utf-8_*_

import os
import re
import simplejson

files = os.listdir("resource")

users = open("users.txt", 'w')

for f in files:
    print(f)
    str_st = open("resource/" + f).read().decode('utf-8').replace('\0', '')
    str_st = re.sub("u'", "\"", str_st)
    json = simplejson.loads(str_st)
    cards = json.get("rateDetail", {}).get("rateList", {})
    for card in cards:
        id = card.get("id", '')
        sellerId = card.get("sellerId", '')
        name = card.get("displayUserNick", '')
        rateContent = card.get("rateContent", '')
        position = card.get("position", '')
        rateDate = card.get("rateDate", '')

        print>> users, str(id) + '\t' + str(sellerId) + '\t' + str(
                name.encode("utf_8")) + '\t' + str(
                rateContent.encode("utf_8")) + '\t' + str(position) + '\t' + str(
                rateDate.encode("utf_8").strip('\t'))
