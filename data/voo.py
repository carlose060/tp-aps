from .db import DB


class VooDB(DB):
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