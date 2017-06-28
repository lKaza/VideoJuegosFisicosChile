import sys
reload(sys)
sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from sernatur.items import SernaturItem

class SernaturSpider(CrawlSpider):
	name = 'gamerspider'
	item_count = 0
	allowed_domain = ['https://www.zmart.cl']
	start_urls = ['https://www.zmart.cl/JuegosPS4']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="ProdDisplayType5_MasProductos_32641"]/p'))), # Click en la paginacion
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@id="BoxProdDisplay63033"]/div[1]/a')), # Ingresa al contenido
							callback = 'parse_item', follow = False)
	}

	def parse_item(self, response):
		ml_item = SernaturItem()
		#info de producto
		ml_item['nombre'] = response.xpath('//*[@id="ficha_producto_int"]/h1/text()').extract_first()
		ml_item['precio'] = response.xpath('//*[@id="PriceProduct"]/text()').extract()
		self.item_count += 1
		if self.item_count > 30:
			raise CloseSpider('item_exceeded')
		yield ml_item


