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
    
   
    
    
        
    def create_tables(self):
        self.execute('''
            CREATE TABLE IF NOT EXISTS aviao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                capacidade INTEGER NOT NULL,
                modelo TEXT not NULL
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
                numero_carteira TEXT NOT NULL             
            )
        ''')
        
        self.commit()
        self.close()

if __name__ == '__main__':
    db = DB()
    db.create_tables()