from scipy.stats import shapiro


def check_normality(series):

    series = series.dropna()

    if len(series) < 3:
        return None

    if len(series) > 5000:
        series = series.sample(5000, random_state=42)

    statistic, p_value = shapiro(series)

    return {
        "Statistic": statistic,
        "P Value": p_value,
        "Normal": p_value > 0.05
    }
