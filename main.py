from fastapi import FastAPI, Request, HTTPException
from manager import verbs_functions_for_db as functions_db
from typing import List
from manager.schemas.beacon import Beacon

app = FastAPI()

@app.get("/beacons/{uuid}" ,response_model = List[Beacon])
def get_beacon_by_uuid(uuid):
	session = functions_db.find_one(uuid)
	if session is None:
		raise HTTPException(404)
	return session

@app.post("/")
def make_session(session_list: List[Beacon]):
	session = functions_db.insert(session_list)
	return session

@app.post("/beacons/{uuid}")
def update_by_uuid(uuid, patch: List[Beacon], request: Request):
	if "PATCH" == request.headers.get("X-HTTP-Method-Override"):
		session = functions_db.find_one(uuid)

		if session is None:
			raise HTTPException(404)

		beacons = [dict(beacon) for beacon in patch ]
		up_session = functions_db.update(uuid, beacons)

		return up_session
	else:
		raise HTTPException(400)
