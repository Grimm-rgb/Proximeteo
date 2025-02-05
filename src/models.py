from pydantic import BaseModel
from sqlmodel import Field, SQLModel

#class représentant ton entité dans la base de données
class Releve(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    date: str
    temperature: float
    humidite: float
    idSonde: int

class Sonde(SQLModel, table=True) :
    id: int | None = Field(default=None, primary_key=True)
    is_active : bool