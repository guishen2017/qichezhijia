# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qichezhijia.items import QichezhijiaItem


class QicheSpider(CrawlSpider):
    name = 'qiche'
    allowed_domains = ['autohome.com.cn']

    rules = (
        # //car.autohome.com.cn/pic/series/
        Rule(LinkExtractor(allow=r'//car.autohome.com.cn/pic/series/\d+.html'),follow=True),
        # /pic/series/4851-1.html
        Rule(LinkExtractor(allow=r'//car.autohome.com.cn/pic/series/.+'),callback="parse_item",follow=True),
    )

    def parse_item(self, response):
        # //ul[@class="rank-list-ul"]/li/div/a[@id]/@href
        imgs = response.xpath('//div[contains(@class,"uibox-con")]//li/a/img/@src').getall()
        images_url = list(map(lambda url: response.urljoin(url), imgs))
        category = response.xpath('//div[@class="breadnav"]/a/text()').getall()
        category_one = category[2]
        category_two = category[3]
        category_three = category[4]
        category_four = response.xpath('//div[@class="uibox-title"]/text()').getall()[-1]
        item = QichezhijiaItem(category_one=category_one,category_two=category_two,category_three=category_three,category_four = category_four,image_urls = images_url)
        yield item

    def start_requests(self):
        alphabet = [chr(i) for i in range(65,91)]
        for letter in alphabet:
            url = "https://www.autohome.com.cn/grade/carhtml/{}.html".format(letter)
            yield self.make_requests_from_url(url)

