import sqlite3
from pathlib import Path
class DB:

     # Singleton, garate que só exista uma instancia dessa classe.
    __instance = None
    def __new__(cls):
        if DB.__instance is None:
            DB.__instance = super().__new__(cls)
        return DB.__instance
    
    def __init__(self):
        try:
            self.conn = sqlite3.connect(str(Path.home()) + f'/Documentos/tp-aps/db.sqlite3')
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
                reserva_id INTEGER DEFAULT(NULL),
                FOREIGN KEY (reserva_id) REFERENCES reserva(id) ON DELETE SET NULL
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
        self.execute('''
            CREATE TABLE IF NOT EXISTS voo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                origem TEXT NOT NULL,
                destino TEXT NOT NULL,
                data TEXT NOT NULL,
                aviao_id INTEGER NOT NULL,
                piloto_id INTEGER NOT NULL,
                FOREIGN KEY (aviao_id) REFERENCES aviao(id) ON DELETE CASCADE,
                FOREIGN KEY (piloto_id) REFERENCES piloto(id) ON DELETE CASCADE
            )
        ''')
        self.execute('''
            CREATE TABLE IF NOT EXISTS reserva (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                preco TEXT NOT NULL,
                voo_id INTEGER NOT NULL,
                assento INTEGER NOT NULL,
                FOREIGN KEY (voo_id) REFERENCES voo(id) ON DELETE SET NULL
            )
        ''')
        self.commit()
        self.close()

if __name__ == '__main__':
    db = DB()
    db.create_tables()