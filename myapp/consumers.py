from channels.generic.websocket import WebsocketConsumer
from random import randint
from time import sleep
import json
from channels.generic.websocket import WebsocketConsumer
from .models import Campaign, BusinessDomains, NewBusinessDomains
from scrapy.crawler import CrawlerProcess
from django.shortcuts import get_object_or_404
from scrapy.utils.project import get_project_settings
from PrinceScraping.PrinceScraping.spiders.get_businesses import GetBusinessWebsites




class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
  

        #for i in range(1000):
        #    self.send(json.dumps({'message': randint(1, 100)}))
        #    sleep(1)

    def receive(self, text_data):

        campaign = get_object_or_404(Campaign, pk=1)

        process = CrawlerProcess(get_project_settings())
        process.crawl(GetBusinessWebsites, campaign = campaign, N = 1)
        #process.start()
        
        new_domains = BusinessDomains.objects.filter(campaign=campaign)
        #print(stored_data_set)

        visited_domains = []

        for business in new_domains:
            visited_domains.append(business.name)


        print("DOMAINS: \n")
        print(visited_domains)

        # Send a response back to the client
        self.send(text_data=json.dumps({
            'message': visited_domains
        }))

 