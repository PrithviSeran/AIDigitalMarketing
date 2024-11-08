from channels.generic.websocket import WebsocketConsumer
from random import randint
from time import sleep
import json
from channels.generic.websocket import WebsocketConsumer
from .models import BusinessDomains, NewBusinessDomains
from .models import NewCampaign as Campaign
from scrapy.crawler import CrawlerProcess
from django.shortcuts import get_object_or_404
from scrapy.settings import Settings
from PrinceScraping.PrinceScraping.spiders.get_businesses import GetBusinessWebsites
from PrinceScraping.PrinceScraping import settings as my_settings
from myapp.serializer import *


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
  

    def receive(self, text_data):

        text_data = json.loads(text_data)

        campaign_id = text_data["message"]

        campaign = Campaign.objects.get(id = campaign_id)

        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)

        process = CrawlerProcess(settings=crawler_settings)
        process.crawl(GetBusinessWebsites,
                      campaign_id = campaign.id,
                      N = 5,
                      target_audience = campaign.target_audience,
                      purpose = campaign.purpose,
                      user_info = campaign.user_info)

        f = open("/Users/prithviseran/Documents/AIDigitalMarketingApp/scrapy-done.txt", "r")
        status = f.read()

        while(status == "false"):
            f = open("/Users/prithviseran/Documents/AIDigitalMarketingApp/scrapy-done.txt", "r")
            status = f.read()

        f = open("/Users/prithviseran/Documents/AIDigitalMarketingApp/scrapy-done.txt", "w")
        f.write("false")
        f.close()
        
        new_domains = BusinessDomains.objects.filter(campaign_id=campaign.id)

        new_domains_serializer = DomainsSerializer(new_domains, many=True)

        self.send(text_data = json.dumps({
            'message': new_domains_serializer.data
        }))

class CampaignWSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
  

    def receive(self, text_data):

        text_data = json.loads(text_data)

        user = self.scope["user"]

        campaigns = Campaign.objects.filter(user = user)

        serializer = NewCampaignSerializer(campaigns, many=True)

        self.send(text_data = json.dumps({
            'message': serializer.data
        }))

 