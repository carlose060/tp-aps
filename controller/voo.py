# ---------------------------------------------------------------#
# IMPORTS PARA SER VISIVEIS BIBLIOTECAS EXTERNAS DA PASTAR RAIZ
from sys import path
from pathlib import Path
SRC_PATH = Path(__file__).resolve().parent.parent
path.append(str(SRC_PATH))
# ---------------------------------------------------------------#

from data.db import DB
from model.voo import Voo


class VooController:
    
    def __init__(self):
        self.voos = []
        
    def add(self, origem, destino, data, aviao, piloto):
        db = DB()
       
        id_voo = db.insert_voo(origem, destino, data, aviao.id, piloto.id)
        voo = Voo(id_voo, origem, destino, data, aviao, piloto)
        self.voos.append(voo)
        db.close()
        return voo
    
    def load(self, id_voo, origem, destino, data, aviao, piloto):
        voo = Voo(id_voo, origem, destino, data, aviao, piloto)
        self.voos.append(voo)
        return voo
    
    def get(self, id_voo):
        for voo in self.voos:
            if voo.id == int(id_voo):
                return voo
        return None
    
    def get_all(self):
        return [str(v.id)+f' | {v.origem} - {v.destino} - {v.data}' for v in self.voos]
    
    def remove(self, info_voo):
        id_voo, _ = info_voo.split(' | ')
        for voo in self.voos:
            if voo.id == id_voo:
                db = DB()
                db.remove_voo(id_voo)
                self.voos.remove(voo)
                db.close()
                return True
        return False