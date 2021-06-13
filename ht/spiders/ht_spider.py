import scrapy

from ht.items import HtItem


class BlogSpider(scrapy.Spider):
    name = 'ht_news'
    start_urls = ['https://www.hindustantimes.com/latest-news']

    def parse(self, response):
        headlines = response.css('.storyShortDetail').css('h2 a::text').extract()
        type_of = response.css('.storyShortDetail').css('h2 a::attr(href)').extract()
        published_date = response.css('.storyShortDetail').css('.stroyPub').css('.dateTime::text').extract()
        for obj in zip(headlines, type_of, published_date):
            item = HtItem()
            item["title"] = obj[0]
            item["category"] = obj[1].split('/')[1]
            item["published_date"] = obj[2]
            yield item
