

class Assento:
    def __init__(self, id, numero, id_aviao):
        self.id = id
        self.numero = numero
        self.ocupado = False
        self.id_aviao = id_aviao

    def __str__(self):
        return f'Assento: {self.numero} - Ocupado: {self.ocupado}'