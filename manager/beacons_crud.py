# schemas database sqlalchemy
from manager.schemas.beacons_location import BeaconsLocation

# session sqlalchemy
from manager.utils.db_session import session

# models beacons fastapi
from manager.models.beacon_location import BeaconLocation

import uuid
from typing import List
from datetime import datetime
from sqlalchemy import and_

def add_beacon(beacon_location: BeaconLocation):
    uuid_ = str(uuid.uuid4())
    update_beacon(beacon_location.id)
    beacons_values = BeaconsLocation(uuid = uuid_,**beacon_location.dict())
    session.add(beacons_values)
    session.commit()
    return {'beacon_uuid': uuid_}

def update_beacon(beacon_id: str):
    session.query(BeaconsLocation).filter(BeaconsLocation.id == beacon_id, BeaconsLocation.active == True).update({BeaconsLocation.until: datetime.now(), BeaconsLocation.active: False}, synchronize_session = False)
    session.commit()

def get_beacons(beacon_id: str):
    return session.query(BeaconsLocation).filter(BeaconsLocation.id == beacon_id).all()

def get_beacons_with_filters(values: dict):
    return session.query(BeaconsLocation).filter(and_(getattr(BeaconsLocation,item) == value for item, value in values.items())).all()
