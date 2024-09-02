from .db import DB

class ReservaDAOimp(DB):
    
    
    # # Singleton, garate que só exista uma instancia dessa classe.
    __instance = None
    def __new__(cls):
        if ReservaDAOimp.__instance is None:
            ReservaDAOimp.__instance = super().__new__(cls)
        return ReservaDAOimp.__instance
    
    def __init__(self):
        super().__init__()
    
    def select_all_reservas_from_voo(self, id_voo):
        self.execute(f'SELECT * FROM reserva WHERE voo_id = {id_voo}')
        return self.cursor.fetchall()
    
    def insert(self, reserva):
        print(reserva.preco, reserva.voo.id, reserva.assento)
        self.execute(f'''
            INSERT INTO reserva (preco, voo_id, assento) VALUES ({reserva.preco}, {reserva.voo.id}, {reserva.assento})
        ''')
        self.commit()
        return self.cursor.lastrowid
    
    def remove(self, id):
        self.execute(f'DELETE FROM reserva WHERE id = {id}')
        self.commit()
        return True
    
    
    def get_with_id(self, id):
        self.execute(f'SELECT * FROM reserva WHERE id = {id}')
        return self.cursor.fetchone()
    
    def get_all(self):
        self.execute('SELECT * FROM reserva')
        return self.cursor.fetchall()
    