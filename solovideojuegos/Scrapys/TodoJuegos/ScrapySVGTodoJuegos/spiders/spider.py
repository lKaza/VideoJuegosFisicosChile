import sys
reload(sys)
sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from ScrapySVGTodoJuegos.items import ScrapysvgtodojuegosItem
from selenium import webdriver
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from scrapy.utils.log import configure_logging

class SVGSpiderPS4(CrawlSpider):
	name = 'gamerspidertodojuegosPS4'
	item_count = 0
	allowed_domain = ['https://www.todojuegos.cl']
	start_urls = ['http://www.todojuegos.cl/Productos/Destacados/Ps4-Juegos-Disponibles/']

	rules = {
		# Para cada item
		#Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="ProdDisplayType5_MasProductos_32641"]/p'))), # Click en la paginacion
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@id="content"]/div[3]/table')), # Ingresa al contenido
							callback = 'parse_item', follow = False)
	}
	def parse_item(self, response):
		
		
		ml_item = ScrapysvgtodojuegosItem()
		#info de producto
		ml_item['titulo'] = response.xpath('//*[@id="content"]/div[3]/h1/text()').extract_first()
		ml_item['precio'] = response.xpath('//*[@id="content"]/div[5]/div[1]/h2/text()').extract()
		ml_item['link'] = 'http://www.todojuegos.cl/Productos/PS4/'+ml_item['titulo']
		#ml_item['sku'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][1]/span[@class="txValueInfoGral"]/text()').extract()
		ml_item['plataforma'] = 'PS4'

		self.item_count += 1
		if self.item_count > 300:
			raise CloseSpider('item_exceeded')
		yield ml_item


class SVGSpiderPS3(CrawlSpider):
	name = 'gamerspidertodojuegosPS3'
	item_count = 0
	allowed_domain = ['https://www.todojuegos.cl']
	start_urls = ['http://www.todojuegos.cl/Productos/Destacados/Ps3-Todos-Los-Disponibles/']

	rules = {
		# Para cada item
		#Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="ProdDisplayType5_MasProductos_32641"]/p'))), # Click en la paginacion
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@id="content"]/div[3]/table')), # Ingresa al contenido
							callback = 'parse_itemPS3', follow = False)
	}
	def parse_itemPS3(self, response):
		
		
		ml_item = ScrapysvgtodojuegosItem()
		#info de producto
		ml_item['titulo'] = response.xpath('//*[@id="content"]/div[3]/h1/text()').extract_first()
		ml_item['precio'] = response.xpath('//*[@id="content"]/div[5]/div[1]/h2/text()').extract()
		ml_item['link'] = 'http://www.todojuegos.cl/Productos/PS3/'+ml_item['titulo']
		#ml_item['sku'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][1]/span[@class="txValueInfoGral"]/text()').extract()
		ml_item['plataforma'] = 'PS3'

		self.item_count += 1
		if self.item_count > 300:
			raise CloseSpider('item_exceeded')
		yield ml_item

class SVGSpiderXONE(CrawlSpider):
	name = 'gamerspidertodojuegosxone'
	item_count = 0
	allowed_domain = ['https://www.todojuegos.cl']
	start_urls = ['http://www.todojuegos.cl/Productos/XONE/_juegos/']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="navLinkNext"]'))), # Click en la paginacion
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@id="ListadoResultados"]/table')), # Ingresa al contenido
							callback = 'parse_itemXOne', follow = False)
	}
	def parse_itemXOne(self, response):
		
		
		ml_item = ScrapysvgtodojuegosItem()
		#info de producto
		ml_item['titulo'] = response.xpath('//*[@id="content"]/div[3]/h1/text()').extract_first()
		ml_item['precio'] = response.xpath('//*[@id="content"]/div[5]/div[1]/h2/text()').extract()
		ml_item['link'] = 'http://www.todojuegos.cl/Productos/XONE/'+ml_item['titulo']
		#ml_item['sku'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][1]/span[@class="txValueInfoGral"]/text()').extract()
		ml_item['plataforma'] = 'XboxOne'

		self.item_count += 1
		if self.item_count > 300:
			raise CloseSpider('item_exceeded')
		yield ml_item

class SVGSpiderPSVITA(CrawlSpider):
	name = 'gamerspidertodojuegospsvita'
	item_count = 0
	allowed_domain = ['https://www.todojuegos.cl']
	start_urls = ['http://www.todojuegos.cl/Productos/PSV/_juegos/']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="navLinkNext"]'))), # Click en la paginacion
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@id="ListadoResultados"]/table')), # Ingresa al contenido
							callback = 'parse_itemPSVITA', follow = False)
	}
	def parse_itemPSVITA(self, response):
		
		
		ml_item = ScrapysvgtodojuegosItem()
		#info de producto
		ml_item['titulo'] = response.xpath('//*[@id="content"]/div[3]/h1/text()').extract_first()
		ml_item['precio'] = response.xpath('//*[@id="content"]/div[5]/div[1]/h2/text()').extract()
		ml_item['link'] = 'http://www.todojuegos.cl/Productos/PSV/'+ml_item['titulo']
		#ml_item['sku'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][1]/span[@class="txValueInfoGral"]/text()').extract()
		ml_item['plataforma'] = 'PSVita'

		self.item_count += 1
		if self.item_count > 300:
			raise CloseSpider('item_exceeded')
		yield ml_item


class SVGSpiderWIIU(CrawlSpider):
	name = 'gamerspidertodojuegospswiiu'
	item_count = 0
	allowed_domain = ['https://www.todojuegos.cl']
	start_urls = ['http://www.todojuegos.cl/Productos/wiiu/_juegos/']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="navLinkNext"]'))), # Click en la paginacion
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@id="ListadoResultados"]/table')), # Ingresa al contenido
							callback = 'parse_itemWiiu', follow = False)
	}
	def parse_itemWiiu(self, response):
		
		
		ml_item = ScrapysvgtodojuegosItem()
		#info de producto
		ml_item['titulo'] = response.xpath('//*[@id="content"]/div[3]/h1/text()').extract_first()
		ml_item['precio'] = response.xpath('//*[@id="content"]/div[5]/div[1]/h2/text()').extract()
		ml_item['link'] = 'http://www.todojuegos.cl/Productos/wiiu/'+ml_item['titulo']
		#ml_item['sku'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][1]/span[@class="txValueInfoGral"]/text()').extract()
		ml_item['plataforma'] = 'Wiiu'

		self.item_count += 1
		if self.item_count > 300:
			raise CloseSpider('item_exceeded')
		yield ml_item


class SVGSpiderNSWI(CrawlSpider):
	name = 'gamerspidertodojuegosNSWI'
	item_count = 0
	allowed_domain = ['https://www.todojuegos.cl']
	start_urls = ['http://www.todojuegos.cl/Productos/NSWI/_juegos/']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="navLinkNext"]'))), # Click en la paginacion
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@id="ListadoResultados"]/table')), # Ingresa al contenido
							callback = 'parse_itemNSWI', follow = False)
	}
	def parse_itemNSWI(self, response):
		
		
		ml_item = ScrapysvgtodojuegosItem()
		#info de producto
		ml_item['titulo'] = response.xpath('//*[@id="content"]/div[3]/h1/text()').extract_first()
		ml_item['precio'] = response.xpath('//*[@id="content"]/div[5]/div[1]/h2/text()').extract()
		ml_item['link'] = 'http://www.todojuegos.cl/Productos/NSWI/'+ml_item['titulo']
		#ml_item['sku'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][1]/span[@class="txValueInfoGral"]/text()').extract()
		ml_item['plataforma'] = 'NSWI'

		self.item_count += 1
		if self.item_count > 300:
			raise CloseSpider('item_exceeded')
		yield ml_item



configure_logging()
runner = CrawlerRunner()
runner.crawl(SVGSpiderPS4)
runner.crawl(SVGSpiderPS3)
runner.crawl(SVGSpiderXONE)
runner.crawl(SVGSpiderPSVITA)
runner.crawl(SVGSpiderNSWI)
runner.crawl(SVGSpiderWIIU)
d = runner.join()
d.addBoth(lambda _: reactor.stop())

reactor.run()