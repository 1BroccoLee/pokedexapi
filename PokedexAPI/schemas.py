from pydantic import BaseModel, EmailStr, validator
from typing import Optional


class PokemonStatsResponseModel(BaseModel):
    against_bug: Optional[float] = None
    against_dark: Optional[float] = None
    against_dragon: Optional[float] = None
    against_electric: Optional[float] = None
    against_fairy: Optional[float] = None
    against_fight: Optional[float] = None
    against_fire: Optional[float] = None
    against_flying: Optional[float] = None
    against_ghost: Optional[float] = None
    against_grass: Optional[float] = None
    against_ground: Optional[float] = None
    against_ice: Optional[float] = None
    against_normal: Optional[float] = None
    against_poison: Optional[float] = None
    against_psychic: Optional[float] = None
    against_rock: Optional[float] = None
    against_steel: Optional[float] = None
    against_water: Optional[float] = None
    attack: Optional[int] = None
    defense: Optional[int] = None
    experience_growth: Optional[int] = None
    height_m: Optional[float] = None
    hp: Optional[int] = None
    sp_attack: Optional[int] = None
    sp_defense: Optional[int] = None
    speed: Optional[int] = None
    weight_kg: Optional[float] = None

    class Config:
        orm_mode = True


class PokemonResponseModel(BaseModel):
    id: int
    name: str
    classification: str
    type1: str
    type2: str
    generation: int
    stats: PokemonStatsResponseModel
    legendary: int

    class Config:
        orm_mode = True
