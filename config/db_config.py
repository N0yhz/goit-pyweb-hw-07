import os 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
load_dotenv()

POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')

DATABASE_URL = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine, future=True)
session = Session()