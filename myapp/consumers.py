from channels.generic.websocket import WebsocketConsumer
from random import randint
from time import sleep
import json
from channels.generic.websocket import WebsocketConsumer
from .models import BusinessDomains, NewBusinessDomains
from .models import NewCampaign as Campaign
from scrapy.crawler import CrawlerProcess
from django.shortcuts import get_object_or_404
#from scrapy.utils.project import settings
from scrapy.settings import Settings
from PrinceScraping.PrinceScraping.spiders.get_businesses import GetBusinessWebsites
from PrinceScraping.PrinceScraping import settings as my_settings
import inspect



class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
  

    def receive(self, text_data):

        #print(text_data)
        #print(type(text_data))

        #print(numofBusiness)

        text_data = json.loads(text_data)

        campaign = text_data["message"]
        N = text_data["numOfBusinesses"]

        campaign = get_object_or_404(Campaign, name = campaign)

        print("Campaign ID: \n")
        print(campaign.id)

        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)

        process = CrawlerProcess(settings=crawler_settings)
        process.crawl(GetBusinessWebsites, campaign_id = campaign.id, N = int(N))

        #f = open("/Users/prithviseran/Documents/AIDigitalMarketingApp/scrapy-done.txt", "w")
        #f.write("false")
        #f.close()

        f = open("/Users/prithviseran/Documents/AIDigitalMarketingApp/scrapy-done.txt", "r")
        status = f.read()

        while(status == "false"):
            f = open("/Users/prithviseran/Documents/AIDigitalMarketingApp/scrapy-done.txt", "r")
            status = f.read()

        f = open("/Users/prithviseran/Documents/AIDigitalMarketingApp/scrapy-done.txt", "w")
        f.write("false")
        f.close()
        
        new_domains = BusinessDomains.objects.filter(campaign_id=campaign.id)

        visited_domains = []

        for business in new_domains:
            visited_domains.append(business.name)

        self.send(text_data = json.dumps({
            'message': visited_domains
        }))

 