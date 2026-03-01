from database import DataBaseModel
databasemodel = DataBaseModel('tech_store')
print(f'BASE DOS PRODUTOS TECH STORE \n {databasemodel.mostrar_database()}')
question = input('(1) Inserir Produto \n (2) Deletar Produto: ')
if question == '1':
    nome = input('Nome do produto: ')
    preco = int(input('Preço do produto: '))
    marca = input('Marca do produto: ')
    categoria = input('Categoria do produto: ')
    especificacoes = input('Especificações do produto: ')
    databasemodel.add_produto(nome, preco, marca, categoria, especificacoes)
    print('Produto adicionado')
print(databasemodel.mostrar_database())