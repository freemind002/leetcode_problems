import polars as pl

data = [
    [2, "Meir", 3000],
    [3, "Michael", 3800],
    [7, "Addilyn", 7400],
    [8, "Juan", 6100],
    [9, "Kannon", 7700],
]
employees = pl.LazyFrame(
    data, schema=["employee_id", "name", "salary"], orient="row"
).cast({"employee_id": pl.Int64, "name": pl.String, "salary": pl.Int64})


def calculate_special_bonus(employees: pl.LazyFrame) -> pl.DataFrame:
    result_df = employees.select(
        [
            "employee_id",
            pl.when(
                (pl.col("employee_id") % 2 != 0)
                & (~pl.col("name").str.starts_with("M"))
            )
            .then(pl.col("salary"))
            .otherwise(pl.lit(0))
            .alias("bonus"),
        ]
    ).collect()

    return result_df


result = calculate_special_bonus(employees)
print(result)
