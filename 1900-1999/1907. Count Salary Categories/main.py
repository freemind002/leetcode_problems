import polars as pl

data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
accounts = pl.LazyFrame(data, schema=["account_id", "income"], orient="row").cast(
    {"account_id": pl.Int64, "income": pl.Int64}
)


def count_salary_categories(accounts: pl.LazyFrame) -> pl.DataFrame:
    print(accounts.collect())
    result_df = pl.LazyFrame(
        data=[
            ["Low Salary", accounts.filter(pl.col("income") < 20000).collect().height],
            [
                "Average Salary",
                accounts.filter(pl.col("income").is_between(20000, 50000))
                .collect()
                .height,
            ],
            ["High Salary", accounts.filter(pl.col("income") > 50000).collect().height],
        ],
        schema=["category", "accounts_count"],
        orient="row",
    ).collect()

    return result_df


result = count_salary_categories(accounts)
print(result)
