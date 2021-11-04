# streamlit_app.py

import streamlit as st
from gsheetsdb import connect

# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows

sheet_url = st.secrets["https://docs.google.com/spreadsheets/d/1XBGtUKORl0QBaUXeshFhNAMj5tSbaDRyFUU9PaGtUIY/edit#gid=1393963821"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Print results.
for row in rows:
    st.write(f"{row.BA} has a :{row.Q1}:")
