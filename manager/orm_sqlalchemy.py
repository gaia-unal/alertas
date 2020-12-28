from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID, insert
from sqlalchemy.orm import sessionmaker

from psycopg2.extras import DictCursor, execute_values
import psycopg2
from manager.utils import connection_settings as cs 

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user= cs.DATABASE_USERNAME,
    pw= cs.DATABASE_PASSWORD,
    url= cs.DATABASE_HOST,
    db= cs.DATABASE_NAME)

engine = create_engine(DB_URL)
conn = engine.connect()

Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base()

class Beacons(Base):
    __tablename__ = 'beacons'

    uuid = Column(UUID(as_uuid=True),primary_key=True)
    id = Column(String, primary_key=True)
    from_ = Column(DateTime)
    until = Column(DateTime)
    rssi = Column(Integer)


def add_session(values):
    beacons_values = [Beacons(uuid=val[0],id=val[2],from_=val[1],until=val[4],rssi=val[3]) for val in values]
    session.add_all(beacons_values)
    session.commit()
    
def get_session(session_uuid):
    beacons_session = session.query(Beacons).filter(Beacons.uuid ==  session_uuid)
    beacons = [[row.from_,row.id,row.rssi,row.until] for row in beacons_session]
    return beacons

def update_session(values):
    beacons_values = [{'uuid':val[0],'id':val[2],'from_':val[1],'until':val[4], 'rssi':val[3]} for val in values]
    stmt = insert(Beacons).values(beacons_values)
    stmt = stmt.on_conflict_do_update(
        index_elements = [Beacons.uuid,Beacons.id],
        set_ = dict(rssi = stmt.excluded.rssi, until = stmt.excluded.until)
    )
    conn.execute(stmt)

