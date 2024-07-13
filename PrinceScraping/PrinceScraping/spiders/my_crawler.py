# my_crawler.py
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor, defer
from get_businesses import GetBusinessWebsites
from scrapy import signals

class CrawlerRunnerWithReturn(CrawlerRunner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.items = []

    @defer.inlineCallbacks
    def crawl(self, *args, **kwargs):
        spider = self.create_crawler(*args, **kwargs)
        spider.signals.connect(self.item_scraped, signals.item_scraped)
        yield super().crawl(spider)

    def item_scraped(self, item, response, spider):
        self.items.append(item)
