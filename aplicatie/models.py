from django.db import models
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

hostname = "127.0.0.1"
username = "root"
password = ""
port = 3306
database = "lista_cumparaturi"

DATABASE_URL = f'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}'

engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Produs(Base):
    __tablename__ = "Produse"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nume = Column(String(200), nullable=False)
    cumparat = Column(Boolean, default=False, nullable=False)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

