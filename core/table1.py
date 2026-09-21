from tableone import TableOne


def generate_table1(df):
    categorical = list(
        df.select_dtypes(include=["object"]).columns
    )

    table = TableOne(
        data=df,
        columns=df.columns.tolist(),
        categorical=categorical
    )

    return table.tableone
