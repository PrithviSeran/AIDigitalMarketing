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
import scrapy
from urllib.parse import urlparse
import psycopg2
from PrinceScraping.PrinceScraping.llama3 import llama_wrapper, CLEAN_UP_RESPONSE, check_if_content_is_relavent, TEST_TEXT


class GetBusinessWebsites(CrawlSpider):
    name = "princecrawler"

    campaign_id = 0
    scraped_pages = 0
    count = 0
    response = None
    target_audience = None
    purpose = None
    user_info = None
    N = 0
    token_cap = 14000

    rules = (
        Rule(LinkExtractor(allow=""), callback="parse"),
    )

    def __init__(self, campaign_id, N = 1, target_audience = None, purpose = None, user_info = None, *args, **kwargs):
        super(GetBusinessWebsites, self).__init__(*args, **kwargs)

        self.campaign_id = campaign_id
        self.N = N
        self.target_audience = target_audience
        self.purpose = purpose
        self.user_info = user_info
        self.create_connection()


    def parse(self, response):
            
            body_text = ''.join(response.xpath("//body//text()").extract()).strip()

            if len(body_text) > 14000: body_text = body_text[:14000]
            
            content = llama_wrapper(CLEAN_UP_RESPONSE, body_text)

            print(body_text)

            business_domain = PrincescrapingItem()

            business_domain['campaign_id'] = self.campaign_id
            business_domain['name'] = response.xpath('//title/text()').get().replace("'", "''")
            business_domain['domain'] = self.get_domain(response)
            business_domain['url'] = response.url
            business_domain['target_audience'] = self.target_audience
            business_domain['purpose'] = self.purpose
            business_domain['user_info'] = self.user_info
            business_domain['content'] = content

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

        self.allowed_domains = []


        domains = self.select_domains()

        self.count = 0

        print("LINKS\n")
        print(links)
        print("LINK")
        
        for link in links:

            current_request = Request(link.get_attribute('href'))

            domain = self.get_domain(current_request)
            
            if domain not in domains and self.count < self.N:

                print("\nIs it even running???\n")
                self.count += 1

                self.allowed_domains = [domain]

                link_href = link.get_attribute('href')

                yield scrapy.Request(link_href, callback=self.parse)

        driver.quit()



    def handle_error(self, failure):
        self.logger.info("Skipping restricted page!")
        # Simply return None so the spider skips the forbidden page
        return None


    def get_domain(self, response):
        parsed_uri = urlparse(response.url)
        domain = '{uri.netloc}'.format(uri=parsed_uri)

        domain = domain.replace("''", "'")

        return domain
    

    def create_connection(self):
        self.conn = psycopg2.connect(
            host ="localhost",
            dbname ="AIDigMar",
            user="postgres",
            password="",
            port="5433")
        
        self.curr = self.conn.cursor()


    def select_domains(self):
        self.curr.execute(f"""SELECT domain FROM myapp_businessdomains WHERE campaign_id = {self.campaign_id};""")

        result = self.curr.fetchall()

        result = [x[0] for x in result] 

        return result

