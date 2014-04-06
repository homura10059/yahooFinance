# coding: utf-8

from datetime import datetime

from scrapy import log
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from yahooFinance.items import FinanceItem


class FinanceSpider(CrawlSpider):
    name = 'finance'
    allowed_domains = ["finance.yahoo.com"]
    start_urls = [
        'http://finance.yahoo.com/q?s=V',
    ]
    rules = [
        Rule(SgmlLinkExtractor(allow=('\+Cash\+Flow\&annual', )), callback='parse_news'),
    ]

    def parse_news(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        item = FinanceItem()
        
        sel = Selector(response)
        item['title'] = sel.xpath('//title/text()').extract()
        item['body'] = sel.xpath('//table[@class="yfnc_tabledata1"]').extract()
        yield item

