

class Voo:
    def __init__(self, id, origem, destino, data, aviao, piloto):
        self.id = id
        self.origem = origem
        self.destino = destino
        self.data = data
        self.aviao = aviao
        self.piloto = piloto
  

    def __str__(self):
        return f'Origem: {self.origem}, Destino: {self.destino}, Data: {self.data}, Avião: {self.aviao}, Piloto: {self.piloto}'