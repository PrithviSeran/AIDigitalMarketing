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
from scrapy.exceptions import CloseSpider

class GetBusinessWebsites(CrawlSpider):
    name = "princecrawler"
    start_urls = ['https://www.chocolate.co.uk']
    campaign_id = 0
    scraped_pages = 0

    rules = (
        Rule(LinkExtractor(allow=""), callback="parse"),
    )

    def __init__(self, campaign_id, N = 1, *args, **kwargs):
        super(GetBusinessWebsites, self).__init__(*args, **kwargs)

        self.campaign_id = campaign_id
        self.N = N

    def parse(self, response):

        business_domain = PrincescrapingItem()

        business_domain['campaign_id'] = self.campaign_id
        business_domain['name'] = response.xpath('//title/text()').get().replace("'", "''")
        business_domain['url'] = response.url

        yield business_domain

       #next_page = response.css('[rel="next"] x:attr(href)').get()

       #if next_page is not None:
       #    next_page_url = 'https://www.chocolate.co.uk' + next_page
       #    yield response.follow(next_page_url, callback=self.parse)


    """
    def start_requests(self) -> Iterable[Request]:
        
        driver = webdriver.Chrome()
        
        driver.get("https://www.google.com")

        input_element = driver.find_element(By.NAME, "q")
        input_element.send_keys("testing" + Keys.ENTER)

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "COVID"))
        )

        links = driver.find_elements(By.PARTIAL_LINK_TEXT, "COVID")

        time.sleep(5)

        requests = []
        
        for link in links:
            requests.append(Request(link.get_attribute('href')))

        self.domain_count = self.domain_count + 1
        
        driver.quit()

        return requests 
    """
        
    """
    def parse(self, response):
        # Extract data from the response
        business_domain = PrincescrapingItem()

        business_domain['title'] = response.xpath('//title/text()').get()
        business_domain['url'] = response.url

        yield business_domain
        """




"""
    def parse(self, response):

        print(self.count)
        print(int(self.N))
        print("\n")

        if int(self.count) >= int(self.N):
                print("Exception Called")
                my_model_instance = BusinessDomains(
                        campaign = self.campaign,
                        name = "Please Again Please Work"
                )
                my_model_instance.save()
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
"""