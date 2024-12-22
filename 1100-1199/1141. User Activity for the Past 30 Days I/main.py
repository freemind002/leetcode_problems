from datetime import date, timedelta

import polars as pl

data = [
    [1, 1, "2019-07-20", "open_session"],
    [1, 1, "2019-07-20", "scroll_down"],
    [1, 1, "2019-07-20", "end_session"],
    [2, 4, "2019-07-20", "open_session"],
    [2, 4, "2019-07-21", "send_message"],
    [2, 4, "2019-07-21", "end_session"],
    [3, 2, "2019-07-21", "open_session"],
    [3, 2, "2019-07-21", "send_message"],
    [3, 2, "2019-07-21", "end_session"],
    [4, 3, "2019-06-25", "open_session"],
    [4, 3, "2019-06-25", "end_session"],
]
activity = pl.LazyFrame(
    data,
    schema=["user_id", "session_id", "activity_date", "activity_type"],
    orient="row",
).cast(
    {
        "user_id": pl.Int64,
        "session_id": pl.Int64,
        "activity_date": pl.Date,
        "activity_type": pl.String,
    }
)


def user_activity(activity: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        activity.filter(
            pl.col("activity_date").is_between(
                date(2019, 7, 27) + timedelta(days=-29),
                date(2019, 7, 27),
            )
        )
        .group_by("activity_date")
        .agg(active_users=pl.col("user_id").n_unique())
        .rename({"activity_date": "day"})
        .collect()
    )

    return result_df


result = user_activity(activity)
print(result)
