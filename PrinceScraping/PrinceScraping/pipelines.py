# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sys
sys.path.append("/Users/prithviseran/Documents/AIDigitalMarketingApp")
from itemadapter import ItemAdapter
from scrapy.exceptions import CloseSpider
import psycopg2
from urllib.parse import urlparse
from PrinceScraping.PrinceScraping.llama3 import llama_wrapper, CLEAN_UP_RESPONSE
import os
import re

    
class SavingToPostgresPipeline(object):

    def __init__(self):
        self.create_connection()
        self.N = 0
        self.count = 0

    def create_connection(self):
        self.conn = psycopg2.connect(
            host ="localhost",
            dbname ="AIDigMar",
            user="postgres",
            password="*PeterisVal6h7j",
            port="5433")
        
        self.curr = self.conn.cursor()

    def process_item(self, item, spider):

        if spider.N <= self.count:
            raise CloseSpider(reason='Max Number Reacher')

        self.curr.execute(f"""SELECT domain FROM myapp_businessdomains WHERE campaign_id = {spider.campaign_id};""")

        result = self.curr.fetchall()

        result = [x[0] for x in result] 

        undo_string = item.get("domain").replace("''", "'")
        # [(166,), (167,)]

        print("Undo String" + undo_string)
        print("Result")
        print(result)

        if undo_string not in result:
            self.count += 1
            self.get_content_of_page(spider.response, item.get("domain"))
            self.store_db(item)

        return item
    
    def close_spider(self, item):
        f = open("/Users/prithviseran/Documents/AIDigitalMarketingApp/scrapy-done.txt", "w")
        f.write("true")
        f.close()

    def store_db(self, item):

        campaign_id = item.get("campaign_id")
        name = item.get("name")
        url = item.get("url")
        domain = item.get("domain")

        self.curr.execute(f""" INSERT INTO myapp_businessdomains (name, campaign_id, url, domain) VALUES ('{name}', {campaign_id}, '{url}', '{domain}');""")
        self.conn.commit()

    def get_content_of_page(self, response, domain):

        body_text = ''.join(response.xpath("//body//text()").extract()).strip()

        body_text = llama_wrapper(CLEAN_UP_RESPONSE, body_text)

        dir_path = "/Users/prithviseran/Documents/AIDigitalMarketingApp/ScrapedWebsites"

        completeName = os.path.join(dir_path, domain + ".txt")
                
        # Optionally, save the text to a file
        with open(completeName, 'w') as f:
                f.write(body_text)

