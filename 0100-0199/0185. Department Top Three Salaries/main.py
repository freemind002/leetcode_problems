import polars as pl

data = [
    [1, "Joe", 85000, 1],
    [2, "Henry", 80000, 2],
    [3, "Sam", 60000, 2],
    [4, "Max", 90000, 1],
    [5, "Janet", 69000, 1],
    [6, "Randy", 85000, 1],
    [7, "Will", 70000, 1],
]
employee = pl.LazyFrame(
    data,
    schema={
        "id": pl.Int64,
        "name": pl.String,
        "salary": pl.Int64,
        "departmentId": pl.Int64,
    },
    orient="row",
)
data = [[1, "IT"], [2, "Sales"]]
department = pl.LazyFrame(
    data, schema={"id": pl.Int64, "name": pl.String}, orient="row"
)


def top_three_salaries(
    employee: pl.LazyFrame, department: pl.LazyFrame
) -> pl.DataFrame:
    result_df = (
        employee.join(
            employee.group_by("departmentId")
            .agg(pl.col("salary").unique().sort().tail(3))
            .explode("salary"),
            on=["departmentId", "salary"],
        )
        .join(
            department.rename({"id": "departmentId", "name": "Department"}),
            on="departmentId",
        )
        .select("Department", Employee=pl.col("name"), Salary=pl.col("salary"))
        .sort(["Department", "Salary"], descending=[False, True])
        .collect()
    )

    return result_df


result = top_three_salaries(employee, department)
print(result)
