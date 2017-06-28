# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy import signals
from scrapy.exporters import CsvItemExporter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import csv

import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request

class SernaturPipeline(object):
	def __init__(self):
		self.conn = MySQLdb.connect('localhost', 'root', '', 'solovideojuegos', charset="utf8", use_unicode=True)
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):    
		try:
			self.cursor.execute("INSERT INTO solovideojuegos (titulo, precio) VALUES (%s, %s)", (item['titulo'], item['precio']) )

			self.conn.commit()


		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])


		return item
"""
Para exportar a un CSV
	def __init__(self):
		self.files = {}

	@classmethod
	def from_crawler(cls, crawler):
		pipeline = cls()
		crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
		crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
		return pipeline

	def spider_opened(self, spider):
		file = open('%s_items.csv' % spider.name, 'w+b')
		self.files[spider] = file
		self.exporter = CsvItemExporter(file)
		self.exporter.fields_to_export = ['titulo','direccion', 'telefono', 'email', 'clas', 'sitioweb', 'maps']
		self.exporter.start_exporting()

	def spider_closed(self, spider):
		self.exporter.finish_exporting()
		file = self.files.pop(spider)
		file.close()

	def process_item(self, item, spider):
		self.exporter.export_item(item)
		return item

class MercadoImagenesPipeline(ImagesPipeline):
	
	def get_media_requests(self, item, info):
		return [Request(x, meta={'image_name': item["image_name"]})
				for x in item.get('image_urls', [])]

	def file_path(self, request, response=None, info=None):
		return '%s.jpg' % request.meta['image_name']
"""