from typing import Iterable
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from selenium import webdriver
import sys
sys.path.append("/Users/prithviseran/Documents/AIDigitalMarketingApp")
import django
#from myapp.models import BusinessDomains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.exceptions import CloseSpider
import time
from scrapy import signals
from scrapy.signalmanager import dispatcher
from urllib.parse import urlparse
import os

class GetBusinessWebsites(CrawlSpider):
    name = "princecrawler"
    count = 0
    N = 0
    domain_count = 0

    rules = (
        Rule(LinkExtractor(allow=""), callback="parse"),
    )

    def __init__(self, campaign = None, count = 2, *args, **kwargs):
        super(GetBusinessWebsites, self).__init__(*args, **kwargs)
        self.visited_domains = set()
        self.campaign = campaign
        self.N = count
        dispatcher.connect(self.spider_opened, signal=signals.spider_opened)
        dispatcher.connect(self.spider_closed, signal=signals.spider_closed)
        dispatcher.connect(self.response_received, signal=signals.response_received)

    def spider_opened(self, spider):
        self.visited_domains = set()
        #self.log("Spider opened: %s" % spider.name)

    def spider_closed(self, spider):
        #self.log("Spider closed: %s" % spider.name)
        #self.log("Total unique domains visited: %d" % len(self.visited_domains))
        pass

    def response_received(self, response, request, spider):

        print("\n\n\n\n\n\nOVER HERRREEEE")
        print(self.N)
        print(" \n\n\n\n\n\n\n")

        if int(self.count) >= int(self.N):
               while(1):
                      print(self.visited_domains)
               raise CloseSpider("Max Count Reached")

        self.count = self.count + 1
        domain = urlparse(response.url).netloc
        self.visited_domains.add(domain)
        #self.log(f"Visited domain: {domain}")
        self.save_domain(domain)

    def save_domain(self, domain):
        #from myapp.models import BusinessDomains  # Import your model here
        pass
    
        #if domain not in self.visited_domains:
        #        BusinessDomains.objects.create(
        #        campaign=self.campaign,
        #        name=domain
        #        )


        # return domain name and send to websocket

    def start_requests(self) -> Iterable[Request]:
        
        driver = webdriver.Chrome()
        
        driver.get("https://www.google.com")

        #WebDriverWait(driver, 5).until(
        #    EC.presence_of_all_elements_located((By.NAME, "gLFyf"))
        #)

        input_element = driver.find_element(By.NAME, "q")
        input_element.send_keys("testing" + Keys.ENTER)

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "COVID"))
        )

        links = driver.find_elements(By.PARTIAL_LINK_TEXT, "COVID")

        time.sleep(5)
        # for link in links:
        #    print(link.get_attribute('href'))

        requests = []
        
        
        for link in links:
            #print("\n\n\n\n\n\nOVER HERRREEEE " + link.get_attribute('href') + "\n\n\n\n\n\n\n")
            #print(link.get_attribute('href'))
            requests.append(Request(link.get_attribute('href')))

        self.domain_count = self.domain_count + 1
        
        driver.quit()

        return requests #requests #super().start_requests()
    
    def parse(self, response):
        # Alternatively, you can use XPath
        para_texts = response.xpath('*//p/text()').getall()

        div_texts = response.xpath('*//div/text()').getall()

        a_texts = response.xpath('*//a/text()').getall()

        span_texts = response.xpath('*//span/text()').getall()

        h1_texts = response.xpath('*//h1/text()').getall()

        h2_texts = response.xpath('*//h2/text()').getall()

        h3_texts = response.xpath('*//h3/text()').getall()

        h4_texts = response.xpath('*//h4/text()').getall()

        h5_texts = response.xpath('*//h5/text()').getall()

        h6_texts = response.xpath('*//h6/text()').getall()

        li_texts = response.xpath('*//li/text()').getall()

        strong_texts = response.xpath('*//strong/text()').getall()

        em_texts = response.xpath('*//em/text()').getall()

        blockquote_texts = response.xpath('*//blockquote/text()').getall()

        td_texts = response.xpath('*//td/text()').getall()

        dt_texts = response.xpath('*//dt/text()').getall()

        caption_texts = response.xpath('*//caption/text()').getall()

        all_text = []

        # Print the extracted text for demonstration
        for text in div_texts:
            
                all_text.append(text.strip().replace('\n', ''))

        for text in para_texts:
            
                all_text.append(text.strip().replace('\n', ''))

        for text in a_texts:
            
                all_text.append(text.strip().replace('\n', ''))

        for text in span_texts:
            
                all_text.append(text.strip().replace('\n', ''))

        for text in h1_texts:
            
                all_text.append(text.strip().replace('\n', ''))

        for text in h2_texts:
            
                all_text.append(text.strip().replace('\n', ''))

        for text in h3_texts:
                all_text.append(text.strip().replace('\n', ''))

        for text in h4_texts:
            
                all_text.append(text.strip().replace('\n', ''))

        for text in h5_texts:
            
                all_text.append(text.strip().replace('\n', ''))

        for text in h6_texts:
            
                all_text.append(text.strip().replace('\n', ''))

        for text in li_texts:
            
                all_text.append(text.strip().replace('\n', ''))

        for text in strong_texts:
            
                all_text.append(text.strip().replace('\n', ''))

        for text in em_texts:
            
                all_text.append(text.strip().replace('\n', ''))

        for text in blockquote_texts:
            
                all_text.append(text.strip().replace('\n', ''))

        for text in td_texts:
            
                all_text.append(text.strip().replace('\n', ''))

        for text in dt_texts:
            
                all_text.append(text.strip().replace('\n', ''))

        for text in caption_texts:
            
                all_text.append(text.strip().replace('\n', ''))

        domain = urlparse(response.url).netloc

        #print("\n\n\n\n\n\nOVER HERRREEEE " + str(domain) + "\n\n\n\n\n\n\n")

        dir_path = "/Users/prithviseran/Documents/AIDigitalMarketingApp/ScrapedWebsites"

        completeName = os.path.join(dir_path, domain + ".txt")

        #print(completeName)
        #print(self.visited_domains)
        #if domain not in self.visited_domains:
        #campaign = BusinessDomains.objects.create()
        #data_set = {'tag1', 'tag2', 'tag3'}
        #campaign.campaign = self.campaign
        #campaign.name = domain

        """
        # Optionally, save the text to a file
        with open(completeName + '.txt', 'a') as f:
            for text in all_text:
                f.write(text.strip())
        """