# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from imdb.items import ImdbItem
from scrapy.loader import ItemLoader

class Top500Spider(scrapy.Spider):
    name = 'top500'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/search/title?groups=top_500&sort=user_rating&view=advanced']

    def parse(self, response):
        itens_number = response.css('.lister-current-last-item::text').extract_first()
        next_page = response.css('.lister-page-next::attr(href)').extract_first()
        for selector in response.css('.lister-item'):
            item = ItemLoader(item=ImdbItem(), selector=selector)
            item.add_value('position', selector.css('.lister-item-index::text').extract_first())
            item.add_value('name', selector.css('.lister-item-header > a::text').extract_first())
            item.add_value('genre', selector.css('.genre::text').extract_first())
            item.add_value('rating', selector.css('.ratings-imdb-rating > strong::text').extract_first())
            yield item.load_item()
        if int(itens_number) < 500:
            next_url = response.urljoin(next_page)
            request = Request(url=next_url, callback=self.parse)
            yield request