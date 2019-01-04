#!/usr/bin/python
# __*__coding:utf-8__*__

import os

files = os.listdir("process")

for f in files:
    print(f)
    with open("process/" + f) as f1:
        s = f1.read()
        if s:
            s = s.strip()
            s = s.lstrip('jsonp1916(')
            s = s.lstrip('jsonp2014(')
            s = s.rstrip(')')
        fo = open(f, "w")
        fo.write(s)
        fo.close()
