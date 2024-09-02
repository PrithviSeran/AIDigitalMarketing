from typing import Iterable
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from selenium import webdriver
import sys
sys.path.append("/Users/prithviseran/Documents/AIDigitalMarketingApp")
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PrinceScraping.PrinceScraping.items import PrincescrapingItem
import os
from urllib.parse import urlparse
import psycopg2
from scrapy.pqueues import ScrapyPriorityQueue

class GetBusinessWebsites(CrawlSpider):
    name = "princecrawler"
    #start_urls = ['https://www.chocolate.co.uk']
    #allowed_domains = ['https://www.chocolate.co.uk']
    campaign_id = 0
    scraped_pages = 0
    count = 0
    response = None
    target_audience = None
    N = 0

    rules = (
        Rule(LinkExtractor(allow=""), callback="parse"),
    )

    def __init__(self, campaign_id, N = 1, target_audience = None, *args, **kwargs):
        super(GetBusinessWebsites, self).__init__(*args, **kwargs)

        self.campaign_id = campaign_id
        self.N = N
        self.target_audience = target_audience
        self.create_connection()

    def parse(self, response):

        business_domain = PrincescrapingItem()

        business_domain['campaign_id'] = self.campaign_id
        business_domain['name'] = response.xpath('//title/text()').get().replace("'", "''")
        business_domain['domain'] = self.get_domain(response)
        business_domain['url'] = response.url

        self.response = response

        return business_domain

    def start_requests(self) -> Iterable[Request]:
        
        driver = webdriver.Chrome()
        
        driver.get("https://www.google.com")

        input_element = driver.find_element(By.NAME, "q")
        input_element.send_keys(self.target_audience + Keys.ENTER)

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.g a"))
        )

        links = driver.find_elements(By.CSS_SELECTOR, "div.g a")

        time.sleep(5)

        requests = []
        self.allowed_domains = []

        domains = self.select_domains()
        
        for link in links:

            current_request = Request(link.get_attribute('href'))

            domain = self.get_domain(current_request)

            current_request_domain = Request("https://" + domain)

            refined_domain = domain.replace("''", "'")
            
            if refined_domain not in domains:
                requests.append(current_request_domain)
                self.allowed_domains.append(domain)
        
        driver.quit()

        self.allowed_domains = self.allowed_domains[:self.N]

        print("Requests\n\n")

        print(requests[:self.N])

        print("\n\nRequests")

        return requests[:self.N]

    def get_domain(self, response):
        parsed_uri = urlparse(response.url)
        domain = '{uri.netloc}'.format(uri=parsed_uri)

        return domain
    
    def create_connection(self):
        self.conn = psycopg2.connect(
            host ="localhost",
            dbname ="AIDigMar",
            user="postgres",
            password="*PeterisVal6h7j",
            port="5433")
        
        self.curr = self.conn.cursor()

    def select_domains(self):
        self.curr.execute(f"""SELECT domain FROM myapp_businessdomains WHERE campaign_id = {self.campaign_id};""")

        result = self.curr.fetchall()

        result = [x[0] for x in result] 

        return result