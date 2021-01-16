from fastapi import APIRouter, HTTPException
from manager import beacons_crud
from typing import List, Optional
from manager.models.beacon_location import BeaconLocation 

router = APIRouter()

@router.get("/beacon/{id}" ,response_model = List[BeaconLocation])
def get_beacon_by_id(id: str):
	beacon = beacons_crud.get_beacons(id)
	if beacon is None:
		raise HTTPException(404)
	return beacon

@router.get("/beacons/")
def read_sessions(beacon_id: Optional[str] = None, location: Optional[str] = None, active: Optional[bool] = None):
	query_parameters = {"id": beacon_id, "location":location, "active": active}
	beacon = beacons_crud.get_beacons_with_filters({e : query_parameters[e] for e in query_parameters if query_parameters[e]!= None})
	if beacon is None:
		raise HTTPException(404)
	return beacon