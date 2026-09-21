def get_statistical_method(test_name):

    methods = {
        "Independent T-Test": (
            "Continuous variables were compared between two independent "
            "groups using an independent-samples t-test."
        ),
        "Mann-Whitney U": (
            "Continuous variables were compared between two independent "
            "groups using the Mann-Whitney U test."
        ),
        "Chi-Square Test": (
            "Categorical variables were compared using the chi-square test."
        ),
        "Fisher Exact Test": (
            "Categorical variables were compared using Fisher's exact test."
        )
    }

    return methods.get(
        test_name,
        "Statistical analysis was performed using an appropriate statistical test."
    )
