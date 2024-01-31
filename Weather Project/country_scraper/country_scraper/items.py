# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    flag = scrapy.Field()
    name = scrapy.Field()
    province = scrapy.Field()
    population = scrapy.Field()


class USAStateItem(scrapy.Item):
    name = scrapy.Field()
    short_name = scrapy.Field()
