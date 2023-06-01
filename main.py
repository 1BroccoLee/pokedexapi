from fastapi import FastAPI, Depends, UploadFile, HTTPException
from sqlalchemy.orm import Session, subqueryload
from PokedexAPI.database import engine, SessionLocal, Base
from PokedexAPI.schemas import PokemonResponseModel
import PokedexAPI.fileuploads
import PokedexAPI.models
from typing import List
# from fastapi_pagination import Page, paginate, Params, add_pagination


app = FastAPI()
# add_pagination(app)

Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/pokemon")
def Upload_Pokemon(pokemonCSVFile: UploadFile, db: Session = Depends(get_db)):
    PokedexAPI.fileuploads.uploadCSVFileToPokemonDatabase(pokemonCSVFile, db)
    return {"message": "Pokemon Data uploaded"}


@app.post("/pokemon_stats")
def Upload_Pokemon_Stats(pokemonStatsCSVFile: UploadFile, db: Session = Depends(get_db)):
    PokedexAPI.fileuploads.uploadCSVFileToPokemonStatsDatabase(
        pokemonStatsCSVFile, db)
    return {"message": "Stats Data uploaded"}


@app.get("/pokemon", response_model=List[PokemonResponseModel])
def Get_All_Pokemon(db: Session = Depends(get_db)):
    pokemon = db.query(PokedexAPI.models.Pokemon).options(
        subqueryload(PokedexAPI.models.Pokemon.stats)).all()
    return pokemon

# @app.get("/pokemon", response_model=Page[PokemonResponseModel])
# def Get_All_Pokemon(db: Session = Depends(get_db)):
#     pokemon = db.query(PokedexAPI.models.Pokemon).options(
#         subqueryload(PokedexAPI.models.Pokemon.stats)).all()
#     return paginate(pokemon)


@app.get("/pokemon/{pokemon_name}", response_model=PokemonResponseModel)
def Get_Pokemon_name(pokemon_name: str, db: Session = Depends(get_db)):
    pokemon = db.query(PokedexAPI.models.Pokemon).filter(
        PokedexAPI.models.Pokemon.name.ilike(pokemon_name)).first()
    # ilike allows search that is not case sensitive
    if not pokemon:
        raise HTTPException(404, "Pokemon not found")
    return pokemon
