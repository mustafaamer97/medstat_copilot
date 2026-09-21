from tableone import TableOne

def create_table1(df):

    categorical = list(
        df.select_dtypes(include=["object"]).columns
    )

    continuous = list(
        df.select_dtypes(include=["int64", "float64"]).columns
    )

    table = TableOne(
        data=df,
        categorical=categorical,
        columns=categorical + continuous
    )

    return table
