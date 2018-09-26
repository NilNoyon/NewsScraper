from sqlalchemy import create_engine,Column,Integer,String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
import sys
import newsinfo.settings
from datetime import datetime,date

DeclarativeBase = declarative_base()

def db_connect():
    return create_engine(URL(**newsinfo.settings.DATABASE))

def create_headlines_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class HeadlineItem(DeclarativeBase):
    __tablename__ = "headlines"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    headline=Column('headline',String(500))
    href=Column('href',String(255))
    image_url =Column('image_url',String(255),nullable=True)
    posting_date =Column('posting_date',String(255),nullable=True)
    full_news = Column('full_news',String(10000),nullable=True)
