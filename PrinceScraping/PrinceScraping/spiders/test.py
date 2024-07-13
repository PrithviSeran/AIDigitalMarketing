# run_spider.py
from twisted.internet import reactor
from my_crawler import CrawlerRunnerWithReturn
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor, defer
from get_businesses import GetBusinessWebsites
from scrapy import signals

configure_logging()

@defer.inlineCallbacks
def crawl():
    runner = CrawlerRunnerWithReturn(get_project_settings())
    yield runner.crawl(GetBusinessWebsites)
    reactor.stop()
    return runner.items

def run_spider():
    items = []
    d = crawl()
    d.addCallback(lambda x: items.extend(x))
    reactor.run()
    return items

if __name__ == '__main__':
    scraped_items = run_spider()
    print(scraped_items)
