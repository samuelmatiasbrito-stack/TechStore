import mysql.connector
import json
import pandas as pd
from database import DataBaseModel

with open("userpassword.json", "r") as locked:
    userpassword = json.load(locked)

with mysql.connector.connect(
    host="localhost",
    user=userpassword['USER'],
    password=userpassword['PASS'],
    database="tech_store"
) as sql_database:
    tech_store = pd.read_sql("SELECT * FROM produtos", sql_database)

databasemodel = DataBaseModel(tech_store)
print(tech_store)
while True:
    print('DataBase carregada')
    opcao = input('(1) Exportar para Excel \n (2) \n Adicionar novo produto \n (3) Conferir produto específico: ')
    if opcao == '1':
        databaseexcelname = input('Nome do Arquivo: ')
        print('Exportando...')
        databasemodel.export_excel(databaseexcelname)
        pass
    elif opcao == '2':