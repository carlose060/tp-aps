from model.reserva import Reserva
from data.reserva import ReservaDAOimp
from .voo import VooController

from .voo import VooController


class ReservaController:
    
    
    def add(self, preco,  id_voo, assento):
        voo = VooController().get(id_voo)
        reserva = Reserva(0, int(assento), voo, str(preco))
        db = ReservaDAOimp()
        id_reserva = db.insert_reserva(reserva)
        reserva.id = id_reserva
        db.close()
        return reserva
        
    def get_assentos_disponiveis(self, id_voo):
        voo = VooController().get(id_voo)
        qtd_assentos = voo.aviao.capacidade
        db = ReservaDAOimp()
        reservas = db.select_all_reservas_from_voo(id_voo)
        db.close()
        assentos_livre = [f'{i}' for i in range(1, qtd_assentos+1)]
        for reserva in reservas:
           assentos_livre.remove(str(reserva[3]))
            
        return assentos_livre 
    
    def get_all(self):
        db = ReservaDAOimp()
        reservas = db.get_all()
        db.close()
        return [Reserva(r[0],  r[3], VooController().get(r[2]),  r[1]) for r in reservas]
    
    def remove(self, id):
        db = ReservaDAOimp()
        db.remove(id)
        db.close()
        return True