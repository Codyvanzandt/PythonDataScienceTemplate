# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GradCafeSpiderItem(scrapy.Item):
    institution = scrapy.Field()
    program = scrapy.Field()
    decision = scrapy.Field()
    status = scrapy.Field()
    notes = scrapy.Field()
    gre = scrapy.Field()
    gpa = scrapy.Field()
