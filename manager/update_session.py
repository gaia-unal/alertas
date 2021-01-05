from manager.schemas.beacons import Beacons
from sqlalchemy.dialects.postgresql import insert
from manager.utils.db_session import session, conn
from manager.get_session import get_session

def update_session(uuid_, beacons):
    columns = beacons[0].keys()
    values = [[uuid_, *[value for value in beacon.values()]]  for beacon in beacons]
    beacons_values = [{'uuid':val[0],'id':val[2],'from_':val[1],'until':val[4], 'rssi':val[3]} for val in values]
    stmt = insert(Beacons).values(beacons_values)
    stmt = stmt.on_conflict_do_update(
        index_elements = [Beacons.uuid,Beacons.id],
        set_ = dict(rssi = stmt.excluded.rssi, until = stmt.excluded.until)
    )
    conn.execute(stmt)
    
    up_ss = get_session(uuid_)
    up_ss.append({"uuid": str(uuid_)})
    
    return up_ss