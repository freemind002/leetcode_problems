import polars as pl

data = [
    [3, "2020-03-21 10:16:13"],
    [7, "2020-01-04 13:57:59"],
    [2, "2020-07-29 23:09:44"],
    [6, "2020-12-09 10:39:37"],
]
signups = (
    pl.LazyFrame(data, schema=["user_id", "time_stamp"], orient="row")
    .cast({"user_id": pl.Int64, "time_stamp": pl.String})
    .with_columns(pl.col("time_stamp").str.to_datetime())
)
data = [
    [3, "2021-01-06 03:30:46", "timeout"],
    [3, "2021-07-14 14:00:00", "timeout"],
    [7, "2021-06-12 11:57:29", "confirmed"],
    [7, "2021-06-13 12:58:28", "confirmed"],
    [7, "2021-06-14 13:59:27", "confirmed"],
    [2, "2021-01-22 00:00:00", "confirmed"],
    [2, "2021-02-28 23:59:59", "timeout"],
]
confirmations = (
    pl.LazyFrame(data, schema=["user_id", "time_stamp", "action"], orient="row")
    .cast({"user_id": pl.Int64, "time_stamp": pl.String, "action": pl.String})
    .with_columns(pl.col("time_stamp").str.to_datetime())
)


def confirmation_rate(
    signups: pl.LazyFrame, confirmations: pl.LazyFrame
) -> pl.DataFrame:
    result_df = (
        signups.join(confirmations, on="user_id", how="left")
        .group_by("user_id")
        .agg(
            confirmation_rate=(
                pl.col("action").str.count_matches("confirmed").sum()
                / pl.col("action").len()
            ).round(2)
        )
        .collect()
    )

    return result_df


result = confirmation_rate(signups, confirmations)
print(result)
