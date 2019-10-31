# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 小区名
    community_name = scrapy.Field()
    # 几室
    shi_num = scrapy.Field()
    # 几厅
    ting_num = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 朝向
    direction = scrapy.Field()
    # 装修
    decoration = scrapy.Field()
    # 成交日期
    deal_date = scrapy.Field()
    # 总价
    total_price = scrapy.Field()
    # 单价
    unit_price = scrapy.Field()
    # 楼层
    layer = scrapy.Field()



