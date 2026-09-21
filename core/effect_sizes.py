import math


def mean_difference(group1, group2):
    return group1.mean() - group2.mean()


def risk_ratio(table):
    a = table.iloc[0, 0]
    b = table.iloc[0, 1]
    c = table.iloc[1, 0]
    d = table.iloc[1, 1]

    risk1 = a / (a + b)
    risk2 = c / (c + d)

    if risk2 == 0:
        return None

    return risk1 / risk2


def odds_ratio(table):
    a = table.iloc[0, 0]
    b = table.iloc[0, 1]
    c = table.iloc[1, 0]
    d = table.iloc[1, 1]

    if b == 0 or c == 0:
        return None

    return (a * d) / (b * c)
