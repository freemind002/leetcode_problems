import polars as pl

students_data = [
    [32, "Piper", 5],
    [217, None, 19],
    [779, "Georgia", 20],
    [849, "Willow", 14],
]
students_schema = ["student_id", "name", "age"]

lf = pl.LazyFrame(students_data, students_schema)


def dropMissingData(students: pl.LazyFrame) -> pl.DataFrame:
    result = students.drop_nulls(subset=["name"]).collect()

    return result


result = dropMissingData(lf)
print(result)
