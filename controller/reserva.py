# ---------------------------------------------------------------#
# IMPORTS PARA SER VISIVEIS BIBLIOTECAS EXTERNAS DA PASTAR RAIZ
from sys import path
from pathlib import Path
SRC_PATH = Path(__file__).resolve().parent.parent
path.append(str(SRC_PATH))
# ---------------------------------------------------------------#

from data.db import DB
from model.reserva import Reserva

class ReservaController:

    def __init__(self):
        self.reservas = []
        
    def add(self, assentos, id_voo):
        db = DB()
        for assento in assentos:
            id_reserva = db.insert_reserva(id_voo, assento.id )
            reserva = Reserva(id_reserva, id_voo, assento.id)
            self.reservas.append(reserva)
        db.close()
    
    def get(self, id_assento, id_voo):
        for reserva in self.reservas:
            if int(reserva.assento) == int(id_assento) and int(reserva.voo) == int(id_voo):
                return reserva
        return None