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
        res = self.cursor.execute(sql)
        return res.fetchall()
        
    def commit(self):    
        self.conn.commit()
    
    def close(self):
        self.conn.close()
    
    def insert_aviao(self, capacidade_aviao):
        self.execute(f'''
            INSERT INTO aviao (capacidade) VALUES ({capacidade_aviao})
        ''')
        self.commit()
        return self.cursor.lastrowid
    
    def remove_aviao(self, id_aviao):
        self.execute(f'''
            DELETE FROM aviao WHERE id = {id_aviao}
        ''')
        self.commit()
    
    def insert_assento(self, numero, id_aviao):
        self.execute(f'''
            INSERT INTO assento (numero, id_aviao) VALUES ({numero}, {id_aviao})
        ''')
        self.commit()
        return self.cursor.lastrowid
    
        
        
    def create_tables(self):
        self.execute('''
            CREATE TABLE IF NOT EXISTS aviao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                capacidade INTEGER NOT NULL
            )
        ''')
        self.execute('''
            CREATE TABLE IF NOT EXISTS assento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero INTEGER NOT NULL,
                ocupado BOOLEAN NOT NULL DEFAULT FALSE,
                id_aviao INTEGER NOT NULL,
                FOREIGN KEY(id_aviao) REFERENCES aviao(id) ON DELETE CASCADE
            )
        ''')
        self.execute('''
            CREATE TABLE IF NOT EXISTS reserva (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_voo INTEGER NOT NULL,
                id_assento INTEGER NOT NULL,
                FOREIGN KEY(id_voo) REFERENCES voo(id) ON DELETE CASCADE,
                FOREIGN KEY(id_assento) REFERENCES assento(id) ON DELETE CASCADE
            )
        ''')
        self.execute('''
            CREATE TABLE IF NOT EXISTS passageiro (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                id_reserva INTEGER NOT NULL,
                FOREIGN KEY(id_reserva) REFERENCES reserva(id) ON DELETE SET NULL
            )
        ''')
        self.execute('''
            CREATE TABLE IF NOT EXISTS voo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                origem TEXT NOT NULL,
                destino TEXT NOT NULL,
                data TEXT NOT NULL,
                aviao_id INTEGER NOT NULL,
                id_aviao INTEGER NOT NULL,
                id_piloto INTEGER NOT NULL,
                FOREIGN KEY(id_aviao) REFERENCES aviao(id) ON DELETE SET NULL
                FOREIGN KEY(id_piloto) REFERENCES piloto(id) ON DELETE SET NULL
            )
        ''')
        self.execute('''
            CREATE TABLE IF NOT EXISTS piloto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                id_voo INTEGER NOT NULL,
                FOREIGN KEY(id_voo) REFERENCES voo(id) ON DELETE SET NULL
            )
        ''')
       
        
        self.commit()
        self.close()

if __name__ == '__main__':
    db = DB()
    db.create_tables()
    