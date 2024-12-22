import polars as pl

students_data = [
    [1, "Mason", "King", 6],
    [2, "Ava", "Wright", 7],
    [3, "Taylor", "Hall", 16],
    [4, "Georgia", "Thompson", 18],
    [5, "Thomas", "Moore", 10],
]
students_schema = ["id", "first", "last", "age"]

lf = pl.LazyFrame(students_data, students_schema)


def renameColumns(students: pl.LazyFrame) -> pl.DataFrame:
    result = students.rename(
        {
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years",
        }
    ).collect()

    return result


result = renameColumns(lf)
print(result)
