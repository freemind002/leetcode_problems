import polars as pl

data = [
    [5, "Alice", 250, 1],
    [4, "Bob", 175, 5],
    [3, "Alex", 350, 2],
    [6, "John Cena", 400, 3],
    [1, "Winston", 500, 6],
    [2, "Marie", 200, 4],
]
queue = pl.LazyFrame(
    data, schema=["person_id", "person_name", "weight", "turn"], orient="row"
).cast(
    {
        "person_id": pl.Int64,
        "person_name": pl.String,
        "weight": pl.Int64,
        "turn": pl.Int64,
    }
)


def last_passenger(queue: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        queue.sort("turn")
        .with_columns(total_weight=pl.col("weight").cum_sum())
        .filter(pl.col("total_weight") <= 1000)
        .tail(1)
        .select("person_name")
        .collect()
    )

    return result_df


result = last_passenger(queue)
print(result)
