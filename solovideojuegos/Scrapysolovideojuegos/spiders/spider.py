import sys
reload(sys)
sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from Scrapysolovideojuegos.items import SVGItem


class SVGSpider(CrawlSpider):
	name = 'gamerspider'
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
		ml_item = SVGItem()
		#info de producto
		ml_item['titulo'] = response.xpath('//*[@id="ficha_producto_int"]/h1/text()').extract_first()
		ml_item['precio'] = response.xpath('//*[@id="PriceProduct"]/text()[not(parent::span[@class="SignoPriceProduct"])and normalize-space()]').extract()
		self.item_count += 1
		if self.item_count > 30:
			raise CloseSpider('item_exceeded')
		yield ml_item


