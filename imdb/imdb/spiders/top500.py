# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class Top500Spider(scrapy.Spider):
    name = 'top500'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/search/title?groups=top_500&sort=user_rating&view=advanced']

    def parse(self, response):
        itens_number = response.css('.lister-current-last-item::text').extract_first()
        next_page = response.css('.lister-page-next::attr(href)').extract_first()
        for selector in response.css('.lister-item'):
            yield {
                'title' : selector.css('.lister-item-header > a::text').extract_first(),
                'genre' : selector.css('.genre::text').extract_first(),
                'rating' : selector.css('.ratings-imdb-rating > strong::text').extract_first()
            }
        if int(itens_number) < 500:
            next_url = response.urljoin(next_page)
            request = Request(url=next_url, callback=self.parse)
            yield request