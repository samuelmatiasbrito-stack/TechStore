from database import DataBaseModel
databasemodel = DataBaseModel('tech_store')

while True:
    print(f'BASE DOS PRODUTOS TECH STORE \n {databasemodel.mostrar_database()}')
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
        referencia = int(input('Referência do produto a ser deletado: '))
        print(databasemodel.deletar_produto(referencia))
        print(databasemodel.mostrar_database())
        export = input('Exportar para Excel? \n (1) Sim (2) Não: ')
        if export == '1':
            name = input('Nome do arquivo: ')
            databasemodel.export_excel(name)
            print('Planilha exportada com sucesso')
            break
        elif export == '2':
            break
    elif question == '3':
        print(databasemodel.mostrar_database())
        ref = input('Referencia do produto específico: ')
        print(databasemodel.mostrar_produto_especifico(ref))