import psycopg2
import uuid

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

def insert(beacon):
	conn = connect()
	cur = conn.cursor()
	uuid_ = uuid.uuid4()
	values_ = (str(uuid_),beacon)
	insert_query ='INSERT INTO beacons (id,info) VALUES (%s,%s)' 
	cur.execute(insert_query,values_)
	conn.commit()
	return uuid_

def find_one(id):
	conn = connect()
	cur = conn.cursor()
	find_query = 'SELECT (info) FROM beacons WHERE (id = %s) '
	cur.execute(find_query,(id,))
	response = cur.fetchone()
	return response[0]

def update(id):
	conn = connect()
	cur = conn.cursor()
	update_query = 'UPDATE beacons set rssi = %s , until = %s '


