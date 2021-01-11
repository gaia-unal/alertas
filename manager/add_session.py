# schemas database sqlalchemy
from manager.schemas.beacons import Beacons
from manager.schemas.beacons_location import BeaconsLocation

# session sqlalchemy
from manager.utils.db_session import session

# models beacons fastapi
from manager.models.beacon import Beacon

# update_session file
from manager import update_session 

import uuid
from typing import List

def add_session(coll_beacons : List[Beacon],location: str):
    uuid_ = uuid.uuid4()
    add_beacons(coll_beacons,location,uuid_)
    beacons_values = [Beacons( uuid = str(uuid_), **beacon.dict() ) for beacon in coll_beacons]
    session.add_all(beacons_values)
    session.commit()
    
    return {'session_uuid':str(uuid_)}

def add_beacons(coll_beacons: List[Beacon], location: str, uuid_: uuid):
    beacons_values = [BeaconsLocation(**dict((k,beacon.dict()[k]) for k in ['from_','id','until']), uuid = str(uuid_), location = location, status = True) for beacon in coll_beacons]
    update_session.update_beacon_location([beacons.id for beacons in beacons_values])
    session.add_all(beacons_values)
    session.commit()


	