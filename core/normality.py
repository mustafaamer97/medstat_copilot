from scipy.stats import shapiro

def test_normality(series):

    series = series.dropna()

    if len(series) < 3:
        return None

    stat, p = shapiro(series)

    return {
        "statistic": stat,
        "p_value": p,
        "normal": p > 0.05
    }
