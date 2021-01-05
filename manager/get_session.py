from manager.schemas.beacons import Beacons
from manager.utils.db_session import session

def get_session(session_uuid):
    beacons_session = session.query(Beacons).filter(Beacons.uuid == session_uuid)
    beacons = [[row.from_,row.id,row.rssi,row.until] for row in beacons_session]
    return beacons