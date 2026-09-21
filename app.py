import streamlit as st
import pandas as pd

from core.data_loader import load_file
from core.data_profiler import profile_dataset
from core.table1_generator import create_table1
from core.normality import test_normality

st.set_page_config(
    page_title="MedStat Copilot",
    page_icon="📊",
    layout="wide"
)

st.title("MedStat Copilot")

uploaded_file = st.file_uploader(
    "Upload Excel or CSV",
    type=["csv", "xlsx"]
)

if uploaded_file:

    df = load_file(uploaded_file)

    st.success("Dataset loaded successfully")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    profile = profile_dataset(df)

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", profile["rows"])
    col2.metric("Columns", profile["columns"])
    col3.metric("Missing Values", profile["missing"])

    st.divider()

    st.subheader("Table 1")

    table1 = create_table1(df)

    st.dataframe(table1.tableone)

    st.divider()

    st.subheader("Normality Testing")

    numeric_cols = df.select_dtypes(
        include=["int64", "float64"]
    ).columns

    for col in numeric_cols:

        result = test_normality(df[col])

        if result:

            st.write(
                f"**{col}** "
                f"(p={result['p_value']:.4f}) "
                f"→ {'Normal' if result['normal'] else 'Non-Normal'}"
            )
