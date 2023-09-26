from typing import Optional, List
from pydantic import BaseModel
from enum import Enum


class Fuel(str, Enum):
    ethanol = 'ethanol'
    gasoline = 'gasoline'
    flex = 'flex'
    electric = 'electric'
    hybrid = 'hybrid'
    

class Car(BaseModel):
	id: Optional[int] = None
	manufacturer: str
	model: str
	year: int
	motorization: float
	fuel: Fuel
	avg_consumption: Optional[float] = None
	plate_number: str