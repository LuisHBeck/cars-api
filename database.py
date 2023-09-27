from typing import Optional

from sqlmodel import SQLModel, Field, create_engine

DB_FILE = 'db.sqlite3'
engine = create_engine(f'sqlite:///{DB_FILE}', echo=True)


class CarModel(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	manufacturer: str
	model: str
	year: int
	motorization: float
	fuel: str
	avg_consumption: Optional[float] = None
	# plate_number: str
	plate_number: str = Field(unique=True)


def create_tables():
	SQLModel.metadata.create_all(engine)


if __name__ == '__main__':
	create_tables()