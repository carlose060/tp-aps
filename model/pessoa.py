

class Pessoa:
    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade

    
class Passageiro(Pessoa):
    def __init__(self, id, nome, idade, reserva = None):
        super().__init__(id ,nome, idade)
        self.reserva = reserva
        

    def __str__(self):
        return f'Nome: {self.nome}, Reserva: {self.reserva}'
    

class Piloto(Pessoa):
    def __init__(self, id, nome, idade, voo = None):        
        super().__init__(id, nome, idade)
        self.voo = voo      

    def __str__(self):
        return f'Nome: {self.nome}, Avião: {self.voo}'
    
  