from .db import DB

class ReservaDB(DB):
    
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