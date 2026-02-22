
from database import DataBaseModel
databasemodel = DataBaseModel('tech_store')
print(databasemodel.mostrar_database())
print(databasemodel.mostrar_database())

#     print('DataBase carregada')
#     opcao = input('(1) Exportar para Excel \n (2) Adicionar novo produto \n (3) Conferir produto específico: ')
#     if opcao == '1':
#         databaseexcelname = input('Nome do Arquivo: ')
#         print('Exportando...')
#         databasemodel.export_excel(databaseexcelname)
#         pass
#     elif opcao == '2':
