import ast
import uuid
import json
from manager.schemas.beacons import Beacons
from manager.utils.db_session import session

def add_session(coll_beacons):
    uuid_ = uuid.uuid4()
    val = [tuple(ast.literal_eval(beacon.json()).values() )for beacon in coll_beacons]
    values = [(str(uuid_),) + val[i] for i in range(len(val))]
    beacons_values = [Beacons(uuid=val[0],id=val[2],from_=val[1],until=val[4],rssi=val[3]) for val in values]
    session.add_all(beacons_values)
    session.commit()
    
    return {'session_uuid':str(uuid_)}



	