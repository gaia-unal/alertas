from fastapi import APIRouter, Request, HTTPException
from manager.models.beacon_location import BeaconLocation, BeaconLocationName
from manager.beacons_crud import add_beacon, update_beacon
from datetime import datetime


router = APIRouter()

@router.post("/beacon/{id}/{location}")
def add_beacon_location(id: str, location_name: BeaconLocationName):
    beacon_location = BeaconLocation(id = id, location = location_name.name, from_ = datetime.now())
    beacon = add_beacon(beacon_location)
    return beacon

@router.patch("/beacon/{id}/{deactivate}")
def update_beacon_location(id, request: Request):
    update_beacon(id)