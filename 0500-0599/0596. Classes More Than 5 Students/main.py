import polars as pl

data = [
    ["A", "Math"],
    ["B", "English"],
    ["C", "Math"],
    ["D", "Biology"],
    ["E", "Math"],
    ["F", "Computer"],
    ["G", "Math"],
    ["H", "Math"],
    ["I", "Math"],
]
courses = pl.LazyFrame(
    data, schema={"student": pl.String, "class": pl.String}, orient="row"
)


def find_classes(courses: pl.LazyFrame) -> pl.DataFrame:
    result_df = (
        courses.group_by("class")
        .agg(pl.col("student").n_unique())
        .filter(pl.col("student") >= 5)
        .select("class")
        .collect()
    )

    return result_df


result = find_classes(courses)
print(result)
