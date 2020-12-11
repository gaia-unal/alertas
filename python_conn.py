import psycopg2
import uuid
import ast
import json

beacons_keys_list = ["from_","id","rssi","until"]

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

def insert(beacons):
	conn = connect()
	cur = conn.cursor()
	uuid_ = uuid.uuid4()
	val = [tuple(ast.literal_eval(beacon.json()).values() )for beacon in beacons]
	values = [(str(uuid_),) + val[i] for i in range(len(val))]
	beacons.append({'session_uuid':str(uuid_)})
	insert_query ='INSERT INTO beacons (uuid,from_,id,rssi,until) VALUES (%s,%s,%s,%s,%s)' 
	cur.executemany(insert_query,values)
	conn.commit()
	return beacons

def find_one(session_uuid):
	conn = connect()
	cur = conn.cursor()
	find_query = 'SELECT (from_,id,rssi,until) FROM beacons WHERE (uuid = %s)'
	cur.execute(find_query,(session_uuid,))
	response = cur.fetchall()
	resp = [response[i][0].strip("'()").split('"') for i in range(len(response))]
	li_be = [dict.fromkeys(beacons_keys_list,None) for i in range(len(resp))]
	for li,re in zip(li_be,resp):
		li["from_"] = re[1]
		li["id"] = re[2].strip(',')
		li["rssi"] = list(map(int, re[3].strip('{}').split(',')))
		li["until"] = re[5]
	return li_be

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


