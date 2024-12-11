from typing import List

import polars as pl

players_data = [
    [846, "Mason", 21, "Forward", "RealMadrid"],
    [749, "Railey", 30, "Winger", "Barcelona"],
    [155, "Bob", 28, "Striker", "ManchesterUnited"],
    [583, "Isabella", 32, "Goalkeeper", "Liverpool"],
    [388, "Zachary", 24, "Midfielder", "BayernMunich"],
    [883, "Ava", 23, "Defender", "Chelsea"],
    [355, "Violet", 18, "Striker", "Juventus"],
    [247, "Thomas", 27, "Striker", "ParisSaint-Germain"],
    [761, "Jack", 33, "Midfielder", "ManchesterCity"],
    [642, "Charlie", 36, "Center-back", "Arsenal"],
]
players_schema = ["player_id", "name", "age", "position", "team"]

lf = pl.LazyFrame(players_data, players_schema)


def getDataframeSize(players: pl.LazyFrame) -> List[int]:
    rows = players.collect().height
    columns = players.collect().width

    return [rows, columns]


result = getDataframeSize(lf)
print(result)
