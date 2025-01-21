import pandas as pd
from sqlalchemy import create_engine

df=pd.read_excel("Online Retail.xlsx")

engine= create_engine()

connection_string = (
    "Driver={SQL Server};"
    "Server=your_server_name;"
    "Database=DataScienceDB;"  # Use the name of your new database
    "UID=your_username;"
    "PWD=your_password;"
)

conn = pyodbc.connect(connection_string)

df.to_sql('Customers',con=conn, if_exists='replace',index=False)

conn.close()