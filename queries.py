import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect('match_data.db')

df = pd.read_sql_query("SELECT * FROM match_data", conn)

conn.close()