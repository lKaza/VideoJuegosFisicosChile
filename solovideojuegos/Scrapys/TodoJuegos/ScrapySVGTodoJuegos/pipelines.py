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


class ScrapysvgtodojuegosPipeline(object):
	def __init__(self):
		self.conn = MySQLdb.connect('localhost', 'root', '', 'solovideojuegos', charset="utf8", use_unicode=True)
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):    
		try:
		
			self.cursor.execute("INSERT INTO solovideojuegos (titulo,precio,tienda,link,sku,plataforma) VALUES (%s,%s,%s,%s,%s,%s)" , (item['titulo'],item['precio'],'Todojuegos',item['link'],1,item['plataforma']) )

			self.conn.commit()


		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0],e.args[1])


		return item



