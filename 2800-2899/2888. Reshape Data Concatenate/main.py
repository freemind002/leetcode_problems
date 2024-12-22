import polars as pl

lf_01 = pl.LazyFrame(
    [[1, "Mason", 8], [2, "Ava", 6], [3, "Taylor", 15], [4, "Georgia", 17]],
    ["student_id", "name", "age"],
)
lf_02 = pl.LazyFrame(
    [[5, "Leo", 7], [6, "Alex", 7]],
    ["student_id", "name", "age"],
)


def concatenateTables(lf1: pl.LazyFrame, lf2: pl.LazyFrame) -> pl.DataFrame:
    result = pl.concat([lf1, lf2]).collect()

    return result


result = concatenateTables(lf_01, lf_02)
print(result)
