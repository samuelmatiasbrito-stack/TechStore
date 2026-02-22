import mysql.connector
import pandas as pd
with mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    database="tech_store"
) as Sql_Arquivo:
    TechStore = pd.read_sql("SELECT * FROM produtos", Sql_Arquivo)

print(TechStore)
