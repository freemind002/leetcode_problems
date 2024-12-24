import polars as pl

data = [[1, "john@example.com"], [2, "bob@example.com"], [3, "john@example.com"]]
person = pl.LazyFrame(data, schema=["id", "email"], orient="row").cast(
    {"id": pl.Int64, "email": pl.String}
)


def delete_duplicate_emails(person: pl.LazyFrame) -> pl.DataFrame:
    result_df = person.unique(subset="email", keep="first").sort("id").collect()

    return result_df


result = delete_duplicate_emails(person)
print(result)
