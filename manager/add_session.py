import uuid
from typing import List
from manager.schemas.beacons import Beacons
from manager.models.beacon import Beacon
from manager.utils.db_session import session

def add_session(coll_beacons : List[Beacon]):
    uuid_ = uuid.uuid4()
    beacons_values = [Beacons( uuid = str(uuid_), **beacon.dict() ) for beacon in coll_beacons]
    session.add_all(beacons_values)
    session.commit()
    
    return {'session_uuid':str(uuid_)}



	