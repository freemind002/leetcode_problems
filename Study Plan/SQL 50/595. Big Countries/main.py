import polars as pl

data = [
    ["Afghanistan", "Asia", 652230, 25500100, 20343000000],
    ["Albania", "Europe", 28748, 2831741, 12960000000],
    ["Algeria", "Africa", 2381741, 37100000, 188681000000],
    ["Andorra", "Europe", 468, 78115, 3712000000],
    ["Angola", "Africa", 1246700, 20609294, 100990000000],
]
schema = ["name", "continent", "area", "population", "gdp"]
lf = pl.LazyFrame(data, schema, orient="row").cast(
    {
        "name": pl.String,
        "continent": pl.String,
        "area": pl.Int64,
        "population": pl.Int64,
        "gdp": pl.Int64,
    }
)


def big_countries(world: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        world.filter((pl.col("area") >= 3000000) | (pl.col("population") >= 25000000))
        .select(["name", "population", "area"])
        .collect()
    )

    return result_df


result = big_countries(lf)
print(result)
