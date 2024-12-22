import polars as pl

weather_lf = pl.LazyFrame(
    [
        ["Jacksonville", "January", 13],
        ["Jacksonville", "February", 23],
        ["Jacksonville", "March", 38],
        ["Jacksonville", "April", 5],
        ["Jacksonville", "May", 34],
        ["ElPaso", "January", 20],
        ["ElPaso", "February", 6],
        ["ElPaso", "March", 26],
        ["ElPaso", "April", 2],
        ["ElPaso", "May", 43],
    ],
    ["city", "month", "temperature"],
)


def pivotTable(weather: pl.LazyFrame) -> pl.DataFrame:
    result = weather.collect().pivot(on="city", index="month", values="temperature")

    return result


result = pivotTable(weather_lf)
print(result)
