from datetime import datetime
from sqlite3 import Date
from xmlrpc.client import Boolean
from sqlalchemy import(create_engine, MetaData,
                       Table, Column, Integer, String, DateTime)

engine = create_engine('jdbc:postgresql://postgres:5432/receita-cnpj')
# engine = create_engine(
    # 'jdbc:postgresql://receita-cnpj:receita1234postgres:5432/receita-cnpj')

meta_data = MetaData(bind=engine)
current_date = datetime.now

available_links = Table('available_links', meta_data,
                        Column('id', Integer, primary_key=True),
                        Column('name', String(250)),
                        Column('link', String(250)),
                        Column('is_downloadded', Boolean),
                        Column('retries', Integer),
                        Column('created_at', DateTime, default=current_date),
                        Column('updated_at', DateTime, default=current_date,
                               onupdate=datetime.now)
                        )


