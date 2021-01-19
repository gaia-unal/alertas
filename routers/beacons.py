from routers import router
from manager.schemas.beacons_locations import BeaconsLocation, BeaconLocationName
from manager import beacons
from datetime import datetime

@router.post("/beacons/{id}/location")
def create_one(id: str, location_name: BeaconLocationName):
    beacon_location = BeaconsLocation(id = id, location = location_name.name, from_ = datetime.now())
    beacon = beacons.add_one(beacon_location)
    return beacon

@router.patch("/beacons/{id}/deactivate")
def deactivate_one(id:str):
    beacons.deactivate_one(id)
