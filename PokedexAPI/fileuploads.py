import csv
from PokedexAPI.models import Pokemon, PokemonStats


def uploadCSVFileToPokemonDatabase(file, db):
    fileContent = file.file.read().decode("utf-8")
    rows = csv.reader(fileContent.splitlines(), delimiter=",")
    next(rows)
    for row in rows:
        pokemon = Pokemon(classification=row[1], name=row[3], type1=row[5],
                          type2=row[6], generation=row[7], legendary=row[8])
        db.add(pokemon)
    db.commit()


def uploadCSVFileToPokemonStatsDatabase(file, db):
    fileContent = file.file.read().decode("utf-8")
    rows = csv.reader(fileContent.splitlines(), delimiter=",")
    next(rows)
    for row in rows:
        pokemonStats = PokemonStats(pokemon_id=row[0],
                                    against_bug=row[1],
                                    against_dark=row[2],
                                    against_dragon=row[3],
                                    against_electric=row[4],
                                    against_fairy=row[5],
                                    against_fight=row[6],
                                    against_fire=row[7],
                                    against_flying=row[8],
                                    against_ghost=row[9],
                                    against_grass=row[10],
                                    against_ground=row[11],
                                    against_ice=row[12],
                                    against_normal=row[13],
                                    against_poison=row[14],
                                    against_psychic=row[15],
                                    against_rock=row[16],
                                    against_steel=row[17],
                                    against_water=row[18],
                                    attack=row[19],
                                    # base_egg_steps=row[20],
                                    # base_happiness=row[21],
                                    # base_total=row[22],
                                    # capture_rate=row[23],
                                    defense=row[24],
                                    experience_growth=row[25],
                                    height_m=row[26]if row[26]else None,
                                    hp=row[27],
                                    sp_attack=row[28],
                                    sp_defense=row[29],
                                    speed=row[30],
                                    weight_kg=row[31] if row[31]else None)
        db.add(pokemonStats)
    db.commit()
