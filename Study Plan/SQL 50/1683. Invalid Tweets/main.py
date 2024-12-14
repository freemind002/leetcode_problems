import polars as pl

data = [[1, "Let us Code"], [2, "More than fifteen chars are here!"]]
schema = ["tweet_id", "content"]
lf = pl.LazyFrame(data, schema, orient="row").cast(
    {"tweet_id": pl.Int64, "content": pl.String}
)


def invalid_tweets(tweets: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        tweets.filter(pl.col("content").str.len_chars() > 15)
        .select("tweet_id")
        .collect()
    )

    return result_df


result = invalid_tweets(lf)
print(result)
