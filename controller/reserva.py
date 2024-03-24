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
        
    def add(self, assentos, voo):
        db = DB()
        for assento in assentos:
            id_reserva = db.insert_reserva(voo.id, assento.id )
            reserva = Reserva(id_reserva, voo, assento)
            self.reservas.append(reserva)
        db.close()
    
    def load(self, id_reserva, voo, assento):
        reserva = Reserva(id_reserva, voo, assento)
        self.reservas.append(reserva)
        return reserva
    
    def get(self, id_assento, id_voo):
        for reserva in self.reservas:
            if int(reserva.assento.id) == int(id_assento) and int(reserva.voo.id) == int(id_voo):
                return reserva
        return None
    
    def get_with_id(self, id_reserva):
        for reserva in self.reservas:
            if reserva.id == int(id_reserva):
                return reserva
        return None