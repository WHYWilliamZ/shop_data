# -*- coding: utf-8 -*-
import scrapy
from first_spider.items import FirstSpiderItem

class ShopspiderSpider(scrapy.Spider):
    name = 'ShopSpider'
    allowed_domains = ['dianping.com']
    url = 'http://www.dianping.com/beijing/ch45/g147'
    start_urls = [url]

    def parse(self, response):
        for each in response.xpath("//*[@id='shop-all-list']/ul/li"):
            item = FirstSpiderItem()
            item['shop_name'] = each.xpath("./div[2]/div[1]/a[1]/h4/text()").extract()[0]
            item['shop_addr'] = each.xpath("./div[2]/div[3]/span/text()").extract()[0]
            item['shop_star'] = each.xpath("./div[2]/div[2]/span/@title").extract()[0]
            item['comment_count'] = each.xpath("./div[2]/div[2]/a[1]/b/text()").extract()[0]
            item['aver_price'] = each.xpath("./div[2]/div[2]/a[2]/b/text()").extract_first()


            yield item



