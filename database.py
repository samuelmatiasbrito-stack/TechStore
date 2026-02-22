import mysql.connector
import json
import pandas as pd
with open("userpassword.json", "r") as locked:
    userpassword = json.load(locked)

class DataBaseModel:
    
    def __init__(self, arquivo):
        self.database = arquivo
        self.connector = self.obter_connector()

    def export_excel(self, nome):
        return self.database.to_excel(f'{nome}.xlsx', sheet_name='DataBase', header=False)
    
    def obter_connector(self):
            with open('userpassword.json', 'r') as locked:
                userpassword = json.load(locked)
                return mysql.connector.connect(
                    host = 'localhost',
                    user = userpassword['USER'],
                    password = userpassword['PASS'],
                    database = self.database
                )
            
    def add_produto(self,nome, preco, marca, categoria, especificacoes):
         pass
      
    def mostrar_database(self):
         return pd.read_sql('SELECT * from produtos', self.connector)
    
    def __del__(self):
         self.connector.close()
         print('Conexão encerrada')