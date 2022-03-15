from datetime import datetime
from sqlite3 import Date
from sqlalchemy import(create_engine, MetaData,
                       Table, Column, Boolean, Integer, String, DateTime)
from utils import EnvData

print(EnvData.get_env("DB_URI"))
engine = create_engine(EnvData.get_env("DB_URI"))  
meta_data = MetaData(bind=engine)
current_date = datetime.now

available_links = Table('available_links', meta_data,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(250)),
                    Column('link', String(250)),
                    Column('is_downloaded', Boolean, default=False),
                    Column('retries', Integer, default=0),
                    Column('created_at', DateTime, default=current_date),
                    Column('updated_at', DateTime, onupdate=datetime.now)
                    )

meta_data.create_all(checkfirst=True)
