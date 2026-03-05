import mysql.connector
import os
import pandas as pd

class DataBaseModel:
    
    def __init__(self, arquivo):
        self.database = arquivo
        self.connector = self.obter_connector()
        self.cursor = self.connector.cursor()

    def export_to_excel(self, nome):
        return self.mostrar_database().to_excel(f'{nome}.xlsx', sheet_name='DataBase', header=False)
    
    def exportar_excel_question(self):
        export = input('Exportar para Excel \n (1) Sim | (2) Não: ')
        if export == '1':
            name = input('Nome do arquivo: ')
            self.export_to_excel(name)
            print('Planilha exportada com sucesso')

    def mostrar_produto_especifico(self, ref):
        query = "SELECT * FROM produtos WHERE nome LIKE %s"
        return pd.read_sql(query, self.connector, params=(f"%{ref}%",))
    
    def obter_connector(self):
        return mysql.connector.connect(
            host = 'localhost',
            user = os.getenv('USER'),
            password = os.getenv('PASSWORD'),
            database = self.database
        )
            
    def add_produto(self):
        nome = input('Nome do produto: ')
        preco = int(input('Preço do produto: '))
        marca = input('Marca do produto: ')
        categoria = input('Categoria do produto: ')
        especificacoes = input('Especificações do produto: ')
        query = """
            INSERT INTO produtos (nome, preco, marca, categoria, especificacoes)
            VALUES (%s, %s, %s, %s, %s)
        """
        valores = (nome, preco, marca, categoria, especificacoes)
        self.cursor.execute(query, valores)
        self.connector.commit()
        self.cursor.close()
        print('Produto adicionado')


    def add_cliente_dados_pessoais(self,nome, preco, marca, categoria, especificacoes):
        query = """
            INSERT INTO produtos (nome, preco, marca, categoria, especificacoes)
            VALUES (%s, %s, %s, %s, %s)
        """
        valores = (nome, preco, marca, categoria, especificacoes)
        self.cursor.execute(query, valores)
        self.connector.commit()
        self.cursor.close()

    def add_venderproduto(self):
        export = input('Vender produto? \n (1) Sim | (2) Não: ')
        if export == '1':
            produto = input('ID do produto a ser vendido: ')
            nome_cliente = input('Nome do cliente: ')
            data_compra = input('Data da compra (DD/MM/AAAA): ')
            self.deletar_produto(produto)
            print('Produto vendido com sucesso, Cliente adicionado ao sistema')
            query = """
                INSERT INTO clientes_produtos (nome, produto, datacompra)
            VALUES (%s, %s, STR_TO_DATE(%s, '%d/%m/%y'))
            """
            valores = (nome_cliente, produto, data_compra)
            self.cursor.execute(query, valores)
            self.connector.commit()
            self.cursor.close()

    def deletar_produto(self, referencia):
            self.cursor.execute("SELECT * FROM produtos WHERE id = %s", (referencia))
            produto = self.cursor.fetchone()

            if produto:
                query = 'DELETE FROM produtos WHERE id = %s'
                self.cursor.execute(query, (referencia,))
                self.connector.commit()
                return(self.cursor.rowcount, 'produto removido')
            else:
                return f'Nenhum produto encontrado com o ID: {referencia}'
      
    def mostrar_database(self):
         return pd.read_sql('SELECT * from produtos', self.connector)
    
    def __del__(self):
         self.connector.close()
         print('Conexão encerrada')