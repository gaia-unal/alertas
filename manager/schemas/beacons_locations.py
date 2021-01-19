from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BeaconsLocation(BaseModel):
	id : str
	location : str
	from_ : datetime
	until : Optional[datetime] = None
	active : Optional[bool] = None

	class Config:
		orm_mode = True

class BeaconLocationName(BaseModel):
	name : str