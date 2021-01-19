from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

class Beacons(Base):
    __tablename__ = 'beacons'

    uuid = Column(UUID(as_uuid=True),primary_key=True)
    id = Column(String, primary_key=True)
    from_ = Column(DateTime)
    until = Column(DateTime)
    rssi = Column(Integer)