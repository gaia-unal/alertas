from fastapi import HTTPException
from routers import router
from manager import beacons
from typing import List, Optional
from manager.schemas.beacons_locations import BeaconsLocation 

@router.get("/beacons/{id}" ,response_model = List[BeaconsLocation])
def get_one(id: str):
	beacon = beacons.get_many({"id": id})
	if beacon is None:
		raise HTTPException(404)
	return beacon

@router.get("/beacons/",response_model = List[BeaconsLocation])
def get_many(id: Optional[str] = None, location: Optional[str] = None, active: Optional[bool] = None):
	query_parameters = {"id": id, "location":location, "active": active}
	beacon = beacons.get_many({e : query_parameters[e] for e in query_parameters if query_parameters[e]!= None})
	if beacon is None:
		raise HTTPException(404)
	return beacon