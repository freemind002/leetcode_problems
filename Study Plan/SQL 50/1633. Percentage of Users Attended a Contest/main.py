import polars as pl

data = [[6, "Alice"], [2, "Bob"], [7, "Alex"]]
users = pl.LazyFrame(data, schema=["user_id", "user_name"], orient="row").cast(
    {"user_id": pl.Int64, "user_name": pl.String}
)
data = [
    [215, 6],
    [209, 2],
    [208, 2],
    [210, 6],
    [208, 6],
    [209, 7],
    [209, 6],
    [215, 7],
    [208, 7],
    [210, 2],
    [207, 2],
    [210, 7],
]
register = pl.LazyFrame(data, schema=["contest_id", "user_id"], orient="row").cast(
    {"contest_id": pl.Int64, "user_id": pl.Int64}
)


def users_percentage(users: pl.LazyFrame, register: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        users.join(register, on="user_id", how="left")
        .group_by("contest_id")
        .agg(
            percentage=(
                pl.col("user_id").count()
                / users.unique("user_id").collect().height
                * 100
            ).round(2)
        )
        .collect()
    )

    return result_df


result = users_percentage(users, register)
print(result)
