import polars as pl

data = [
    [1, "Winston", "winston@leetcode.com"],
    [2, "Jonathan", "jonathanisgreat"],
    [3, "Annabelle", "bella-@leetcode.com"],
    [4, "Sally", "sally.come@leetcode.com"],
    [5, "Marwan", "quarz#2020@leetcode.com"],
    [6, "David", "david69@gmail.com"],
    [7, "Shapiro", ".shapo@leetcode.com"],
]
users = pl.LazyFrame(
    data,
    schema={"user_id": pl.Int64, "name": pl.String, "mail": pl.String},
    orient="row",
)


def valid_emails(users: pl.LazyFrame) -> pl.DataFrame:
    result_df = users.filter(
        pl.col("mail").str.contains(
            r"^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\?com)?\.com$"
        )
    ).collect()

    return result_df


result = valid_emails(users)
print(result)
