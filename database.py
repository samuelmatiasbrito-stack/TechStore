class DataBaseModel:
    def __init__(self, arquivo):
        self.database = arquivo
    def export_excel(self, nome):
        self.database.to_excel(f'{nome}.xlsx', sheet_name='DataBase', header=False)
        
