import mysql.connector
import os
import pandas as pd

class DataBaseModel:
    
    def __init__(self, arquivo):
        self.database = arquivo
        self.connector = self.obter_connector()
        self.cursor = self.connector.cursor()

    def export_excel(self, nome):
        return self.database.to_excel(f'{nome}.xlsx', sheet_name='DataBase', header=False)
    
    def obter_connector(self):
        return mysql.connector.connect(
            host = 'localhost',
            user = os.getenv('USER'),
            password = os.getenv('PASSWORD'),
            database = self.database
        )
            
    def add_produto(self,nome, preco, marca, categoria, especificacoes):
        query = """
            INSERT INTO produtos (nome, preco, marca, categoria, especificacoes)
            VALUES (%s, %s, %s, %s, %s)
        """
        valores = (nome, preco, marca, categoria, especificacoes)
        self.cursor.execute(query, valores)
        self.connector.commit()
        self.cursor.close()

    def deletar_produto(self, referencia):
            self.cursor.execute("SELECT * FROM produtos WHERE referencia = %s", (referencia,))
            produto = self.cursor.fetchone()

            if produto:
                print('Produto encontrado:', produto)

                query = 'DELETE FROM produtos WHERE referencia = %s'
                self.cursor.execute(query, (referencia,))
                self.cursor.commit()

                print(self.cursor.rowcount, 'produto removido')
            else:
                print('Nenhum produto encontrado com a referência:', referencia)
      
    def mostrar_database(self):
         return pd.read_sql('SELECT * from produtos', self.connector)
    
    def __del__(self):
         self.connector.close()
         print('Conexão encerrada')