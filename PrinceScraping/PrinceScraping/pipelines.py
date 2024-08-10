# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class PrincescrapingPipeline:
    def process_item(self, item, spider):
        return item
    
class SavingToPostgresPipeline(object):

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.conn = psycopg2.connect(
            host ="localhost",
            dbname ="AIDigMar",
            user="postgres",
            password="*PeterisVal6h7j",
            port="5433")
        
        self.curr = self.conn.cursor()

    def process_item(self, item, spider):
        print(item)
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

        self.curr.execute(f""" INSERT INTO myapp_businessdomains (name, campaign_id, url) VALUES ({name}, {campaign_id}, {url});""")
        self.conn.commit()

