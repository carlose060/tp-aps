

class Aviao:
    def __init__(self, id, capacidade, assentos):
        self.id = id
        self.capacidade = capacidade
        self.assentos = assentos

    def __str__(self):
        return f'Avião: {self.id} - Capacidade: {self.capacidade}'
    
    def __dict__(self):
        return {
            'id': self.id,
            'capacidade': self.capacidade
        }