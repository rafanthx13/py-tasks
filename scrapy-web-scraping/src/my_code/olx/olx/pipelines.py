# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class OlxSqlLitePipeline(object):

	# Processar cada Item
	def process_item(self, item, spider):
		# Testando o ItemPipeline
		# spider.log("Item Capturado -------------------------")
		self.bd.execute(
			'insert into cars(title, ports, year) values (:title, :ports, :year)',
			item
		)
		# Vou dar sempre um commit para garantir que para cada item vai inserir
		self.bd.commit()
		return item

	# Caso nao tiver a tabela vai criala
	def create_table(self):
		# Vamo verificar se existe essa tabela
		# sqllite_master vai serve para buscarmos informaçoes gerias o bd
		result = self.bd.execute(
			'SELECT name FROM sqlite_master WHERE type = "table" AND name = "cars" '
		)
		# result nao é uma lsita, é um iterator
		try:
			# Se eu consigo executar isso, significa que tem a tabela
			value = next(result)
		except StopIteration as ex:
			# nao tem a tabela, entao, vamos criala
			self.bd.execute(
				'create table cars(id integer primary key, title text, ports text, year text)'
			)

	# Quando a spider for executada
	def open_spider(self, spider):
		self.bd = sqlite3.connect('my-db-scrapy')
		self.create_table()

	def close_spider(self, spider):
		# Tem que fazer o commit
		self.bd.close()
