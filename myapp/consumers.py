from channels.generic.websocket import WebsocketConsumer
from random import randint
from time import sleep
import json
from channels.generic.websocket import WebsocketConsumer
from .models import Campaign, BusinessDomains
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
        data = json.loads(text_data)
        message = data['message']

        print("You are a Genius!")

        campaign = get_object_or_404(Campaign, pk=1)

        process = CrawlerProcess(get_project_settings())
        process.crawl(GetBusinessWebsites, campaign = campaign, count = 1)
        #process.start()
        

        domains_for_campaign = BusinessDomains.objects.filter(campaign=campaign)
        #print(stored_data_set)

        visited_domains = set()

        for business in domains_for_campaign:
                visited_domains.add(business.name)

        print("DOMAINS: \n")
        print(visited_domains)

        # Send a response back to the client
        self.send(text_data=json.dumps({
            'message': list(visited_domains)
        }))

 