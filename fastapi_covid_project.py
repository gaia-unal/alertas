from fastapi import FastAPI
import python_conn
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

app = FastAPI()

class Beacon(BaseModel):
	from_ : datetime
	id : str
	rssi : list
	until : datetime 

class BeaconPatchSchema(BaseModel):
	from_: Optional[datetime] = None
	id : Optional[str] = None
	rssi : Optional[list]
	until : datetime

@app.get("/beacons/{uuid}", response_model = Beacon)
def get_beacon_by_uuid(uuid):
	beacon = python_conn.find_one(uuid)
	if beacon is None:
		raise HTTPException(404)
	return beacon

@app.post("/")
def make_beacons(beacon: Beacon):
	beacon_dict = python_conn.insert(beacon.json())
	return beacon_dict

@app.patch("/beacons/{uuid}", response_model = Beacon)
def update_by_uuid(uuid, patch: BeaconPatchSchema):
	beacon_data = python_conn.find_one(uuid)
	if beacon_data is None:
		raise HTTPException(404)
	beacon_model = Beacon(**beacon_data)
	update_data = patch.dict(exclude_unset = True)
	update_beacon = beacon_model.copy(update = update_data)
	beacon = python_conn.update(uuid,update_beacon.json())
	return beacon
