from manager.utils.connection_db import engine
from sqlalchemy.orm import sessionmaker

conn = engine.connect()

Session = sessionmaker(bind = engine)
session = Session()