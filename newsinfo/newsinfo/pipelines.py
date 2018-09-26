# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
import sys
from newsinfo.models import HeadlineItem,db_connect,create_headlines_table
from newsinfo import items

class NewsinfoPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_headlines_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        headline = HeadlineItem(**item)

        try:
            session.add(headline)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
