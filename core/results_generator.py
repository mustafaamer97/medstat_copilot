def generate_results_text(result):

    test = result["test"]
    statistic = result["statistic"]
    p_value = result["p_value"]

    significance = (
        "statistically significant"
        if p_value < 0.05
        else "not statistically significant"
    )

    return (
        f"A {test} was performed. "
        f"The test statistic was {statistic:.3f}, "
        f"with a p-value of {p_value:.4f}. "
        f"The observed difference was {significance}."
    )
