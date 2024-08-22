from .db import DB

class AviaoDAO:
    def insert_aviao(self, aviao):
        pass
    
    def remove_aviao(self, id_aviao):
        pass
    
    def get_aviao_with_id(self, id_aviao):
        pass
    
    def get_all_avioes(self):
        pass

class AviaoDAOimp(DB, AviaoDAO):
    
    # Singleton, garate que só exista uma instancia dessa classe.
    __instance = None
    def __new__(cls):
        if AviaoDAOimp.__instance is None:
            AviaoDAOimp.__instance = super().__new__(cls)
        return AviaoDAOimp.__instance
    
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
        
    def get_aviao_with_id(self, id_aviao):
        self.execute(f'''
            SELECT * FROM aviao WHERE id = {id_aviao}
        ''')
        return self.cursor.fetchone()
    
    def get_all_avioes(self):
        self.execute('SELECT * FROM aviao')
        return self.cursor.fetchall()