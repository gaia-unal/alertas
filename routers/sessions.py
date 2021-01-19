from fastapi import Request, HTTPException
from routers import router
from manager import sessions
from typing import List
from manager.schemas.beacons import Beacon

@router.post("/sessions")
def create_one(beacons_list: List[Beacon]):
	session = sessions.add_one(beacons_list)
	return session

@router.post("/sessions/{uuid}")
def update_one(uuid, patch: List[Beacon], request: Request):
	if "PATCH" == request.headers.get("X-HTTP-Method-Override"):
		session = sessions.get_one(uuid)

		if session is None:
			raise HTTPException(404)

		return sessions.update_one(uuid, patch)
	else:
		raise HTTPException(400)