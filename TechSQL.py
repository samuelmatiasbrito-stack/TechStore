from database import DataBaseModel
databasemodel = DataBaseModel('tech_store')

while True:
    print(f'BASE DOS PRODUTOS TECH STORE')
    question = input('(1) Inserir Produto (2) Deletar Produto (3) Ver produtos específicos: ')
    if question == '1':
        nome = input('Nome do produto: ')
        preco = int(input('Preço do produto: '))
        marca = input('Marca do produto: ')
        categoria = input('Categoria do produto: ')
        especificacoes = input('Especificações do produto: ')
        databasemodel.add_produto(nome, preco, marca, categoria, especificacoes)
        print('Produto adicionado')
        print(databasemodel.mostrar_database())
        break

    elif question == '2':
        print(databasemodel.mostrar_database())
        referencia = int(input('ID do produto a ser deletado: '))
        print(databasemodel.deletar_produto(referencia))
        print(databasemodel.mostrar_database())
        print(databasemodel.exportar_excel_question())

    elif question == '3':
        print(databasemodel.mostrar_database())
        referencia = input('Nome do produto específico: ')
        print(databasemodel.mostrar_produto_especifico(referencia))
        print(databasemodel.exportar_excel_question())