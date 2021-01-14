# schemas database sqlalchemy
from manager.schemas.beacons import Beacons

# session sqlalchemy
from manager.utils.db_session import session
from manager.utils.db_session import conn

# models beacons fastapi
from manager.models.beacon import Beacon

# dialects and expressions sqlalchemy
from sqlalchemy.dialects.postgresql import insert

import uuid
from typing import List

def add_session(coll_beacons : List[Beacon]):
    uuid_ = uuid.uuid4()
    beacons_values = [Beacons( uuid = str(uuid_), **beacon.dict() ) for beacon in coll_beacons]
    session.add_all(beacons_values)
    session.commit()
    return {'session_uuid':str(uuid_)}

def update_session(uuid_:uuid, coll_beacons: List[Beacon]):
    beacons_values = [dict(beacon, uuid=str(uuid_)) for beacon in coll_beacons]
    stmt = insert(Beacons).values(beacons_values)
    stmt = stmt.on_conflict_do_update(
        index_elements = [Beacons.uuid,Beacons.id],
        set_ = dict(rssi = stmt.excluded.rssi, until = stmt.excluded.until)
    )
    conn.execute(stmt)
    return beacons_values

def get_session(session_uuid: uuid):
    return session.query(Beacons).filter(Beacons.uuid == session_uuid).all()