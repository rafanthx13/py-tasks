# -*- coding: utf-8 -*-
import scrapy

from scrapy.loader import VeducaItemLoader # Item
from scrapy.loader.processors import TakeFirst # Executar o Extract First
from courses.items import CourseItem 



class VeducaSpider(scrapy.Spider):
    name = 'veduca'
    allowed_domains = ['veduca.org']
    start_urls = ['https://veduca.org/courses']

    def parse(self, response):
        course_list = response.xpath("//div[contains(@class, 'course-list')]//a")
        for course_item in course_list:
            url = course_item.xpath(".//@href").extract_first()
            url = 'https://veduca.org%s' % url
            yield scrapy.Request(
                url = url, callback = self.parse_detail
            )
        next_page = response.xpath(
            "//span[contains(@class, 'next')]/a/@href"
        ).extract_first()
        # Agora, se tiver o "Next" na pagina, vai pegalo, se nao conseguir tem valor FALSE
        # Depois agente testa ele, se existir, entao avaça na página
        if next_page:
            self.log('PAGE: %s' % next_page)
            url = 'https://veduca.org%s' % next_page
            yield scrapy.Request(
                url=url, callback=self.parse
            )
    
    def parse_detail(self, response):
        # Item  - Classe/Dicionairo que define o item pra ser manipulado
        # ItemLoader = Responsavel por escolhar os  xpath e definir os dados do item a ser processado
        #	Os comandos do IteLoader sao carregados aqui mesmo
        # Processor = forma de como pegar, no caos usamos Take_First, significa que vai busca a primeira ocorrencia para cada xpath
        loader = VeducaItemLoader(CourseItem(), response = response) #
        loader.add_value('url', response.url)
        loader.add_xpath(
            'title', '//*[contains(@class, "course-title")]/text()'
        )
        loader.add_xpath(
            'headline', '//*[contains(@class, "course-subtitle")]/text()'
        )
        loader.add_xpath(
            'instructors', '//*[contains(@class, "author-name")]/text()'
        )
        loader.add_xpath(
            'lectures', '//a[contains(@class, "item")]/@href'
        )
        loader.add_xpath(
            'instructors_description', '//div[contains(@class, "bio")]/div/div/div/div/div[2]'
        )
        yield loader.load_item() # Vai gerar o Item
