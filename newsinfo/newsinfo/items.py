# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class HeadlineItem(scrapy.Item):
    id = scrapy.Field()
    headline = scrapy.Field()
    href = scrapy.Field()
    posting_date = scrapy.Field()
