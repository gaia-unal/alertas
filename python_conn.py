import psycopg2
import uuid
import ast
import json
from psycopg2.extras import DictCursor

beacons_keys_list = ["from_","id","rssi","until"]

def connect():
	coon = None

	try:

		print('Connecting to the PostgreSQL database...')
		conn = psycopg2.connect(
			host = 'localhost',
			database = 'beacons_db',
			user = 'postgres',
			password = "%froac$"
			)

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	return conn

def insert(beacons):
	conn = connect()
	cur = conn.cursor()
	uuid_ = uuid.uuid4()
	val = [tuple(ast.literal_eval(beacon.json()).values() )for beacon in beacons]
	values = [(str(uuid_),) + val[i] for i in range(len(val))]
	insert_query ='INSERT INTO beacons (uuid,from_,id,rssi,until) VALUES (%s,%s,%s,%s,%s)' 
	cur.executemany(insert_query,values)
	conn.commit()
	return {'session_uuid':str(uuid_)}

def find_one(session_uuid):
	conn = connect()
	cur = conn.cursor(cursor_factory=DictCursor)
	find_query = 'SELECT from_, id, rssi, until FROM beacons WHERE (uuid = %s)'
	cur.execute(find_query,(session_uuid,))
	response = cur.fetchall()

	data = [dict(row) for row in response]

	return data

def update(uuid_,session,up_session):
	conn = connect()
	cur = conn.cursor()
	insert_values = list()
	update_values = list()
	val_up_se = [tuple(ast.literal_eval(sess.json()).values() )for sess in up_session]
	id_se = [se['id']for se in session]
	values_up_se = [(str(uuid_),) + val_up_se[i] for i in range(len(val_up_se))]
	for va in values_up_se:
		if va[2] not in id_se:
			insert_values.append(va)
		else:
			update_values.append(tuple([va[3],va[4],va[0],va[2]]))
	if len(update_values) != 0:
		update_query = 'UPDATE beacons set rssi = %s , until = %s WHERE (uuid = %s and id = %s)'
		cur.executemany(update_query,update_values)
		conn.commit()
	if len(insert_values) != 0:
		insert_query ='INSERT INTO beacons (uuid,from_,id,rssi,until) VALUES (%s,%s,%s,%s,%s)' 
		cur.executemany(insert_query,insert_values)
		conn.commit()
	up_ss = find_one(uuid_)
	up_ss.append({"uuid":str(uuid_)})
	return up_ss


