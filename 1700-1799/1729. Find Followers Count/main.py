import polars as pl

data = [["0", "1"], ["1", "0"], ["2", "0"], ["2", "1"]]
followers = pl.LazyFrame(data, schema=["user_id", "follower_id"], orient="row").cast(
    {"user_id": pl.Int64, "follower_id": pl.Int64}
)


def count_followers(followers: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        followers.group_by("user_id")
        .agg(followers_count=pl.col("follower_id").count())
        .collect()
    )

    return result_df


result = count_followers(followers)
print(result)
