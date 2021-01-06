from manager.schemas.beacons import Beacons
from manager.models.beacon import Beacon
from typing import List
import uuid
from sqlalchemy.dialects.postgresql import insert
from manager.utils.db_session import conn

def update_session(uuid_:uuid, coll_beacons: List[Beacon]):
    beacons_values = [dict(beacon, uuid=str(uuid_)) for beacon in coll_beacons]
    stmt = insert(Beacons).values(beacons_values)
    stmt = stmt.on_conflict_do_update(
        index_elements = [Beacons.uuid,Beacons.id],
        set_ = dict(rssi = stmt.excluded.rssi, until = stmt.excluded.until)
    )
    conn.execute(stmt)
    
    return beacons_values