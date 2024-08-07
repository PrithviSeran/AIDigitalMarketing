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

    def store_db(self, item):
        #self.curr.execute(""" INSERT INTO myapp_businessdomains
                             # VALUES ('please', 2);""")
        #self.conn.commit()
        pass
