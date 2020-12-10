import psycopg2
import uuid
import ast
import json

def connect():
	coon = None

	try:

		print('Connecting to the PostgreSQL database...')
		conn = psycopg2.connect(
			host = 'localhost',
			database = 'beacons_db',
			user = 'postgres',
			password = "gaia_user"
			)

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	return conn
'''
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed.')'''

def insert(beacon_):
	conn = connect()
	cur = conn.cursor()
	beacon = ast.literal_eval(beacon_)
	beacon['uuid'] = str(uuid.uuid4())
	values_ = (beacon['uuid'],beacon['id'],beacon['from_'],beacon['until'],beacon['rssi'])
	insert_query ='INSERT INTO beacons (uuid,id,from_,until,rssi) VALUES (%s,%s,%s,%s,%s)' 
	cur.execute(insert_query,values_)
	conn.commit()
	return beacon

def find_one(uuid_):
	conn = connect()
	cur = conn.cursor()
	find_query = 'SELECT (from_,id,rssi,until) FROM beacons WHERE (uuid = %s)'
	cur.execute(find_query,(uuid_,))
	response = cur.fetchone()
	bea_list = response[0].strip('(\\)\"').split('\"')
	beacon = {"from_":bea_list[0],"id":bea_list[1].strip(','),"rssi":ast.literal_eval(bea_list[2]),"until":bea_list[4]}
	return beacon

def update(uuid,beacon_):
	conn = connect()
	cur = conn.cursor()
	beacon = ast.literal_eval(beacon_)
	beacon['uuid'] = uuid
	values_ = (beacon['rssi'],beacon['until'],beacon['uuid'])
	update_query = 'UPDATE beacons set rssi = %s , until = %s WHERE (uuid = %s)'
	cur.execute(update_query,values_)
	conn.commit()
	return beacon


