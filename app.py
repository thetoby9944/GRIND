import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="GRIND.",
    page_icon="assets/grind_logo.png"
)

st.image("assets/grind_logo.svg")

df = pd.read_csv(
    r"https://docs.google.com/spreadsheets/d/1qS66r_5lfu6xgUGDaExV6gaMoZO62i-yczodugfvNdY/export?format=csv&gid=0"
)


for col in df.columns[:-1][::-1]:
    filter_by = st.multiselect(
        f"Filter by {col}",
        df[col].unique()
    )
    if len(filter_by):
        df = df[df[col].isin(filter_by)]
st.write("# ")
st.write("Your exercise of the day is:")

exercise_placeholder = st.empty()
exercise = df.sample().Exercise.values[0]
if st.button("⟳"):
    exercise = df.sample().Exercise.values[0]

exercise_placeholder.write(f"# {exercise}")
