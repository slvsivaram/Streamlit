# streamlit_app.py

import streamlit as st
import pandas as pd
# gsheetsdb
from gsheetsdb import connect

# Create a connection object.


# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
#def run_query(query):
#    rows = conn.execute(query, headers=1)
#    return rows
conn = connect()
sheet_url = "https://docs.google.com/spreadsheets/d/1XBGtUKORl0QBaUXeshFhNAMj5tSbaDRyFUU9PaGtUIY/edit#gid=882222373"


rows = conn.execute(f'SELECT * FROM "{sheet_url}"')
df = pd.DataFrame(rows)
st.title ("RE BE")

st.write(df)

sheet_url1 = "https://docs.google.com/spreadsheets/d/1XBGtUKORl0QBaUXeshFhNAMj5tSbaDRyFUU9PaGtUIY/edit#gid=1393963821"


rows = conn.execute(f'SELECT * FROM "{sheet_url1}"')
df1 = pd.DataFrame(rows)
st.title ("Ojas Target")
option = st.sidebar.selectbox('Select SSA',df1.BA)
st.write( 'selected',df1.iloc[option])
st.write(df1)

# Print results.
#for row in rows:
#    st.write(f"{row.BA} has a :{row.Q1}:")
