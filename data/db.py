import sqlite3

class DB:

    def __init__(self):
        try:
            self.conn = sqlite3.connect('db.sqlite3')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(f'Erro ao conectar com o banco de dados: {e}')
            raise e
        
    def execute(self, sql):
        self.cursor.execute(sql)
        
    def commit(self):    
        self.conn.commit()
    
    def close(self):
        self.conn.close()
    
    def insert_aviao(self, capacidade_aviao, modelo_aviao):
        self.execute(f'''
            INSERT INTO aviao (capacidade, modelo) VALUES ({capacidade_aviao}, '{modelo_aviao}')
        ''')
        self.commit()
        return self.cursor.lastrowid
    
    def remove_aviao(self, id_aviao):
        self.execute(f'''
            DELETE FROM aviao WHERE id = {id_aviao}
        ''')
        self.commit()
    
    def insert_passageiro(self, nome, idade):
        self.execute(f'''
            INSERT INTO passageiro (nome, idade) VALUES ('{nome}', {idade})
        ''')
        self.commit()
        return self.cursor.lastrowid
    
    def update_passageiro(self, id_passageiro, id_reserva):
        self.execute(f'''
            UPDATE passageiro SET id_reserva = {id_reserva} WHERE id = {id_passageiro}
        ''')
        self.commit()
    
    def remove_passageiro(self, nome_pessoa):
        self.execute(f'''
            DELETE FROM passageiro WHERE nome = '{nome_pessoa}'
        ''')
        self.commit()
    
    def insert_piloto(self, nome, idade, numero_carteira):
        self.execute(f'''
            INSERT INTO piloto (nome, idade, numero_carteira) VALUES ('{nome}', {idade}, '{numero_carteira}')
        ''')
        self.commit()
        return self.cursor.lastrowid
    
    def update_piloto(self, id_piloto, id_voo):
        self.execute(f'''
            UPDATE piloto SET id_voo = {id_voo} WHERE id = {id_piloto}
        ''')
        self.commit()
    
    def remove_piloto(self, nome_pessoa):
        self.execute(f'''
            DELETE FROM piloto WHERE nome = '{nome_pessoa}'
        ''')
        self.commit()
    
        
    def create_tables(self):
        self.execute('''
            CREATE TABLE IF NOT EXISTS aviao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                capacidade INTEGER NOT NULL,
                modelo TEXT not NULL,
            )
        ''')
       
        self.execute('''
            CREATE TABLE IF NOT EXISTS passageiro (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                id_reserva INTEGER,
                FOREIGN KEY(id_reserva) REFERENCES reserva(id) ON DELETE SET NULL
            )
        ''')
        
        self.execute('''
            CREATE TABLE IF NOT EXISTS piloto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                numero_carteira TEXT NOT NULL,             
            )
        ''')
        
        self.commit()
        self.close()

if __name__ == '__main__':
    db = DB()
    db.create_tables()
    #db.load_data()