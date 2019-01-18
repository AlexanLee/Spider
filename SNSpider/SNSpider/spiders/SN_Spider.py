# - * - coding: utf-8 - * -

__author__ = "Alexan"

# -*- coding: utf-8 -*-
import scrapy
from SNSpider.items import SnspiderItem


class SnSpider(scrapy.Spider):
    name = 'SNSpider'
    start_urls = ['https://list.suning.com/0-20326-0.html']

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        #       for href in response.css('.question-summary h3 a::attr(href)'):
        #          full_url = response.urljoin(href.extract())
        #         yield scrapy.Request(full_url,headers=headers,callback=self.parse_question)
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, callback=self.parse_question)

    def parse_question(self, response):
        item = SnspiderItem()
        questions = response.css('div.title-selling-point')
        for question in questions:
            item['title'] = question.xpath("/a/text()").extract_first()
            item['content'] = question.xpath("/a/text()").extract_first()
            # item['url'] = question.xpath(
            #         ".//div[ contains(@class, 'answered')]/strong/text()").extract_first()
            # item['tags'] = question.xpath(".//div[contains(@class, 'tags')]/a/text()").extract()
            yield item
