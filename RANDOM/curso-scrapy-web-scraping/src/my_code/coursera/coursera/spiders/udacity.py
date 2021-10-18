# -*- coding: utf-8 -*-
import scrapy


class UdacitySpider(scrapy.Spider):
    name = 'udacity'
    start_urls = ['http://https://br.udacity.com/courses/all/']

    def parse(self, response):
        pass
