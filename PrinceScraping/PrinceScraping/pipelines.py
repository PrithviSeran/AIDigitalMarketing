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
from PrinceScraping.PrinceScraping.llama3 import llama_wrapper, CLEAN_UP_RESPONSE, check_if_content_is_relavent
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
            password="",
            port="5433")
        
        self.curr = self.conn.cursor()

    def process_item(self, item, spider):

        relevance = self.check_relevancy(item)

        print("RELEVANCE\n")
        print(relevance)
        print(item.get("content").strip())
        print("RELEVANCE")

        if relevance == "True":

            self.store_db(item)
            return item
        
        else:

            return None
    
    def close_spider(self, item):
        f = open("/Users/prithviseran/Documents/AIDigitalMarketingApp/scrapy-done.txt", "w")
        f.write("true")
        f.close()

    def store_db(self, item):

        campaign_id = item.get("campaign_id")
        name = item.get("name")
        url = item.get("url")
        domain = item.get("domain")
        content = item.get("content")

        try:
            # Execute the SELECT query to check if the domain exists
            self.curr.execute(
                """SELECT EXISTS (
                    SELECT 1 
                    FROM myapp_businessdomains 
                    WHERE domain = %s AND campaign_id = %s
                );""",
                (domain, campaign_id)
            )
            
            # Fetch the result of the EXISTS query
            exists = self.curr.fetchone()[0]
            
            # If the domain does not exist, proceed with the INSERT query
            if not exists:

                self.curr.execute(
                    """INSERT INTO myapp_businessdomains 
                    (name, campaign_id, url, domain, content) 
                    VALUES (%s, %s, %s, %s, %s);""",
                    (name, campaign_id, url, domain, content)
                )
                
                # Commit the transaction after a successful insert
                self.conn.commit()

            else:
                self.curr.execute(
                    """UPDATE myapp_businessdomains
                    SET content = content ||  %s
                    WHERE domain = %s
                    AND campaign_id = %s;""",
                    (" " + content, domain, campaign_id)
                )

                # Commit the transaction after a successful insert
                self.conn.commit()


        except psycopg2.Error as e:
            # Rollback the transaction in case of any error
            self.conn.rollback()
            print(f"Error occurred: {e}")



    def check_relevancy(self, item):

        relevance = check_if_content_is_relavent(item.get("content"), item.get("user_info"), item.get("purpose"))

        return relevance
