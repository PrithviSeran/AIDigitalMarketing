# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PrincescrapingItem(scrapy.Item):
    # define the fields for your item here like:
    campaign_id = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    domain = scrapy.Field()
    target_audience = scrapy.Field()
    purpose = scrapy.Field()
    user_info = scrapy.Field()
    content = scrapy.Field()

