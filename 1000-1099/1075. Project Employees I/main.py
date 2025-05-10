import polars as pl

data = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]
project = pl.LazyFrame(
    data, schema={"project_id": pl.Int64, "employee_id": pl.Int64}, orient="row"
)
data = [[1, "Khaled", 3], [2, "Ali", 2], [3, "John", 1], [4, "Doe", 2]]
employee = pl.LazyFrame(
    data,
    schema={"employee_id": pl.Int64, "name": pl.String, "experience_years": pl.Int64},
    orient="row",
)


def project_employees_i(project: pl.LazyFrame, employee: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        project.join(employee, on="employee_id", how="left")
        .group_by("project_id")
        .agg(average_years=pl.col("experience_years").mean().round(2))
        .sort("average_years")
        .collect()
    )

    return result_df


result = project_employees_i(project, employee)
print(result)
