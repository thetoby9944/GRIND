import streamlit as st
import pandas as pd
from footer import footer

st.set_page_config(
    page_title="GRIND.",
    page_icon="assets/grind_icon.png"
)

st.image("assets/grind_logo.svg")
st.write("# ")
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

exercise = df.sample().Exercise.values[0]
if st.button("⟳"):
    exercise = df.sample().Exercise.values[0]

st.write(f"# {exercise}")
st.write("# ")
st.write("# ")
st.write("Made with ❤️by [@PostPandemicPump](https://www.instagram.com/postpandemicpump/)")
footer()
