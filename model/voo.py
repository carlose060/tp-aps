from uuid import uuid4


class Voo:
    def __init__(self, origem, destino, data, hora, id_aviao, piloto):
        self.id = uuid4()
        self.origem = origem
        self.destino = destino
        self.data = data
        self.hora = hora
        self.id_aviao = id_aviao
        self.piloto = piloto
  

    def __str__(self):
        return f'Origem: {self.origem}, Destino: {self.destino}, Data: {self.data}, Hora: {self.hora}, Avião: {self.id_aviao}, Piloto: {self.piloto}'