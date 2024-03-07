from uuid import uuid4


class Reserva:
    def __init__(self, voo, assento):
        self.id = uuid4()
        self.voo = voo
        self.assento = assento
    
    def __str__(self):
        return f'Voo: {self.voo}, Assento: {self.assento.numero}'
    
    def __dict__(self):
        return {
            'id': self.id,
            'id_voo': self.voo.id,
            'assento': self.assento.__dict__,
            'id_aviao': self.id_aviao
        }
    
       