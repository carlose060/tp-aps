from sys import path
from pathlib import Path
SRC_PATH = Path(__file__).resolve().parent.parent
path.append(str(SRC_PATH))

from data.db import DB
from model.aviao import Aviao
from controller.assento import AssentoController


class AviaoController:
    def __init__(self):
        self.avioes = []

    def add(self, capacidade):
        db = DB()
        id_aviao = db.insert_aviao(capacidade)
        db.close()
        assentos_controller = AssentoController()
        assentos_controller.add(capacidade, id_aviao)
        
        aviao = Aviao(id_aviao, capacidade, assentos_controller.assentos)
        self.avioes.append(aviao)
        return aviao

    def get(self, id_aviao):
        for aviao in self.avioes:
            if str(aviao.id) == id_aviao:
                return aviao
        return None

    def get_all(self):
        return [str(av.id) for av in self.avioes]
    
    def remove(self, id_aviao):
        for aviao in self.avioes:
            if str(aviao.id) == id_aviao:
                self.avioes.remove(aviao)
                db = DB()
                db.remove_aviao(id_aviao)
                db.close()
                return True
        return False

   