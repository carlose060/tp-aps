# ---------------------------------------------------------------#
# IMPORTS PARA SER VISIVEIS BIBLIOTECAS EXTERNAS DA PASTAR RAIZ
from sys import path
from pathlib import Path
SRC_PATH = Path(__file__).resolve().parent.parent
path.append(str(SRC_PATH))
# ---------------------------------------------------------------#

from data.db import DB
from model.aviao import Aviao



class AviaoController:


    def add(self, capacidade, modelo):
        aviao = Aviao(0, capacidade, modelo)
        db = DB()
        id_aviao = db.insert_aviao(aviao)
        db.close()
        aviao.id = id_aviao
        return True


    def get(self, id_aviao):
        for aviao in self.avioes:
            if str(aviao.id) == str(id_aviao):
                return aviao
        return None

    def get_all(self):
        db = DB()
        avioes = db.get_all_avioes()
       
        db.close()
        return [Aviao(aviao[0], aviao[1], aviao[2]) for aviao in avioes]
    
    
    def remove(self, id_aviao):
        db = DB()
        db.remove_aviao(id_aviao)
        db.close()
        return True
    

   