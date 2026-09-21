import streamlit as st

from core.data_loader import load_file
from core.profiler import profile_dataset
from core.normality import check_normality
from core.table1 import generate_table1


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
