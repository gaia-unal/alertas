import uuid
from manager.schemas.beacons import Beacons
from manager.utils.db_session import session

beacons_keys_list = ["from_","id","rssi","until"]

def get_session(session_uuid):
    beacons_session = session.query(Beacons).filter(Beacons.uuid == session_uuid)
    beacons = [[row.from_,row.id,row.rssi,row.until] for row in beacons_session]
    data = [ dict([(beacons_keys_list[0],row[0]),(beacons_keys_list[1],row[1]),(beacons_keys_list[2],row[2]),(beacons_keys_list[3],row[3])]) for row in beacons]
    return data