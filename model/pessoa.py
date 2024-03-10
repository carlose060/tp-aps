

class Pessoa:
    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade

    
class Passageiro(Pessoa):
    def __init__(self, id, nome, idade, id_reserva = None):
        super().__init__(id ,nome, idade)
        self.id_reserva = id_reserva
        

    def __str__(self):
        return f'Nome: {self.nome}, Reserva: {self.reserva}'
    

class Piloto(Pessoa):
    def __init__(self, id, nome, idade):
        super().__init__(id, nome, idade)
        self.id_voo = None       

    def __str__(self):
        return f'Nome: {self.nome}, Avião: {self.id_voo}'
    
  