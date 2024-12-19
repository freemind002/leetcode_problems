import polars as pl

data = [
    [1, 2, "2016-03-01", 5],
    [1, 2, "2016-03-02", 6],
    [2, 3, "2017-06-25", 1],
    [3, 1, "2016-03-02", 0],
    [3, 4, "2018-07-03", 5],
]
activity = pl.LazyFrame(
    data, schema=["player_id", "device_id", "event_date", "games_played"], orient="row"
).cast(
    {
        "player_id": pl.Int64,
        "device_id": pl.Int64,
        "event_date": pl.Date,
        "games_played": pl.Int64,
    }
)


def gameplay_analysis(activity: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        activity.group_by(["player_id"])
        .agg(event_date=pl.col("event_date"))
        .filter(pl.col("event_date").list.len() >= 2)
        .filter(
            (
                (
                    pl.col("event_date").list.get(1) - pl.col("event_date").list.first()
                ).dt.total_days()
                == 1
            )
        )
        .with_columns(
            fraction=(
                pl.col("player_id").count()
                / activity.unique("player_id").collect().height
            ).round(2)
        )
        .select("fraction")
        .collect()
    )

    return result_df


result = gameplay_analysis(activity)
print(result)
