def profile_dataset(df):

    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing": df.isna().sum().sum(),
    }
