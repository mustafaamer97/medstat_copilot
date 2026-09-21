from scipy.stats import shapiro


def check_normality(series):
    series = series.dropna()

    if len(series) < 3:
        return None

    statistic, p_value = shapiro(series)

    return {
        "statistic": statistic,
        "p_value": p_value
    }
