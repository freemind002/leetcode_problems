import polars as pl

data = [[1, "Abbot"], [2, "Doris"], [3, "Emerson"], [4, "Green"], [5, "Jeames"]]
seat = pl.LazyFrame(data, schema={"id": pl.Int64, "student": pl.String}, orient="row")


def exchange_seats(seat: pl.LazyFrame) -> pl.DataFrame:
    column_list = seat.collect().to_numpy().tolist()
    data = []
    for index in range(0, len(column_list), 2):
        tmp_list = column_list[index : index + 2]
        if len(tmp_list) == 2:
            tmp_list[0][1], tmp_list[1][1] = tmp_list[1][1], tmp_list[0][1]
        data += tmp_list

    result_df = pl.LazyFrame(
        data, schema={"id": pl.Int64, "student": pl.String}, orient="row"
    ).collect()

    return result_df


result = exchange_seats(seat)
print(result)
