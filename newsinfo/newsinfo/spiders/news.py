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
        headlines = response.css('div.gs-c-promo')

        for headline in headlines:
            text = headline.css('div.gs-c-promo-body a.gs-c-promo-heading h3.gs-c-promo-heading__title::text').extract_first()
            href = headline.css('div.gs-c-promo-body a.gs-c-promo-heading::attr(href)').extract_first()
            image_url = headline.css('div.gs-c-promo-image div.gs-o-media-island div.gs-o-responsive-image img::attr(src)').extract_first()
            posting_date = headline.css('div.gs-c-promo-body ul.gs-o-list-inline li.nw-c-promo-meta span.gs-c-timestamp time::attr(datetime)').extract()

            if href is not None:
                href =response.urljoin(href)
                item = HeadlineItem()
                item['headline']=''.join(text)
                item['href']=''.join(href)
                item['image_url']=image_url
                item['posting_date']=''.join(posting_date)
                request = scrapy.Request(url=href,callback=self.parse_href_data,dont_filter=True)
                request.meta['item'] = item
                yield request
    def parse_href_data(self,response):
        item = response.meta['item']
        item['full_news'] = ''.join(response.css('div.story-body div.story-body__inner p::text').extract())
        yield item
