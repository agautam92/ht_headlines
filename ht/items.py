# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from datetime import datetime

import scrapy


class HtItem(scrapy.Item):
    title = scrapy.Field()
    category = scrapy.Field()
    published_date = scrapy.Field()
    created_date = datetime.now()
