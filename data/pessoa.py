from .db import DB


class PessoaDB(DB):
    def __init__(self):
        super().__init__()
        
    
    def insert_passageiro(self, nome, idade):
        self.execute(f'''
            INSERT INTO passageiro (nome, idade) VALUES ('{nome}', {idade})
        ''')
        self.commit()
        return self.cursor.lastrowid
    
    
    def remove_passageiro(self, id):
        self.execute(f'''
            DELETE FROM passageiro WHERE id = {id}
        ''')
        self.commit()
    
    def get_passageiro_with_id(self, id):
        self.execute(f'''
            SELECT * FROM passageiro WHERE id = {id}
        ''')
        return self.cursor.fetchone()
        
    def get_piloto_with_id(self, id):
        self.execute(f'''
            SELECT * FROM piloto WHERE id = {id}
        ''')
        return self.cursor.fetchone()
    
    def insert_piloto(self, nome, idade, numero_carteira):
        self.execute(f'''
            INSERT INTO piloto (nome, idade, numero_carteira) VALUES ('{nome}', {idade}, '{numero_carteira}')
        ''')
        self.commit()
        return self.cursor.lastrowid

    
    def remove_piloto(self, id):
        self.execute(f'''
            DELETE FROM piloto WHERE id = {id}
        ''')
        self.commit()
    
    def get_all_pilotos(self):
        self.execute('SELECT * FROM piloto')
        return self.cursor.fetchall()
    
    def get_all_passageiros(self):
        self.execute('SELECT * FROM passageiro')
        return self.cursor.fetchall()
    
    def get_all_pessoas(self):
        self.execute('SELECT * FROM passageiro')
        passageiros = self.cursor.fetchall()
        todos_passageiros = [list(p) + ['Passageiro'] for p in passageiros]
        self.execute('SELECT * FROM piloto')
        pilotos = self.cursor.fetchall()
        todos_pilotos = [list(p) + ['Piloto'] for p in pilotos]
        return todos_passageiros + todos_pilotos
    
    def update_reserva_passageiro(self, id_passageiro, id_reserva):
        self.execute(f'''
            UPDATE passageiro SET reserva_id = {id_reserva} WHERE id = {id_passageiro}
        ''')
        self.commit()
        