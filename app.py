import streamlit as st
import pandas as pd

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
    "Upload Dataset",
    type=["csv", "xlsx"]
)

if uploaded_file:

    df = load_file(uploaded_file)

    st.success("Dataset Loaded Successfully")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Shape")

    col1, col2 = st.columns(2)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])

    st.subheader("Variable Summary")

    profile = profile_dataset(df)

    st.dataframe(profile)

    st.subheader("Table 1")

    table1 = generate_table1(df)

    st.dataframe(table1)

    st.subheader("Normality Testing")

    numeric_cols = df.select_dtypes(
        include=["int64", "float64"]
    ).columns

    for col in numeric_cols:

        result = check_normality(df[col])

        if result:

            status = (
                "Normal"
                if result["Normal"]
                else "Non-Normal"
            )

            st.write(
                f"{col}: "
                f"p={result['P Value']:.4f} "
                f"→ {status}"
            )
