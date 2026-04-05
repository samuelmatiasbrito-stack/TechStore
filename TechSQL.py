from database import DataBaseModel
databasemodel = DataBaseModel('tech_store')

while True:
    print(f'BASE DOS PRODUTOS TECH STORE')
    question = input('(1) Inserir Produto (2) Deletar Produto (3) Consultar produtos específicos (4) Exportar histórico de vendas: ')
    if question == '1':
        databasemodel.add_produto()
        print(databasemodel.mostrar_database())
        break

    elif question == '2':
        print(databasemodel.mostrar_database())
        print(databasemodel.deletar_produto())
        print(databasemodel.mostrar_database())
        print(databasemodel.exportar_excel_question())

    elif question == '3':
        print(databasemodel.mostrar_produto_especifico())
        print(databasemodel.venderproduto())
        print(databasemodel.exportar_excel_question())

    elif question == '4':
        print(databasemodel.exportar_vendas_excel())