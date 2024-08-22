from .db import DB

class ReservaDAO:
    def select_all_reservas_from_voo(self, id_voo):
        pass
    
    def insert_reserva(self, reserva):
        pass
    
    def get_all(self):
        pass
    
    def remove(self, id):
        pass
class ReservaDAOimp(DB, ReservaDAO):
    
    
    # Singleton, garate que só exista uma instancia dessa classe.
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
    
    def insert_reserva(self, reserva):
        print(reserva.preco, reserva.voo.id, reserva.assento)
        self.execute(f'''
            INSERT INTO reserva (preco, voo_id, assento) VALUES ({reserva.preco}, {reserva.voo.id}, {reserva.assento})
        ''')
        self.commit()
        return self.cursor.lastrowid
    
    def get_all(self):
        self.execute('SELECT * FROM reserva')
        return self.cursor.fetchall()
    
    def remove(self, id):
        self.execute(f'DELETE FROM reserva WHERE id = {id}')
        self.commit()
        return True