from tableone import TableOne


def generate_table1(df):

    categorical = []

    continuous = []

    for col in df.columns:

        if df[col].dtype == "object":
            categorical.append(col)

        else:
            continuous.append(col)

    table = TableOne(
        df,
        columns=df.columns.tolist(),
        categorical=categorical
    )

    return table.tableone
