import polars as pl

data = [
    [3, "Brad", None, 4000],
    [1, "John", 3, 1000],
    [2, "Dan", 3, 2000],
    [4, "Thomas", 3, 4000],
]
employee = pl.LazyFrame(
    data, schema=["empId", "name", "supervisor", "salary"], orient="row"
).cast(
    {"empId": pl.Int64, "name": pl.String, "supervisor": pl.Int64, "salary": pl.Int64}
)
data = [[2, 500], [4, 2000]]
bonus = pl.LazyFrame(data, schema=["empId", "bonus"], orient="row").cast(
    {"empId": pl.Int64, "bonus": pl.Int64}
)


def employee_bonus(employee: pl.LazyFrame, bonus: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        employee.join(bonus, on="empId", how="left")
        .filter((pl.col("bonus") < 1000) | (pl.col("bonus").is_null()))
        .select(["name", "bonus"])
        .collect()
    )

    return result_df


result = employee_bonus(employee, bonus)
print(result)
