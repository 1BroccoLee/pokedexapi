from sqlalchemy import Column, Integer, Float, String, ForeignKey
from PokedexAPI.database import Base
from sqlalchemy.orm import relationship


# models, for use when using db software such as postgres. below we are creating tables in the database

class Pokemon(Base):
    __tablename__ = "pokemon_data"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))
    classification = Column(String(150))
    type1 = Column(String(50))
    type2 = Column(String(50))
    generation = Column(Integer)
    legendary = Column(Integer)

    stats = relationship("PokemonStats", backref="Pokemon", uselist=False)


class PokemonStats(Base):
    __tablename__ = "pokemon_stats"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pokemon_id = Column(Integer, ForeignKey("pokemon_data.id"))
    against_bug = Column(Float, nullable=True)
    against_dark = Column(Float, nullable=True)
    against_dragon = Column(Float, nullable=True)
    against_electric = Column(Float, nullable=True)
    against_fairy = Column(Float, nullable=True)
    against_fight = Column(Float, nullable=True)
    against_fire = Column(Float, nullable=True)
    against_flying = Column(Float, nullable=True)
    against_ghost = Column(Float, nullable=True)
    against_grass = Column(Float, nullable=True)
    against_ground = Column(Float, nullable=True)
    against_ice = Column(Float, nullable=True)
    against_normal = Column(Float, nullable=True)
    against_poison = Column(Float, nullable=True)
    against_psychic = Column(Float, nullable=True)
    against_rock = Column(Float, nullable=True)
    against_steel = Column(Float, nullable=True)
    against_water = Column(Float, nullable=True)
    attack = Column(Integer, nullable=True)
    defense = Column(Integer, nullable=True)
    experience_growth = Column(Integer, nullable=True)
    height_m = Column(Float, nullable=True)
    hp = Column(Integer, nullable=True)
    sp_attack = Column(Integer, nullable=True)
    sp_defense = Column(Integer, nullable=True)
    speed = Column(Integer, nullable=True)
    weight_kg = Column(Float, nullable=True)
