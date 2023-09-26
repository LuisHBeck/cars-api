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
	return {"message": "Welcome to cars API!"}

# GET ALL CARS
@app.get('/api/v1/cars')
async def get_cars():
    return db

# GET CAR BY ID
@app.get('/api/v1/cars/{car_id}')
async def get_car(car_id: int):
    for car in db:
        if car.id == car_id:
            return car
    return HTTPException(404, f"No such car with id: {car_id}")

# DELETE CAR
@app.delete('/api/v1/cars/{car_id}')
async def delte_car(car_id: int):
    for car in db:
        if car.id == car_id:
            db.remove(car)
            return {'on_delete': 'success'}
    return HTTPException(404, f"No such car with id: {car_id}")