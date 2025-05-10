import polars as pl

data = [
    [1, 10, 5, 10, 10],
    [2, 20, 20, 20, 20],
    [3, 10, 30, 20, 20],
    [4, 10, 40, 40, 40],
]
insurance = pl.LazyFrame(
    data,
    schema={
        "pid": pl.Int64,
        "tiv_2015": pl.Float64,
        "tiv_2016": pl.Float64,
        "lat": pl.Float64,
        "lon": pl.Float64,
    },
    orient="row",
)


def find_investments(insurance: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        insurance.filter(
            pl.col("pid").is_in(
                insurance.filter(pl.col("tiv_2015").is_duplicated())
                .collect()
                .get_column("pid")
            ),
            ~pl.col("pid").is_in(
                insurance.filter(pl.struct(["lat", "lon"]).is_duplicated())
                .collect()
                .get_column("pid")
            ),
        )
        .select(pl.col("tiv_2016").sum().round(2))
        .collect()
    )

    return result_df


result = find_investments(insurance)
print(result)
