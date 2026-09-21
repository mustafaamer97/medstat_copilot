import pandas as pd
import streamlit as st

from core.data_loader import load_file
from core.profiler import profile_dataset
from core.normality import check_normality
from core.table1 import generate_table1
from core.effect_sizes import (
    mean_difference,
    risk_ratio,
    odds_ratio
)
from core.results_generator import generate_results_text
from core.statistical_methods import get_statistical_method
from core.word_exporter import create_word_report


st.set_page_config(
    page_title="MedStat Copilot",
    page_icon="📊",
    layout="wide"
)

st.title("MedStat Copilot")

uploaded_file = st.file_uploader(
    "Upload Excel or CSV File",
    type=["csv", "xlsx"]
)

if uploaded_file:

    df = load_file(uploaded_file)

    st.success("File loaded successfully")

    st.subheader("Data Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Summary")

    profile = profile_dataset(df)

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", profile["rows"])
    col2.metric("Columns", profile["columns"])
    col3.metric("Missing Values", profile["missing_values"])

    st.subheader("Table 1")

    table1 = generate_table1(df)

    st.dataframe(table1)

    st.subheader("Normality Test")

    numeric_columns = df.select_dtypes(
        include=["int64", "float64"]
    ).columns

    for column in numeric_columns:

        result = check_normality(df[column])

        if result:

            st.write(
                f"{column}: p = {result['p_value']:.4f}"
            )

    # ------------------ Statistical Analysis ------------------
    st.subheader("Statistical Analysis")

    columns = df.columns.tolist()

    outcome_variable = st.selectbox(
        "Outcome Variable",
        columns
    )

    group_variable = st.selectbox(
        "Group Variable",
        columns
    )

    if st.button("Run Analysis"):

        from core.statistical_tests import (
            run_numeric_test,
            run_categorical_test
        )

        if df[outcome_variable].dtype in [
            "int64",
            "float64"
        ]:

            result = run_numeric_test(
                df,
                outcome_variable,
                group_variable
            )

        else:

            result = run_categorical_test(
                df,
                outcome_variable,
                group_variable
            )

        if result:

            st.success("Analysis Completed")

            st.write(
                f"Test: {result['test']}"
            )

            st.write(
                f"Statistic: {result['statistic']:.4f}"
            )

            st.write(
                f"P-value: {result['p_value']:.4f}"
            )

            if result["test"] in [
                "Independent T-Test",
                "Mann-Whitney U"
            ]:

                groups = df[group_variable].dropna().unique()

                group1 = df[
                    df[group_variable] == groups[0]
                ][outcome_variable].dropna()

                group2 = df[
                    df[group_variable] == groups[1]
                ][outcome_variable].dropna()

                md = mean_difference(group1, group2)

                st.write(
                    f"Mean Difference: {md:.4f}"
                )

            elif result["test"] in [
                "Fisher Exact Test",
                "Chi-Square Test"
            ]:

                table = pd.crosstab(
                    df[group_variable],
                    df[outcome_variable]
                )

                if table.shape == (2, 2):

                    or_value = odds_ratio(table)
                    rr_value = risk_ratio(table)

                    if or_value is not None:
                        st.write(
                            f"Odds Ratio: {or_value:.4f}"
                        )

                    if rr_value is not None:
                        st.write(
                            f"Risk Ratio: {rr_value:.4f}"
                        )

            st.subheader("Results")

            results_text = generate_results_text(result)

            st.write(results_text)

            statistical_methods = get_statistical_method(
                result["test"]
            )

            st.subheader("Statistical Methods")

            st.write(statistical_methods)

            st.subheader("Export")

            document = create_word_report(
                uploaded_file.name,
                table1,
                results_text,
                statistical_methods
            )

            document.save("medstat_report.docx")

            with open("medstat_report.docx", "rb") as file:

                st.download_button(
                    label="Download Word Report",
                    data=file,
                    file_name="medstat_report.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
