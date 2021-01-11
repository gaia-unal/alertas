from fastapi import APIRouter, Request, HTTPException
from manager import add_session, update_session, get_session
from typing import List
from manager.models.beacon import Beacon

router = APIRouter()

@router.post("/{location}")
def make_session(session_list: List[Beacon], location: str):
	session = add_session.add_session(session_list,location)
	return session

@router.post("/session/{uuid}/{location}")
def update_by_uuid(uuid,location: str, patch: List[Beacon], request: Request):
	if "PATCH" == request.headers.get("X-HTTP-Method-Override"):
		session = get_session.get_session(uuid)

		if session is None:
			raise HTTPException(404)

		up_session = update_session.update_session(uuid, patch,location)
		return up_session
	else:
		raise HTTPException(400)