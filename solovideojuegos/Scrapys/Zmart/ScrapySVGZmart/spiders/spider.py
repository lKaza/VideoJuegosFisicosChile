import sys
reload(sys)
sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from ScrapySVGZmart.items import SVGItem
from selenium import webdriver
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from scrapy.utils.log import configure_logging


class SVGSpiderPS4(CrawlSpider):
	name = 'gamerspiderzmartPS4'
	item_count = 0
	allowed_domain = ['https://www.zmart.cl']
	start_urls = ['https://www.zmart.cl/JuegosPS4']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="ProdDisplayType5_MasProductos_32641"]/p'))), # Click en la paginacion
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@id="ProdDisplayType5_32641_Products"]')), # Ingresa al contenido
							callback = 'parse_item', follow = False)
	}

	def parse_item(self, response):
		
		zmart = 'https://www.zmart.cl/'
		ml_item = SVGItem()
		#info de producto
		ml_item['titulo'] = response.xpath('//*[@id="ficha_producto_int"]/h1/text()').extract_first()
		ml_item['precio'] = response.xpath('//*[@id="PriceProduct"]/text()[not(parent::span[@class="SignoPriceProduct"])and normalize-space()]').extract()
		ml_item['link'] = response.xpath('//*[@id="HeaderInfoMiddlePerfil_Box_2"]/a/@href').extract()
		ml_item['sku'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][1]/span[@class="txValueInfoGral"]/text()').extract()
		ml_item['plataforma'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][2]/span[@class="txValueInfoGral"]/text()').extract()

		self.item_count += 1
		if self.item_count > 100:
			raise CloseSpider('item_exceeded')
		yield ml_item

class SVGSpiderXONE(CrawlSpider):
	name = 'gamerspiderzmartXONE'
	item_count = 0
	allowed_domain = ['https://www.zmart.cl']
	start_urls = ['https://www.zmart.cl/JuegosXBONE']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="ProdDisplayType5_MasProductos_32641"]/p'))), # Click en la paginacion
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@id="ProdDisplayType5_32641_Products"]')), # Ingresa al contenido
							callback = 'parse_itemXONE', follow = False)
	}

	def parse_itemXONE(self, response):
		
		zmart = 'https://www.zmart.cl/'
		ml_item = SVGItem()
		#info de producto
		ml_item['titulo'] = response.xpath('//*[@id="ficha_producto_int"]/h1/text()').extract_first()
		ml_item['precio'] = response.xpath('//*[@id="PriceProduct"]/text()[not(parent::span[@class="SignoPriceProduct"])and normalize-space()]').extract()
		ml_item['link'] = response.xpath('//*[@id="HeaderInfoMiddlePerfil_Box_2"]/a/@href').extract()
		ml_item['sku'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][1]/span[@class="txValueInfoGral"]/text()').extract()
		ml_item['plataforma'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][2]/span[@class="txValueInfoGral"]/text()').extract()

		self.item_count += 1
		if self.item_count > 100:
			raise CloseSpider('item_exceeded')
		yield ml_item

class SVGSpiderNSWI(CrawlSpider):
	name = 'gamerspiderzmartNSWI'
	item_count = 0
	allowed_domain = ['https://www.zmart.cl']
	start_urls = ['https://www.zmart.cl/JuegosNSWI']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="ProdDisplayType5_MasProductos_32641"]/p'))), # Click en la paginacion
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@id="ProdDisplayType5_32641_Products"]')), # Ingresa al contenido
							callback = 'parse_itemNSWI', follow = False)
	}

	def parse_itemNSWI(self, response):
		
		zmart = 'https://www.zmart.cl/'
		ml_item = SVGItem()
		#info de producto
		ml_item['titulo'] = response.xpath('//*[@id="ficha_producto_int"]/h1/text()').extract_first()
		ml_item['precio'] = response.xpath('//*[@id="PriceProduct"]/text()[not(parent::span[@class="SignoPriceProduct"])and normalize-space()]').extract()
		ml_item['link'] = response.xpath('//*[@id="HeaderInfoMiddlePerfil_Box_2"]/a/@href').extract()
		ml_item['sku'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][1]/span[@class="txValueInfoGral"]/text()').extract()
		ml_item['plataforma'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][2]/span[@class="txValueInfoGral"]/text()').extract()

		self.item_count += 1
		if self.item_count > 100:
			raise CloseSpider('item_exceeded')
		yield ml_item

class SVGSpiderWIIU(CrawlSpider):
	name = 'gamerspiderzmartWIIU'
	item_count = 0
	allowed_domain = ['https://www.zmart.cl']
	start_urls = ['https://www.zmart.cl/JuegosWIIU']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="ProdDisplayType5_MasProductos_32641"]/p'))), # Click en la paginacion
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@id="ProdDisplayType5_32641_Products"]')), # Ingresa al contenido
							callback = 'parse_itemWIIU', follow = False)
	}

	def parse_itemWIIU(self, response):
		
		zmart = 'https://www.zmart.cl/'
		ml_item = SVGItem()
		#info de producto
		ml_item['titulo'] = response.xpath('//*[@id="ficha_producto_int"]/h1/text()').extract_first()
		ml_item['precio'] = response.xpath('//*[@id="PriceProduct"]/text()[not(parent::span[@class="SignoPriceProduct"])and normalize-space()]').extract()
		ml_item['link'] = response.xpath('//*[@id="HeaderInfoMiddlePerfil_Box_2"]/a/@href').extract()
		ml_item['sku'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][1]/span[@class="txValueInfoGral"]/text()').extract()
		ml_item['plataforma'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][2]/span[@class="txValueInfoGral"]/text()').extract()

		self.item_count += 1
		if self.item_count > 100:
			raise CloseSpider('item_exceeded')
		yield ml_item

class SVGSpiderX360(CrawlSpider):
	name = 'gamerspiderzmartX360'
	item_count = 0
	allowed_domain = ['https://www.zmart.cl']
	start_urls = ['https://www.zmart.cl/JuegosXB360']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="ProdDisplayType5_MasProductos_32641"]/p'))), # Click en la paginacion
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@id="ProdDisplayType5_32641_Products"]')), # Ingresa al contenido
							callback = 'parse_itemX360', follow = False)
	}

	def parse_itemX360(self, response):
		
		zmart = 'https://www.zmart.cl/'
		ml_item = SVGItem()
		#info de producto
		ml_item['titulo'] = response.xpath('//*[@id="ficha_producto_int"]/h1/text()').extract_first()
		ml_item['precio'] = response.xpath('//*[@id="PriceProduct"]/text()[not(parent::span[@class="SignoPriceProduct"])and normalize-space()]').extract()
		ml_item['link'] = response.xpath('//*[@id="HeaderInfoMiddlePerfil_Box_2"]/a/@href').extract()
		ml_item['sku'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][1]/span[@class="txValueInfoGral"]/text()').extract()
		ml_item['plataforma'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][2]/span[@class="txValueInfoGral"]/text()').extract()

		self.item_count += 1
		if self.item_count > 100:
			raise CloseSpider('item_exceeded')
		yield ml_item


class SVGSpiderN3DS(CrawlSpider):
	name = 'gamerspiderzmartN3DS'
	item_count = 0
	allowed_domain = ['https://www.zmart.cl']
	start_urls = ['https://www.zmart.cl/JuegosN3DS']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="ProdDisplayType5_MasProductos_32641"]/p'))), # Click en la paginacion
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@id="ProdDisplayType5_32641_Products"]')), # Ingresa al contenido
							callback = 'parse_itemN3DS', follow = False)
	}

	def parse_itemN3DS(self, response):
		
		zmart = 'https://www.zmart.cl/'
		ml_item = SVGItem()
		#info de producto
		ml_item['titulo'] = response.xpath('//*[@id="ficha_producto_int"]/h1/text()').extract_first()
		ml_item['precio'] = response.xpath('//*[@id="PriceProduct"]/text()[not(parent::span[@class="SignoPriceProduct"])and normalize-space()]').extract()
		ml_item['link'] = response.xpath('//*[@id="HeaderInfoMiddlePerfil_Box_2"]/a/@href').extract()
		ml_item['sku'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][1]/span[@class="txValueInfoGral"]/text()').extract()
		ml_item['plataforma'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][2]/span[@class="txValueInfoGral"]/text()').extract()

		self.item_count += 1
		if self.item_count > 100:
			raise CloseSpider('item_exceeded')
		yield ml_item

class SVGSpiderPSVITA(CrawlSpider):
	name = 'gamerspiderzmartPSVITA'
	item_count = 0
	allowed_domain = ['https://www.zmart.cl']
	start_urls = ['https://www.zmart.cl/JuegosPSVITA']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="ProdDisplayType5_MasProductos_32641"]/p'))), # Click en la paginacion
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@id="ProdDisplayType5_32641_Products"]')), # Ingresa al contenido
							callback = 'parse_itemPSVITA', follow = False)
	}

	def parse_itemPSVITA(self, response):
		
		zmart = 'https://www.zmart.cl/'
		ml_item = SVGItem()
		#info de producto
		ml_item['titulo'] = response.xpath('//*[@id="ficha_producto_int"]/h1/text()').extract_first()
		ml_item['precio'] = response.xpath('//*[@id="PriceProduct"]/text()[not(parent::span[@class="SignoPriceProduct"])and normalize-space()]').extract()
		ml_item['link'] = response.xpath('//*[@id="HeaderInfoMiddlePerfil_Box_2"]/a/@href').extract()
		ml_item['sku'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][1]/span[@class="txValueInfoGral"]/text()').extract()
		ml_item['plataforma'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][2]/span[@class="txValueInfoGral"]/text()').extract()

		self.item_count += 1
		if self.item_count > 100:
			raise CloseSpider('item_exceeded')
		yield ml_item

class SVGSpiderPS3(CrawlSpider):
	name = 'gamerspiderzmartPS3'
	item_count = 0
	allowed_domain = ['https://www.zmart.cl']
	start_urls = ['https://www.zmart.cl/JuegosPS3']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="ProdDisplayType5_MasProductos_32641"]/p'))), # Click en la paginacion
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@id="ProdDisplayType5_32641_Products"]')), # Ingresa al contenido
							callback = 'parse_itemPS3', follow = False)
	}

	def parse_itemPS3(self, response):
		
		zmart = 'https://www.zmart.cl/'
		ml_item = SVGItem()
		#info de producto
		ml_item['titulo'] = response.xpath('//*[@id="ficha_producto_int"]/h1/text()').extract_first()
		ml_item['precio'] = response.xpath('//*[@id="PriceProduct"]/text()[not(parent::span[@class="SignoPriceProduct"])and normalize-space()]').extract()
		ml_item['link'] = response.xpath('//*[@id="HeaderInfoMiddlePerfil_Box_2"]/a/@href').extract()
		ml_item['sku'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][1]/span[@class="txValueInfoGral"]/text()').extract()
		ml_item['plataforma'] = response.xpath('//*[@id="imagen_producto"]/div[@class="dvInfoGral"][2]/span[@class="txValueInfoGral"]/text()').extract()

		self.item_count += 1
		if self.item_count > 100:
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