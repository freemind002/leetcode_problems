from typing import List

import polars as pl

student_data = [[1, 15], [2, 11], [3, 11], [4, 20]]


def createDataframe(student_data: List[List[int]]) -> pl.DataFrame:
    result = pl.LazyFrame(student_data, schema=["student_id", "age"]).collect()

    return result


result = createDataframe(student_data)
print(result)
