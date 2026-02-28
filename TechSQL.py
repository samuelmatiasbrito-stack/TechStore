from database import DataBaseModel
databasemodel = DataBaseModel('tech_store')
print(f'BASE DOS PRODUTOS TECH STORE \n {databasemodel.mostrar_database()}')
inserir_produto = input('Inserir Produto? \n (1) Sim (2) Não: ')
if inserir_produto == '1':
    nome = input('Nome do produto: ')
    preco = int(input('Preço do produto: '))
    marca = input('Marca do produto: ')
    categoria = input('Categoria do produto: ')
    especificacoes = input('Especificações do produto: ')
    databasemodel.add_produto(nome, preco, marca, categoria, especificacoes)
    print('Produto adicionado')
print(databasemodel.mostrar_database())