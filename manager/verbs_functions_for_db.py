import uuid
import ast
import json
from manager import orm_sqlalchemy

beacons_keys_list = ["from_","id","rssi","until"]

def insert(beacons):
	uuid_ = uuid.uuid4()
	val = [tuple(ast.literal_eval(beacon.json()).values() )for beacon in beacons]
	values = [(str(uuid_),) + val[i] for i in range(len(val))]
	orm_sqlalchemy.add_session(values)

	return {'session_uuid':str(uuid_)}

def find_one(session_uuid):
	response = orm_sqlalchemy.get_session(session_uuid)
	data = [ dict([(beacons_keys_list[0],row[0]),(beacons_keys_list[1],row[1]),(beacons_keys_list[2],row[2]),(beacons_keys_list[3],row[3])]) for row in response]

	return data

def update(uuid_, beacons):
	columns = beacons[0].keys()
	values = [[uuid_, *[value for value in beacon.values()]]  for beacon in beacons]
	orm_sqlalchemy.update_session(values)

	up_ss = find_one(uuid_)
	up_ss.append({"uuid": str(uuid_)})

	return up_ss


