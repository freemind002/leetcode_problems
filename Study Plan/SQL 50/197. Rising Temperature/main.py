import polars as pl

data = [
    [1, "2015-01-01", 10],
    [2, "2015-01-02", 25],
    [3, "2015-01-03", 20],
    [4, "2015-01-04", 30],
]
weather = pl.LazyFrame(data, schema=["id", "recordDate", "temperature"]).cast(
    {"id": pl.Int64, "recordDate": pl.Datetime, "temperature": pl.Int64}
)


def rising_temperature(weather: pl.LazyFrame) -> pl.DataFrame:
    result_df = weather.filter(pl.col("temperature").diff() > 0).select("id").collect()

    return result_df


result = rising_temperature(weather)
print(result)
