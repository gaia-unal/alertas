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
	from_: Optional[datetime]
	id : Optional[str]
	rssi : Optional[list]
	until : Optional[datetime]


@app.get("/")
def read_root():
	return {"Hello":"World"}

@app.get("/beacons/{uuid}", response_model = Beacon)
def get_beacon_by_uuid(uuid):
	beacon = python_conn.find_one(uuid)
	if beacon is None:
		raise HTTPException(404)
	return beacon

@app.post("/")
def make_beacons(beacon: Beacon):
	uuid = python_conn.insert(beacon.json())
	return uuid,diccionario

@app.patch("/{uuid}")
def update_by_uuid(uuid, patch: BeaconPatchSchema):
	beacon_data = python_conn.find_one(uuid)
	if beacon_data is None:
		raise HTTPException(404)
	beacon_model = Beacon(**beacon_data)
	update_data = patch.dict(exclude_unset = True)
	update_beacon = beacon_model.copy(update = update_data)

	return update_beacon
