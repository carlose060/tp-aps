

class Pessoa:
    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade

    
class Passageiro(Pessoa):
    def __init__(self, id, nome, idade):
        super().__init__(id ,nome, idade)
        

class Piloto(Pessoa):
    def __init__(self, id, nome, idade, numero_carteira):        
        super().__init__(id, nome, idade)
        self.numero_carteira = numero_carteira      


    
  