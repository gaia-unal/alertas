from pydantic import BaseModel
from datetime import datetime

class Beacon(BaseModel):
	from_ : datetime
	id : str
	rssi : list
	until : datetime 

	class Config:
		orm_mode = True