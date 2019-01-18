#!/usr/bin/python
# __*__coding:utf-8__*__

import os

import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud


class Pre(object):
    def __init__(self):
        self.process = 'process/'
        self.stoppath = u'/data/pg/jd/stopwords/百度停用词表.txt'
        self.stopwords = []

    @staticmethod
    def file2json(self):
        files = os.listdir(self.process)
        for f in files:
            print(f)
            with open(self.process + f) as f1:
                s = f1.read()
                if s:
                    s = s.strip()
                    s = s.lstrip('jsonp1916(')
                    s = s.lstrip('jsonp2014(')
                    s = s.rstrip(')')
                fo = open(f, "w")
                fo.write(s)
                fo.close()

    @staticmethod
    def unduplicate(infile):
        with open(infile) as fin:
            f = fin.readlines()
            f = list(set(f))
            print(len(f))
            fo = open(infile, "w")
            for fw in f:
                fo.write(fw)
            fo.close()

    def draw(self, infile):
        t = open(infile).read()
        w = [word for word in jieba.cut(t) if word not in self.stopwords]
        wl = ' '.join(w)
        font = r'DroidSansFallbackFull.ttf'
        my_wordcloud = WordCloud(font_path=font).generate(wl)
        plt.imshow(my_wordcloud)
        plt.axis("off")
        plt.show()

    def read_stop_words(self):
        with open(self.stoppath, 'r+') as f:
            for line in f.readlines():
                self.stopwords.append(line)


if __name__ == '__main__':
    print('main')
    # Pre.unduplicate('users.txt')
    p = Pre()
    p.read_stop_words()
    p.draw('content.txt')
