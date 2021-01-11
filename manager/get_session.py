# schemas database sqlalchemy
from manager.schemas.beacons import Beacons
from manager.schemas.beacons_location import BeaconsLocation

# session sqlalchemy
from manager.utils.db_session import session

import uuid

def get_session(session_uuid: uuid):
    return session.query(Beacons).filter(Beacons.uuid == session_uuid).all()

def get_beacons(beacon_id: str):
    return session.query(BeaconsLocation).filter(BeaconsLocation.id == beacon_id).all()

def get_beacons_uuid(beacon_id: str,location: str):
    return session.query(BeaconsLocation).filter(BeaconsLocation.id == beacon_id, BeaconsLocation.location == location)