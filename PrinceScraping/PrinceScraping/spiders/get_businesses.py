from typing import Iterable
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from selenium import webdriver
import sys
sys.path.append("/Users/prithviseran/Documents/AIDigitalMarketingApp")
import django
from myapp.models import BusinessDomains, NewBusinessDomains
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
    new_domains = []

    rules = (
        Rule(LinkExtractor(allow=""), callback="parse"),
    )

    def __init__(self, campaign = None, N = 2, *args, **kwargs):
        super(GetBusinessWebsites, self).__init__(*args, **kwargs)

        domains_for_campaign = BusinessDomains.objects.filter(campaign=campaign)

        self.visited_domains = set()

        for business in domains_for_campaign:
                self.visited_domains.add(business.name)

        self.campaign = campaign
        self.N = N
        dispatcher.connect(self.spider_opened, signal=signals.spider_opened)
        dispatcher.connect(self.spider_closed, signal=signals.spider_closed)
        dispatcher.connect(self.response_received, signal=signals.response_received)

    def spider_opened(self, spider):
        #self.visited_domains = set()
        #self.log("Spider opened: %s" % spider.name)
        pass

    def spider_closed(self, spider):
        #self.log("Spider closed: %s" % spider.name)
        #self.log("Total unique domains visited: %d" % len(self.visited_domains))
        pass

    def response_received(self, response, request, spider):
        pass

    def save_domain(self, domain):

        my_model_instance = BusinessDomains(
             campaign = 1,
             name = "Please Work"
        )

        my_model_instance.save()


    def save_new_domain(self, domain):
        NewBusinessDomains.objects.filter(campaign=self.campaign).update_or_create(
               campaign = self.campaign,
               name=domain
        )


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

        print(self.count)
        print(int(self.N))
        print("\n")

        if int(self.count) >= int(self.N):
               print("Exception Called")
               raise CloseSpider("Max Count Reached")
        
        domain = urlparse(response.url).netloc

        if domain not in list(self.visited_domains):

                print("Actual Domain")
                print(domain)

                print("List of Domains")
                print(list(self.visited_domains))
        
                self.count = int(self.count) + 1
                self.save_domain(domain)
                self.visited_domains.add(domain)
                self.new_domains.append(domain)
                #self.save_new_domain(domain)# findahealthcenter.hrsa.gov

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
                
                # Optionally, save the text to a file
                with open(completeName + '.txt', 'a') as f:
                        for text in all_text:
                                f.write(text.strip())
        