from fastapi import FastAPI, Request, HTTPException
import python_conn
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

app = FastAPI()

class Beacon(BaseModel):
	from_ : datetime
	id : str
	rssi : list
	until : datetime 

class BeaconPatchSchema(BaseModel):
	from_: datetime
	id : str
	rssi : list
	until : datetime

@app.get("/beacons/{uuid}" ,response_model = List[Beacon])
def get_beacon_by_uuid(uuid):
	session = python_conn.find_one(uuid)
	if session is None:
		raise HTTPException(404)
	return session

@app.post("/")
def make_session(session_list: List[Beacon]):
	session = python_conn.insert(session_list)
	return session

@app.post("/beacons/{uuid}")
def update_by_uuid(uuid, patch: List[BeaconPatchSchema], request: Request):
	if "PATCH" == request.headers.get("X-HTTP-Method-Override"):
		session = python_conn.find_one(uuid)

		if session is None:
			raise HTTPException(404)

		beacons = [dict(beacon) for beacon in patch ]
		up_session = python_conn.update(uuid, beacons)

		return up_session
	else:
		raise HTTPException(400)
