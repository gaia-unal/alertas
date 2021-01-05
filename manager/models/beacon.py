from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class Beacon(BaseModel):
	from_ : datetime
	id : str
	rssi : list
	until : datetime 