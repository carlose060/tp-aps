from .db import DB
from model.pessoa import Passageiro, Piloto

class PessoaDAOimp(DB):
    
    # # Singleton, garate que só exista uma instancia dessa classe.
    __instance = None
    def __new__(cls):
        if PessoaDAOimp.__instance is None:
            PessoaDAOimp.__instance = super().__new__(cls)
        return PessoaDAOimp.__instance
    
    def __init__(self):
        super().__init__()
        
    
    def insert(self, pessoa):
        if type(pessoa) == Passageiro:   
            self.execute(f'''
                INSERT INTO passageiro (nome, idade) VALUES ('{pessoa.nome}', {pessoa.idade})
            ''')
        elif type(pessoa) == Piloto:
            self.execute(f'''
                INSERT INTO piloto (nome, idade, numero_carteira) VALUES ('{pessoa.nome}', {pessoa.idade}, '{pessoa.numero_carteira}')
            ''')
        else: 
            raise Exception('Tipo de pessoa inválido')
        self.commit()
        return self.cursor.lastrowid
    
    def remove(self, id, type):
        if type == 'Passageiro':
            self.execute(f'''
                DELETE FROM passageiro WHERE id = {id}
            ''')
        elif type == 'Piloto':
            self.execute(f'''
                DELETE FROM piloto WHERE id = {id}
            ''')
        else:
            raise Exception('Tipo de pessoa inválido')
        self.commit()
        
    
    def get_with_id(self, id, type):
        if type == 'Passageiro':
            self.execute(f'''
                SELECT * FROM passageiro WHERE id = {id}
            ''')
        elif type == 'Piloto':
            self.execute(f'''
                SELECT * FROM piloto WHERE id = {id}
            ''')
        else:
            raise Exception('Tipo de pessoa inválido')
        return self.cursor.fetchone()
    
    def get_all(self):
        self.execute('SELECT * FROM passageiro')
        passageiros = self.cursor.fetchall()
        todos_passageiros = [list(p) + ['Passageiro'] for p in passageiros]
        self.execute('SELECT * FROM piloto')
        pilotos = self.cursor.fetchall()
        todos_pilotos = [list(p) + ['Piloto'] for p in pilotos]
        return todos_passageiros + todos_pilotos
    
    def get_all_pilotos(self):
        self.execute('SELECT * FROM piloto')
        return self.cursor.fetchall()
    
    def get_all_passageiros(self):
        self.execute('SELECT * FROM passageiro')
        return self.cursor.fetchall()
     
    def update_reserva_passageiro(self, id_passageiro, id_reserva):
        self.execute(f'''
            UPDATE passageiro SET reserva_id = {id_reserva} WHERE id = {id_passageiro}
        ''')
        self.commit()
        