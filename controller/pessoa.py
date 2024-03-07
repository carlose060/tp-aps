from sys import path
from pathlib import Path
SRC_PATH = Path(__file__).resolve().parent.parent
path.append(str(SRC_PATH))

from model.pessoa import Passageiro, Piloto

class PessoaController:
    def __init__(self):
        self.pessoas = []

    def add(self, nome, idade, tipo):
        if tipo == 'Passageiro':
            pessoa = Passageiro(nome, idade)
        else:
            pessoa = Piloto(nome, idade)
        self.pessoas.append(pessoa)
        return pessoa

    def get_all(self):
        return [str(p.nome) for p in self.pessoas]
    
    def remove(self, nome_pessoa):
        for pessoa in self.pessoas:
            if pessoa.nome == nome_pessoa:
                self.pessoas.remove(pessoa)
                return True
        return False
