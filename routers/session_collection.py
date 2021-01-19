from fastapi import HTTPException
from routers import router
from manager import sessions
from manager.schemas.beacons import Beacon

from typing import List
import uuid

@router.get("/sessions/{uuid}" ,response_model = List[Beacon])
def get_one(uuid):
	session = sessions.get_one(uuid)
	if session is None:
		raise HTTPException(404)
	return session
