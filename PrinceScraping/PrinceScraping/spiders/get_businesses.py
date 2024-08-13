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
import nltk

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
        print("TARGET AUDIENCE: ")
        print(self.target_audience)
        self.create_connection()

    def parse(self, response):

        business_domain = PrincescrapingItem()

        business_domain['campaign_id'] = self.campaign_id
        business_domain['name'] = response.xpath('//title/text()').get().replace("'", "''")
        business_domain['domain'] = self.get_domain(response)
        business_domain['url'] = response.url

        self.response = response

        yield business_domain


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
        
        for link in links:
            requests.append(Request(link.get_attribute('href')))
        
        driver.quit()

        return requests

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