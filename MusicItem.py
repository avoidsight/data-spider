import scrapy


class MusicItem(scrapy.item):
    name = scrapy.Field
    singer = scrapy.Field
    time = scrapy.Field
