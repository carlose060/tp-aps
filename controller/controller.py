from .aviao import AviaoDAOimp
from .pessoa import PessoaDAOimp
from .voo import VooDAOimp
from .reserva import ReservaDAOimp

# Padrão de projeto strategy
class Controller:
    def __init__(self):
        self.strategy = None

   
        