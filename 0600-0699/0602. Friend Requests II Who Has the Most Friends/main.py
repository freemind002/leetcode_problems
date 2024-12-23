import polars as pl

data = [
    [1, 2, "2016/06/03"],
    [1, 3, "2016/06/08"],
    [2, 3, "2016/06/08"],
    [3, 4, "2016/06/09"],
]
request_accepted = pl.LazyFrame(
    data, schema=["requester_id", "accepter_id", "accept_date"], orient="row"
).cast({"requester_id": pl.Int64, "accepter_id": pl.Int64, "accept_date": pl.Date})


def most_friends(request_accepted: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        pl.concat(
            [
                request_accepted.select(id=pl.col("requester_id")),
                request_accepted.select(id=pl.col("accepter_id")),
            ]
        )
        .group_by("id")
        .agg(num=pl.col("id").count())
        .sort("num", descending=True)
        .head(1)
        .collect()
    )

    return result_df


result = most_friends(request_accepted)
print(result)
