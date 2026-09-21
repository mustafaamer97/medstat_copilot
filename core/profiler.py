from core.variable_detector import detect_variable_type


def profile_dataset(df):

    variables = []

    for col in df.columns:

        variables.append({
            "Variable": col,
            "Type": detect_variable_type(df[col]),
            "Missing": int(df[col].isna().sum()),
            "Unique Values": int(df[col].nunique())
        })

    return variables
