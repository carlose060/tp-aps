

class Reserva:
    def __init__(self, id, voo, assento):
        self.id = id
        self.voo = voo
        self.assento = assento
    
    def __str__(self):
        return f'Voo: {self.voo}, Assento: {self.assento.numero}'
      
       