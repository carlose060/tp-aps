# ---------------------------------------------------------------#
# IMPORTS PARA SER VISIVEIS BIBLIOTECAS EXTERNAS DA PASTAR RAIZ
from sys import path
from pathlib import Path
SRC_PATH = Path(__file__).resolve().parent.parent
path.append(str(SRC_PATH))
# ---------------------------------------------------------------#

from data.db import DB
from model.pessoa import Passageiro, Piloto


class PessoaController:
    def __init__(self):
        self.pessoas = []

    def add(self, nome, idade, tipo):
        db = DB()
        if tipo == 'Passageiro':
            id_passageiro = db.insert_passageiro(nome, idade)
            pessoa = Passageiro(id_passageiro, nome, idade)
        else:
            id_piloto = db.insert_piloto(nome, idade)
            pessoa = Piloto(id_piloto, nome, idade)
        self.pessoas.append(pessoa)
        db.close()
        return pessoa
    

    def get_all(self, tipo=None):
        if tipo == 'Passageiro':
            return [str(p.id)+f' | {p.nome}' for p in self.pessoas if type(p) == Passageiro and p.id_reserva is None]
        elif tipo == 'Piloto':
            return [str(p.id)+f' | {p.nome}' for p in self.pessoas if type(p) == Piloto and p.id_voo is None]
        return [str(p.nome) for p in self.pessoas]
    
    def remove(self, nome):
        for pessoa in self.pessoas:
            if pessoa.nome == nome:
                db = DB()
                if type(pessoa) == Passageiro:
                    db.remove_passageiro(nome)
                else:
                    db.remove_piloto(nome)
                self.pessoas.remove(pessoa)
                db.close()
                return True
        return False

    def update(self, id_pessoa, id_reserva=None, id_voo=None):
        for pessoa in self.pessoas:
            if pessoa.id == int(id_pessoa):
                db = DB()
                if type(pessoa) == Passageiro:
                    db.update_passageiro(id_pessoa, id_reserva)
                    db.close()
                    return True
                elif type(pessoa) == Piloto:
                    db.update_piloto(id_pessoa, id_voo)
                    db.close()
                    return True    
        return False