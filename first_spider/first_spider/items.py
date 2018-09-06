# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 餐馆名
    shop_name = scrapy.Field()
    shop_addr=scrapy.Field()
    shop_star=scrapy.Field()
    comment_count = scrapy.Field()
    aver_price = scrapy.Field()
