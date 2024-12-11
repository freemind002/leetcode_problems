import polars as pl

employees_data = [
    [3, "Bob", "Operations", 48675],
    [90, "Alice", "Sales", 11096],
    [9, "Tatiana", "Engineering", 33805],
    [60, "Annabelle", "InformationTechnology", 37678],
    [49, "Jonathan", "HumanResources", 23793],
    [43, "Khaled", "Administration", 40454],
]
employees_schema = ["employee_id", "name", "department", "salary"]

lf = pl.LazyFrame(employees_data, employees_schema)


def selectFirstRows(employees: pl.LazyFrame) -> pl.DataFrame:
    result = employees.head(3).collect()

    return result


result = selectFirstRows(lf)
print(result)
