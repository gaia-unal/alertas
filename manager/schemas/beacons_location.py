from sqlalchemy import Column, Integer, DateTime, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

class BeaconsLocation(Base):
    __tablename__ = 'beacons_location'

    uuid = Column(UUID(as_uuid=True),primary_key=True)
    id = Column(String, primary_key=True)
    from_ = Column(DateTime)
    until = Column(DateTime)
    location = Column(String)
    status = Column(Boolean)
