import uuid
from manager.schemas.beacons import Beacons
from manager.models.beacon import Beacon
from manager.utils.db_session import session

def get_session(session_uuid: uuid):
    return session.query(Beacons).filter(Beacons.uuid == session_uuid).all()