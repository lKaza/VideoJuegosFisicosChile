# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SVGItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()

	#info de producto
	titulo = scrapy.Field()
	precio = scrapy.Field()
	link = scrapy.Field()
	sku = scrapy.Field()
	plataforma = scrapy.Field()
	#telefono = scrapy.Field()
	#email = scrapy.Field()
	#clas = scrapy.Field()
	#sitioweb = scrapy.Field()
	#maps = scrapy.Field()

