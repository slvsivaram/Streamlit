# streamlit_app.py

import streamlit as st
import pandas as pd
# gsheetsdb
from gsheetdb import connect

# Create a connection object.


# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
#def run_query(query):
#    rows = conn.execute(query, headers=1)
#    return rows

sheet_url = "https://docs.google.com/spreadsheets/d/1XBGtUKORl0QBaUXeshFhNAMj5tSbaDRyFUU9PaGtUIY/edit?usp=sharing"

conn = connect()

rows = conn.execute(f'SELECT * FROM "{sheet_url}"')
df = pd.DataFrame(rows)
st.write(df)

# Print results.
#for row in rows:
#    st.write(f"{row.BA} has a :{row.Q1}:")
