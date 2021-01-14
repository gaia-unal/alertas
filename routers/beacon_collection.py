from fastapi import APIRouter, HTTPException
from manager import beacons_crud
from typing import List
from manager.models.beacon_location import BeaconLocation 

router = APIRouter()

@router.get("/beacon/{id}" ,response_model = List[BeaconLocation])
def get_beacon_by_id(id: str):
	beacon = beacons_crud.get_beacons(id)
	if beacon is None:
		raise HTTPException(404)
	return beacon