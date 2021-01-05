from manager.schemas.beacons import Beacons
from manager.utils.db_session import session

def add_session(values):
    beacons_values = [Beacons(uuid=val[0],id=val[2],from_=val[1],until=val[4],rssi=val[3]) for val in values]
    session.add_all(beacons_values)
    session.commit()