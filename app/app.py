import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gold Coast GP Intelligence", layout="wide")

st.title("🏥 Gold Coast GP Intelligence Tool")
st.markdown("**AI-powered data intelligence for General Practitioners in Gold Coast, Australia**")

# Load data
df = pd.read_csv("data/processed/gold_coast_gps_final.csv")

# Sidebar filters
st.sidebar.header("Filters")

gender_filter = st.sidebar.multiselect("Gender", options=df["gender"].unique(), default=df["gender"].unique())
specialty_filter = st.sidebar.multiselect("Specialty", options=df["specialty"].unique(), default=df["specialty"].unique())
practice_filter = st.sidebar.multiselect("Practice", options=df["practice"].unique(), default=df["practice"].unique())

# Apply filters
filtered_df = df[
    (df["gender"].isin(gender_filter)) &
    (df["specialty"].isin(specialty_filter)) &
    (df["practice"].isin(practice_filter))
]

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Doctors", len(filtered_df))
col2.metric("Practices", filtered_df["practice"].nunique())
col3.metric("Female Doctors", len(filtered_df[filtered_df["gender"] == "Female"]))

st.markdown("---")

# Show data
st.subheader("Doctor Directory")
st.dataframe(filtered_df[["name", "gender", "specialty", "practice", "summary"]], use_container_width=True)

# Insights
st.subheader("Quick Insights")
st.write(f"- Most common specialty: **{filtered_df['specialty'].mode()[0] if not filtered_df.empty else 'N/A'}**")
st.write(f"- Number of unique practices: **{filtered_df['practice'].nunique()}**")