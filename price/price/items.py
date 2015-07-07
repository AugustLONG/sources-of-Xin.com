# -*- coding: utf-8 -*-

from scrapy import Item, Field


class XinItem(Item):
    name = Field()
    city = Field()
    band = Field()
    price = Field()
    type_vehicle = Field()
    licensed_time = Field()
    mile = Field()
