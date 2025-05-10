import polars as pl

data = [[8], [8], [3], [3], [1], [4], [5], [6]]
# data = [[8], [8], [7], [7], [3], [3], [3]]
my_numbers = pl.LazyFrame(data, schema={"num": pl.Int64}, orient="row")


def biggest_single_number(my_numbers: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        my_numbers.filter(~pl.col("num").is_duplicated()).sort("num").tail(1).collect()
    )

    return result_df


result = biggest_single_number(my_numbers)
print(result)
