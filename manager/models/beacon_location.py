from pydantic import BaseModel
from datetime import datetime

class BeaconLocation(BaseModel):
	id : str
	from_ : datetime
	until : datetime 
	location : str
	status : bool

	class Config:
		orm_mode = True