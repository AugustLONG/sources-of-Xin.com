# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from price.items import *


class XinSpider(Spider):
    name = 'xmoz'
    allowed_domains = ["xin.com"]
    xin_page = 'http://www.xin.com/quanguo/s/o2a10i'
    start_urls = []
    for page_num in xrange(1, 20910):

        start_urls.append('http://www.xin.com/quanguo/s/o2a10i%dv1/' % page_num)

    def parse(self, response):
        xitems = []
        for car in response.xpath("//div[@class='car-vtc vtc-border ']"):
            xitem = XinItem()
            xitem['name'] = car.xpath(".//div[@class='vtc-info']/p/a/@title").extract()
            xitem['city'] = car.xpath(".//div[@class='box']/ul/li/text()").extract()[3]
            xitem['price'] = car.xpath("div[@class='vtc-money']/em/text()").extract()
            xitem['licensed_time'] = car.xpath(".//div[@class='box']/ul/li/text()").extract()[0]
            xitem['mile'] = car.xpath(".//div[@class='box']/ul/li/text()").extract()[1]
            xitems.append(xitem)
        return xitems
