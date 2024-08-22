from .db import DB

class VooDAO:
    def insert_voo(self, origem, destino, data, id_aviao, id_piloto):
        pass
    
    def remove_voo(self, id_voo):
        pass
    
    def get_all_voos(self):
        pass
    
    def get_voo(self, id_voo):
        pass
    
class VooDAOimp(DB, VooDAO):
    # Singleton, garate que só exista uma instancia dessa classe.
    __instance = None
    def __new__(cls):
        if VooDAOimp.__instance is None:
            VooDAOimp.__instance = super().__new__(cls)
        return VooDAOimp.__instance
    
    def __init__(self):
        super().__init__()
        
    def insert_voo(self, origem, destino, data, id_aviao, id_piloto):
        self.execute(f'''
            INSERT INTO voo (origem, destino, data, aviao_id, piloto_id) VALUES ('{origem}', '{destino}', '{data}', {id_aviao}, {id_piloto})
        ''')
        self.commit()
        return self.cursor.lastrowid
    
    def remove_voo(self, id_voo):
        self.execute(f'''
            DELETE FROM voo WHERE id = {id_voo}
        ''')
        self.commit()
        
    def get_all_voos(self):
        self.execute('SELECT * FROM voo')
        return self.cursor.fetchall()
    
    def get_voo(self, id_voo):
        self.execute(f'SELECT * FROM voo WHERE id = {id_voo}')
        return self.cursor.fetchone()