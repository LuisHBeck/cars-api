from fastapi import FastAPI, HTTPException
from typing import List

from models import Car, Fuel

db: List[Car] = [
    Car(
        id=1,
        manufacturer='Honda',
        model='Civic',
        year=2016,
        motorization=2.0,
        fuel=Fuel.flex,
        avg_consumption=9.0,
        plate_number='EAA-3719'
    )
]

app = FastAPI()

@app.get('/')
async def root():
	return {"message": "Hello, world!"}


@app.get('/api/v1/cars')
async def get_cars():
    return db