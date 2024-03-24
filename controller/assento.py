# ---------------------------------------------------------------#
# IMPORTS PARA SER VISIVEIS BIBLIOTECAS EXTERNAS DA PASTAR RAIZ
from sys import path
from pathlib import Path
SRC_PATH = Path(__file__).resolve().parent.parent
path.append(str(SRC_PATH))
# ---------------------------------------------------------------#

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
            self.assentos.append(Assento(id_assento, numero))
        db.close()
        
    def load(self, list_assentos):
        for assento in list_assentos:
            self.assentos.append(Assento(assento[0], assento[1], assento[2]))
        
    def get(self, id_assento):
        for assento in self.assentos:
            if assento.id == id_assento:
                return assento
        return None
        
    def update(self, assento, ocupado):
        db = DB()
        db.update_assento(assento.id, ocupado)
        db.close()
        assento.ocupado = ocupado
        
   
            