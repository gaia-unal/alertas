import psycopg2
import uuid
import ast
import json
from psycopg2.extras import DictCursor, execute_values

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

def update(uuid_, beacons):
	conn = connect()
	cur = conn.cursor()
	
	columns = beacons[0].keys()
	query  = 'INSERT INTO beacons (uuid, {}) VALUES %s ON CONFLICT (uuid, id) DO UPDATE SET rssi = EXCLUDED.rssi, until = EXCLUDED.until'.format(','.join(columns))
	values = [[uuid_, *[value for value in beacon.values()]]  for beacon in beacons]
	execute_values(cur, query, values)
	conn.commit()
	
	up_ss = find_one(uuid_)
	up_ss.append({"uuid": str(uuid_)})

	return up_ss


