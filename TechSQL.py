import mysql.connector
import pandas as pd
from database import DataBaseModel
with mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="tech_store"
) as sql_database:
    tech_store = pd.read_sql("SELECT * FROM produtos", sql_database)

databasemodel = DataBaseModel(tech_store)
print(tech_store)

opcao = input('Exportar para Excel? \n (1) Sim | (2) Não: ')
if opcao == '1':
    databaseexcelname = input('Nome do Arquivo: ')
    print('Exportando...')
    databasemodel.export_excel(databaseexcelname)