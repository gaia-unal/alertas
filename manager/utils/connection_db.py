import psycopg2
from sqlalchemy import create_engine
from utils import settings 

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user= settings.DATABASE_USERNAME,
    pw= settings.DATABASE_PASSWORD,
    url= settings.DATABASE_HOST,
    db= settings.DATABASE_NAME)

engine = create_engine(DB_URL)