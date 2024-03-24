

class Assento:
    def __init__(self, id, numero, ocupado=False):
        self.id = id
        self.numero = numero
        self.ocupado = ocupado
        

    def __str__(self):
        return f'Assento: {self.numero} - Ocupado: {self.ocupado}'