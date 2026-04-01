# import sqlite3
# import pandas as pd

# conn = sqlite3.connect("sales.db")

# df = pd.read_csv("sales.csv")

# df.to_sql("Sales", conn, if_exists="replace", index=False)

# print("Database created!")
import sqlite3
import pandas as pd

# connect to database
conn = sqlite3.connect("sales.db")

# read CSV
df = pd.read_csv("sales.csv")

# create table in database
df.to_sql("Sales", conn, if_exists="replace", index=False)

print("Database created successfully!")