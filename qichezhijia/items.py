# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QichezhijiaItem(scrapy.Item):
    category_one = scrapy.Field()
    category_two = scrapy.Field()
    category_three = scrapy.Field()
    category_four = scrapy.Field()

    image_urls = scrapy.Field()
    images = scrapy.Field()
