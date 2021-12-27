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


rows1 = conn.execute(f'SELECT * FROM "{sheet_url1}"')
df1 = pd.DataFrame(rows1)
st.title ("Ojas Target")

option = st.sidebar.selectbox('Select BA',df1.BA)
df1.set_index("BA", inplace = True)
result = df1.loc[[option]]
st.write( result)
#st.write( "sum : ", result.sum())

option1 = st.sidebar.selectbox('Select Qtr',("Q1","Q2","Q3","Q4") )
df2 = pd.DataFrame(rows1)
result1 = df2[["BA",option1]]
st.write( result1)
st.line_chart( pd.DataFrame([["BA",option1]]))

#Ojas_Target = st.sidebar.button('Ojas Target')
if st.sidebar.button('Ojas Target'):
    st.write(df1)
st.line_chart(df1)
#df4 = df2[["BA","Total"]]


# Print results.
#for row in rows:
#    st.write(f"{row.BA} has a :{row.Q1}:")
