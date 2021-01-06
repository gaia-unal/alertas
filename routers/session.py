from fastapi import APIRouter, Request, HTTPException
from manager import add_session, update_session, get_session
from typing import List
from manager.models.beacon import Beacon

router = APIRouter()

@router.post("/")
def make_session(session_list: List[Beacon]):
	session = add_session.add_session(session_list)
	return session

@router.post("/session/{uuid}")
def update_by_uuid(uuid, patch: List[Beacon], request: Request):
	if "PATCH" == request.headers.get("X-HTTP-Method-Override"):
		session = get_session.get_session(uuid)

		if session is None:
			raise HTTPException(404)

		up_session = update_session.update_session(uuid, patch)
		return up_session
	else:
		raise HTTPException(400)