import polars as pl

data = [
    [0, 0, "start", 0.712],
    [0, 0, "end", 1.52],
    [0, 1, "start", 3.14],
    [0, 1, "end", 4.12],
    [1, 0, "start", 0.55],
    [1, 0, "end", 1.55],
    [1, 1, "start", 0.43],
    [1, 1, "end", 1.42],
    [2, 0, "start", 4.1],
    [2, 0, "end", 4.512],
    [2, 1, "start", 2.5],
    [2, 1, "end", 5],
]
activity = pl.LazyFrame(
    data, schema=["machine_id", "process_id", "activity_type", "timestamp"]
).cast(
    {
        "machine_id": pl.Int64,
        "process_id": pl.Int64,
        "activity_type": pl.String,
        "timestamp": pl.Float64,
    }
)


def get_average_time(activity: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        activity.collect()
        .pivot(
            index=["machine_id", "process_id"], on="activity_type", values="timestamp"
        )
        .select(
            pl.col("machine_id"),
            (pl.col("end") - pl.col("start")).round(3).alias("processing_time"),
        )
        .group_by("machine_id")
        .mean()
    )

    return result_df


result = get_average_time(activity)
print(result)
