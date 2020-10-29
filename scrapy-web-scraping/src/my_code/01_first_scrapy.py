import scrapy

class GilenoSpider(scrapy.Spider):

	# Toda Spyder tem que ter um 'name'
	name = 'gilenofilho'
	# start_urls : Quando tem, recebe uma lsita de urls que ira acessar
	# se tem , entoa vai acesssar ess pagina
	start_urls = ['http://www.gilenofilho.com.br']

	# por default, ao acessar executa 'parse', e tem o retorno do callback
	def parse(self, response):
		# log serve para imprimir no terminal
		self.log('Hello World')
		self.log(response.body)

# executa com:
# scrapy runspider 01_first_scrapy.py

