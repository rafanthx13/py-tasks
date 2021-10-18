# -*- coding: utf-8 -*-
import scrapy

# response.xpath('//div[contains(@class, "module_pagination")]//a[@rel = "next"]/@href').extract_first()

# response.xpath("//span[contains(text(), 'Ano')]/following-sibling::strong/a/@title").extract_first()

class CarsSpider(scrapy.Spider):
	name = 'cars'
	allowed_domains = ['pe.olx.com.br'] # dominios permitdos, cuidado caso for entra rnuma url muito diferente
	start_urls = ['https://pe.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/']

	def parse(self, response):
		items = response.xpath('//ul[@id="main-ad-list"]/li[not(contains(@class, "list_native"))]') 
			# busca a ul que tem id = main-ad-list, pego todos os itens que nao sejam o de propaganda ad-sense
		self.log(len(items))
		for item in items:
			url = item.xpath('./a/@href').extract_first() # vou pegar o link desse recurso
			yield scrapy.Request(url = url, callback = self.parse_detail) # acesasndo cada item internao
		next_page = response.xpath(
			'//div[contains(@class, "module_pagination")]//a[@rel = "next"]/@href'
		)
		# O scrapy faz de forma assyncronoa, por causa disos, ele vai logar na ordem que der pra ele
		# cuidado, que, ao rodar isso, vai executar cerca 750 paginas * 50 itens, entao, de um CRL + C
		if next_page:
			self.log('Próxima Página: {}'.format(next_page.extract_first()))
			# self.log('Próxima Página: %s' % next_page.extract_first())
			# vou fazer de forma recursiva até  chegar a ultima pagina
			yield scrapy.Request(
			    url = next_page.extract_first(), callback = self.parse
			)



	def parse_detail(self, response):
		# self.log(response.url)
		title = response.xpath('//title/text()').extract_first()
		year = response.xpath(
			'//span[contains(text(), "Ano")]/following-sibling::strong/a/@title'
		).extract_first()
		ports = response.xpath(
			'//span[contains(text(), "Portas")]/following-sibling::strong/text()'
		).extract_first()
		yield {
			'title': title,
			'year': year,
			'ports': ports,
		}
