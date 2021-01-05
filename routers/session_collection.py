from fastapi import APIRouter, HTTPException
from manager import verbs_functions_for_db as functions_db
from typing import List
from manager.models.beacon import Beacon

router = APIRouter()

@router.get("/session/{uuid}" ,response_model = List[Beacon])
def get_beacon_by_uuid(uuid):
	session = functions_db.find_one(uuid)
	if session is None:
		raise HTTPException(404)
	return session