from uuid import uuid4


class Pessoa:
    def __init__(self, nome, idade):
        self.id = uuid4()
        self.nome = nome
        self.idade = idade

    
class Passageiro(Pessoa):
    def __init__(self, nome, idade, id_reserva = None):
        super().__init__(nome, idade)
        self.id_reserva = id_reserva

    def __str__(self):
        return f'Nome: {self.nome}, Reserva: {self.reserva}'
    

class Piloto(Pessoa):
    def __init__(self, nome, idade, id_voo = None):
        super().__init__(nome, idade)
        self.id_voo = id_voo

    def __str__(self):
        return f'Nome: {self.nome}, Avião: {self.id_voo}'
    
  