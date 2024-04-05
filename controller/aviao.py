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
        db = DB()
        id_aviao = db.insert_aviao(capacidade)
        db.close()
               
        aviao = Aviao(id_aviao, capacidade, modelo)

        return aviao


    def get(self, id_aviao):
        for aviao in self.avioes:
            if str(aviao.id) == str(id_aviao):
                return aviao
        return None

    def get_all(self):
        return [str(av.id) for av in self.avioes]
    

   