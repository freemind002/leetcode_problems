import polars as pl

data = [
    [1, 2, "2016-03-01", 5],
    [1, 2, "2016-03-02", 6],
    [2, 3, "2017-06-25", 1],
    [3, 1, "2016-03-02", 0],
    [3, 4, "2018-07-03", 5],
]
activity = pl.LazyFrame(
    data,
    schema={
        "player_id": pl.Int64,
        "device_id": pl.Int64,
        "event_date": pl.Date,
        "games_played": pl.Int64,
    },
    orient="row",
)


def gameplay_analysis(activity: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        activity.sort(["event_date", "player_id"])
        .group_by(["player_id"])
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
        .select(
            fraction=(
                pl.col("player_id").count() / activity.collect().n_unique("player_id")
            ).round(2)
        )
        .collect()
    )

    return result_df


result = gameplay_analysis(activity)
print(result)
