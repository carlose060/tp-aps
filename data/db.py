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
    
    def update_assento(self, id_assento, ocupado):
        self.execute(f'''
            UPDATE assento SET ocupado = {ocupado} WHERE id = {id_assento}
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
            DELETE FROM passageiro WHERE nome = {nome_pessoa}
        ''')
        self.commit()
    
    def insert_piloto(self, nome, idade):
        self.execute(f'''
            INSERT INTO piloto (nome, idade) VALUES ('{nome}', {idade})
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
            DELETE FROM piloto WHERE nome = {nome_pessoa}
        ''')
        self.commit()
    
    def insert_voo(self, origem, destino, data, id_aviao, id_piloto):
        self.execute(f'''
            INSERT INTO voo (origem, destino, data, id_aviao, id_piloto) VALUES ('{origem}', '{destino}', '{data}', {id_aviao}, {id_piloto})
        ''')
        self.commit()
        return self.cursor.lastrowid
    
    def remove_voo(self, id_voo):
        self.execute(f'''
            DELETE FROM voo WHERE id = {id_voo}
        ''')
        self.commit()
    
    def insert_reserva(self, id_voo, id_assento):
        self.execute(f'''
            INSERT INTO reserva (id_voo, id_assento) VALUES ({id_voo}, {id_assento})
        ''')
        self.commit()
        return self.cursor.lastrowid
        
    
        
    def load_data(self, avioes, pessoas, voos, reservas):
        self.execute('''
            SELECT * FROM aviao
        ''')
        list_avioes = self.cursor.fetchall()
        for row in list_avioes:
            id_aviao, capacidade = row
            self.execute(f'''
                SELECT * FROM assento WHERE id_aviao = {id_aviao}
            ''')
            list_assentos = self.cursor.fetchall()
            avioes.load(id_aviao, capacidade, list_assentos)
        self.execute('''
            SELECT * FROM piloto
        ''')
        list_piloto = self.cursor.fetchall()
        for row in list_piloto:
            id_piloto, nome, idade, id_voo = row
            pessoa_carregada = pessoas.load_piloto(id_piloto, nome, idade)
            if id_voo:
                self.execute(f'''
                    SELECT * FROM voo WHERE id = {id_voo}
                ''')
                voo = self.cursor.fetchone()
                id_voo, origem, destino, data, id_aviao, id_piloto = voo
                aviao = avioes.get(id_aviao)
                voo = voos.load(id_voo, origem, destino, data, aviao, pessoa_carregada)
                pessoa_carregada.voo = voo
                self.execute(f'''
                    SELECT * FROM reserva WHERE id_voo = {id_voo}
                ''')
                reservas_voo = self.cursor.fetchall()
                for reserva in reservas_voo:
                    id_reserva, id_voo, id_assento = reserva
                    assento = avioes.assentos_controller.get(id_assento)
                    reservas.load(id_reserva, voo, assento)
        self.execute('''
            SELECT * FROM passageiro
        ''')
        passageiros = self.cursor.fetchall()
        for row in passageiros:
            id_passageiro, nome, idade, id_reserva = row
            reserva = None
            if id_reserva:
                reserva = reservas.get_with_id(id_reserva)
            pessoa_carregada = pessoas.load_passageiro(id_passageiro, nome, idade, reserva)
             
        self.close()
        
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
                id_reserva INTEGER,
                FOREIGN KEY(id_reserva) REFERENCES reserva(id) ON DELETE SET NULL
            )
        ''')
        self.execute('''
            CREATE TABLE IF NOT EXISTS voo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                origem TEXT NOT NULL,
                destino TEXT NOT NULL,
                data TEXT NOT NULL,
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
                id_voo INTEGER,
                FOREIGN KEY(id_voo) REFERENCES voo(id) ON DELETE SET NULL
            )
        ''')
       
        
        self.commit()
        self.close()

if __name__ == '__main__':
    db = DB()
    #db.create_tables()
    db.load_data()