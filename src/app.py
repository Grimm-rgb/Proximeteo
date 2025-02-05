from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
# on import la configuration nécessaire à la connexion à la base de donnée
from database import *
# on import l'ensemble des des models représentant les entités que l'on va manipuler dans la base
from models import *
from fastapi.middleware.cors import CORSMiddleware


# Lancement de fastAPI
app = FastAPI()

# Autorise les requettes de différents endroits 
# /!\  peu sécurisé
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# les routes de l'API
# releve
@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/releve/")
def create_releve(releve: Releve, session: SessionDep) -> Releve:
    session.add(releve)
    session.commit()
    session.refresh(releve)
    return releve

@app.get("/releve/")
def read_releve(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=5)] = 2,
    #le correspond à la valeur max autorisée et derrière le = c'est le nombre par défaut
) -> list[Releve]:
    releves = session.exec(select(Releve).offset(offset).limit(limit)).all()
    return releves

@app.get("/releve/{releve_id}")
def read_releve_by_id(
    session: SessionDep,
    releve_id : int
) -> Releve:
    releve = session.get(Releve, releve_id)
    return releve


@app.get("/")
def read_root():
    return {"Hello": "World"}

# sonde

@app.post("/sonde/")
def create_sonde(sonde: Sonde, session: SessionDep) -> Sonde:
    session.add(sonde)
    session.commit()
    session.refresh(sonde)
    return sonde

@app.get("/sonde/")
def read_sonde(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=6)] = 6,
) -> list[Sonde]:
    sonde = session.exec(select(Releve).offset(offset).limit(limit)).all()
    return sonde
