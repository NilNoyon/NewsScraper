# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
from newsinfo import models
from newsinfo.items import HeadlineItem



class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['www.bbc.com/news']
    start_urls = ['https://www.bbc.com/news']


    def parse(self, response):
        headlines = response.css('div.gs-c-promo-body')

        for headline in headlines:
            text = headline.css('a.gs-c-promo-heading h3.gs-c-promo-heading__title::text').extract_first()
            href = headline.css('a.gs-c-promo-heading::attr(href)').extract_first()
            posting_date = headline.css('ul.gs-o-list-inline li.nw-c-promo-meta span.gs-c-timestamp time::attr(datetime)').extract()


            if href is not None:
                href =response.urljoin(href)
                headline_data = HeadlineItem()
                headline_data['headline']=''.join(text)
                headline_data['href']=''.join(href)
                headline_data['posting_date']=''.join(posting_date)
                yield headline_data
                # print(text,href,posting_date)
                yield scrapy.Request(href,callback=self.parse)

# class SportSpider(object):
#     name = "sportsnews"
#     start_urls = [""]
