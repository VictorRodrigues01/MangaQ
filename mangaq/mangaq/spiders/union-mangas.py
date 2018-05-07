
import scrapy
from mangaq.items import Manga


class UnionMangasSpider(scrapy.Spider):


	name = 'union-mangas'

	start_urls = [
		'http://unionmangas.cc/manga/shingeki-no-kyojin',
	]


	def parse_manga (self,response):
		pass
		