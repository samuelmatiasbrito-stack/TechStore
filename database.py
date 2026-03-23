from weakref import ref

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

    def mostrar_produto_especifico(self):
        produto = input('Nome do produto específico: ')
        if produto:
            query = f"SELECT * FROM produtos WHERE produto LIKE '%{produto}%'"
            pdread = pd.read_sql(query, self.obter_connector())
            
            if pdread.empty:
                print("Produto não encontrado")
                return self.mostrar_produto_especifico()

            else:
                return pdread
        else:
            print("Produto não encontrado")
            return self.mostrar_produto_especifico()            
        
    
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
            INSERT INTO produtos (produto, preco, marca, categoria, especificacoes)
            VALUES (%s, %s, %s, %s, %s)
        """
        valores = (nome, preco, marca, categoria, especificacoes)
        self.cursor.execute(query, valores)
        self.connector.commit()
        print('Produto adicionado')

    def add_cliente_dados_pessoais(self):
        nome_cliente = input('Nome do cliente: ')
        self.nomecliente = nome_cliente
        endereco = input('Endereço: ')
        contato = input('Contato: ')
        email = input('Email: ')
        query = """
            INSERT INTO clientes_informacoes (nome, endereco, contato, email)
            VALUES (%s, %s, %s, %s)
        """
        valores = (nome_cliente, endereco, contato, email)
        self.cursor.execute(query, valores)
        self.connector.commit()
        return self.cursor.lastrowid



    def venderproduto(self):
        export = input('Vender produto? \n (1) Sim | (2) Não: ')
        if export == '1':
            id_cliente = self.add_cliente_dados_pessoais()
            id_produto = input('ID do produto a ser vendido: ')
            query_checar_produto = "SELECT produto FROM produtos WHERE id_produto = %s"
            self.cursor.execute(query_checar_produto, (id_produto,))
            produto = self.cursor.fetchone()
            if not produto:
                print(f"Nenhum produto encontrado com o ID: {id_produto}")
                return   
            data_compra = input('Data da compra (DD/MM/AAAA): ')
            print('Produto vendido com sucesso')
            query = """
                INSERT INTO clientes_produtos (id_produto, id_cliente, data_compra)
                VALUES (%s, %s, STR_TO_DATE(%s, '%d/%m/%Y'))
            """
            valores = (id_produto, id_cliente, data_compra)
            self.cursor.execute(query, valores)
            self.connector.commit()
            print('Produto vendido com sucesso')


    def deletar_produto(self, referencia):
            self.cursor.execute("SELECT * FROM produtos WHERE id_produto = %s", (referencia))
            produto = self.cursor.fetchone()

            if produto:
                query = 'DELETE FROM produtos WHERE id.produto = %s'
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