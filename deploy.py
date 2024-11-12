import streamlit as st
import pymysql
import mysql.connector
import pandas as pd



st.write("敲代码好好玩 哈哈哈...")
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '0531',  # Replace with your password
    database = 'study_content_db'
)

print("connected")

cursor = connection.cursor()

cursor.execute("SELECT * FROM TEXTBOOK_QUESTIONs")
data = cursor.fetchall()

df = pd.DataFrame(data)
st.dataframe(df)