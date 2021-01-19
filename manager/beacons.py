# model database sqlalchemy
from manager.models.beacons_locations import BeaconsLocationH

# session sqlalchemy
from manager.utils.db_session import session

# shema beacons fastapi
from manager.schemas.beacons_locations import BeaconsLocation

import uuid
from typing import List
from datetime import datetime
from sqlalchemy import and_

def add_one(beacons_location: BeaconsLocation):
    uuid_ = str(uuid.uuid4())
    deactivate_one(beacons_location.id)
    beacons_values = BeaconsLocationH(uuid = uuid_,**beacons_location.dict())
    session.add(beacons_values)
    session.commit()
    return {'beacon_uuid': uuid_}

def deactivate_one(beacon_id: str):
    session.query(BeaconsLocationH).\
    filter(BeaconsLocationH.id == beacon_id, BeaconsLocationH.active == True).\
    update({BeaconsLocationH.until: datetime.now(), BeaconsLocationH.active: False}, synchronize_session = False)
    session.commit()

def get_many(values: dict):
    return session.query(BeaconsLocationH).\
    filter(and_(getattr(BeaconsLocationH,item) == value for item, value in values.items())).all()

#clases 