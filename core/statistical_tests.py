from scipy.stats import (
    ttest_ind,
    mannwhitneyu,
    chi2_contingency,
    fisher_exact,
    shapiro
)

import pandas as pd


def is_normal(series):
    series = series.dropna()

    if len(series) < 3:
        return False

    _, p = shapiro(series)

    return p > 0.05


def run_numeric_test(df, outcome, group):

    groups = df[group].dropna().unique()

    if len(groups) != 2:
        return None

    g1 = df[df[group] == groups[0]][outcome].dropna()
    g2 = df[df[group] == groups[1]][outcome].dropna()

    normal = is_normal(g1) and is_normal(g2)

    if normal:

        statistic, p_value = ttest_ind(
            g1,
            g2,
            nan_policy="omit"
        )

        return {
            "test": "Independent T-Test",
            "statistic": statistic,
            "p_value": p_value
        }

    statistic, p_value = mannwhitneyu(
        g1,
        g2
    )

    return {
        "test": "Mann-Whitney U",
        "statistic": statistic,
        "p_value": p_value
    }


def run_categorical_test(df, outcome, group):

    table = pd.crosstab(
        df[group],
        df[outcome]
    )

    if table.shape == (2, 2):

        statistic, p_value = fisher_exact(table)

        return {
            "test": "Fisher Exact Test",
            "statistic": statistic,
            "p_value": p_value
        }

    statistic, p_value, _, _ = chi2_contingency(table)

    return {
        "test": "Chi-Square Test",
        "statistic": statistic,
        "p_value": p_value
    }
