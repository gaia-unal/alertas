# schemas database sqlalchemy
from manager.schemas.beacons import Beacons
from manager.schemas.beacons_location import BeaconsLocation

# session sqlalchemy
from manager.utils.db_session import conn

# models beacons fastapi
from manager.models.beacon import Beacon

# dialects and expressions sqlalchemy
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.sql.expression import update

from typing import List
import uuid

def update_session(uuid_:uuid, coll_beacons: List[Beacon], location: str):
    beacons_values = [dict(beacon, uuid=str(uuid_)) for beacon in coll_beacons]
    update_beacons(uuid_,coll_beacons,location)
    stmt = insert(Beacons).values(beacons_values)
    stmt = stmt.on_conflict_do_update(
        index_elements = [Beacons.uuid,Beacons.id],
        set_ = dict(rssi = stmt.excluded.rssi, until = stmt.excluded.until)
    )
    conn.execute(stmt)
    
    return beacons_values

def update_beacons(uuid_: uuid, coll_beacons: List[Beacon], location: str):
    beacons_values = [dict(dict((k,beacon.dict()[k]) for k in ['from_','id','until']), uuid = str(uuid_), location = location, status = True) for beacon in coll_beacons]
    update_beacon_location([beacons['id'] for beacons in beacons_values])
    stmt = insert(BeaconsLocation).values(beacons_values)
    stmt = stmt.on_conflict_do_update(
        index_elements = [BeaconsLocation.uuid, BeaconsLocation.id],
        set_ = dict(until = stmt.excluded.until, status = stmt.excluded.status)
    )
    conn.execute(stmt)

def update_beacon_location(beacon_id: List[str]):
    for id in beacon_id:
        stmt = update(BeaconsLocation).where(BeaconsLocation.id == id and BeaconsLocation.status == True).values(status = False)
        conn.execute(stmt)
