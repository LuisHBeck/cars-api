from fastapi import FastAPI, HTTPException, Depends, Response
from typing import List, Union
from sqlmodel import Session, select
from database import engine, CarModel
from models import Car, Fuel

app = FastAPI()


def get_session():
    with Session(engine) as session:
        yield session


@app.get('/')
async def root():
	return {"message": "Welcome to cars API!"}

# GET ALL CARS
@app.get('/api/v1/cars/') 
async def get_cars(session: Session() = Depends(get_session)):
    statement = select(CarModel)
    result = session.exec(statement).all()
    return result
    
# GET CAR BY ID
@app.get('/api/v1/cars/{car_id}/', response_model=Car)
async def get_car(car_id: int, session: Session() = Depends(get_session)):
    car = session.get(CarModel, car_id)
    if car is not None:
        return car
    raise HTTPException(404, f"No such car with id: {car_id}")

# CREATE NEW CAR
@app.post('/api/v1/cars/', response_model=Car, status_code=201)
async def post_car(car: CarModel, session: Session() = Depends(get_session)):
    session.add(car)
    session.commit()
    session.refresh(car)
    return car

# UPDATE CAR INFO
@app.put('/api/v1/cars/{car_id}/', response_model=Car)
async def put_car(car_id: int, update_data: Car, session: Session() = Depends(get_session)):
    car = session.get(CarModel, car_id)
    car_dict = update_data.dict(exclude_unset=True)

    if car is None: 
        raise HTTPException(404, f"No such car with id: {car_id}")
    
    for key, value in car_dict.items():
        setattr(car, key, value)
    session.add(car)
    session.commit()
    session.refresh(car)
    return car

# DELETE CAR
@app.delete('/api/v1/cars/{car_id}/')
async def delte_car(car_id: int, session: Session() = Depends(get_session)):
    car = session.get(CarModel, car_id)

    if car is None: 
        raise HTTPException(404, f"No such car with id: {car_id}")
    
    session.delete(car)
    session.commit()
    return Response(status_code=200)