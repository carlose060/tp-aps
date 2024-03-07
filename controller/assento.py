from sys import path
from pathlib import Path
SRC_PATH = Path(__file__).resolve().parent.parent
path.append(str(SRC_PATH))

from data.db import DB
from model.assento import Assento

class AssentoController:
    
    def __init__(self):
        self.assentos = []
    
    def add(self, quantidade, id_aviao):
        db = DB()
        
        for i in range(quantidade):
            numero = i + 1
            id_assento = db.insert_assento(numero, id_aviao)
            self.assentos.append(Assento(id_assento, numero, id_aviao))
        db.close()
        
   
            