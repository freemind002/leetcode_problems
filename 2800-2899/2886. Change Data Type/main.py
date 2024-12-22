import polars as pl

students_data = [
    [1, "Ava", 6, 73.0],
    [2, "Kate", 15, 87.0],
]
students_schema = ["student_id", "name", "age", "grade"]

lf = pl.LazyFrame(students_data, students_schema)


def changeDatatype(students: pl.LazyFrame) -> pl.DataFrame:
    result = students.cast({"grade": pl.Int64}).collect()

    return result


result = changeDatatype(lf)
print(result)
