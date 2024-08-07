from channels.generic.websocket import WebsocketConsumer
from random import randint
from time import sleep
import json
from channels.generic.websocket import WebsocketConsumer
from scrapy.crawler import CrawlerProcess
from django.shortcuts import get_object_or_404
#from scrapy.utils.project import settings
from scrapy.settings import Settings
from spiders.get_businesses import GetBusinessWebsites
import settings as my_settings



crawler_settings = Settings()
crawler_settings.setmodule(my_settings)

process = CrawlerProcess(settings=crawler_settings)
process.crawl(GetBusinessWebsites)
process.start()

print("WHYYYYYYYYYYYYYYYYY")