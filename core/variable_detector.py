import pandas as pd


def detect_variable_type(series):

    unique_values = series.dropna().nunique()

    if pd.api.types.is_numeric_dtype(series):

        if unique_values <= 2:
            return "Binary"

        elif unique_values <= 10:
            return "Categorical"

        else:
            return "Continuous"

    return "Categorical"
