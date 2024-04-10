from db import DB


class AviaoDB(DB):
    def __init__(self):
        super().__init__()
    
    def insert_aviao(self, aviao):
        self.execute(f'''
            INSERT INTO aviao (capacidade, modelo) VALUES ({aviao.capacidade}, '{aviao.modelo}')
        ''')
        self.commit()
        return self.cursor.lastrowid
    
    def remove_aviao(self, id_aviao):
        self.execute(f'''
            DELETE FROM aviao WHERE id = {id_aviao}
        ''')
        self.commit()
    
    def get_all_avioes(self):
        self.execute('SELECT * FROM aviao')
        return self.cursor.fetchall()