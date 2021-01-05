from fastapi import APIRouter, HTTPException
from manager import get_session
from typing import List
from manager.models.beacon import Beacon

router = APIRouter()

@router.get("/session/{uuid}" ,response_model = List[Beacon])
def get_beacon_by_uuid(uuid):
	session = get_session.get_session(uuid)
	if session is None:
		raise HTTPException(404)
	return session