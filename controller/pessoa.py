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
    
    def load_piloto(self, id_piloto, nome, idade):
        pessoa = Piloto(id_piloto, nome, idade)
        self.pessoas.append(pessoa)
        return pessoa

    def load_passageiro(self, id_passageiro, nome, idade, reserva):
        pessoa = Passageiro(id_passageiro, nome, idade, reserva)
        self.pessoas.append(pessoa)
        return pessoa
        
    def get(self, id_pessoa):
        for pessoa in self.pessoas:
            if pessoa.id == int(id_pessoa):
                return pessoa
            
    def get_with_voo(self, id_voo):
        for pessoa in self.pessoas:
            if type(pessoa) == Piloto:
                if pessoa.voo.id == int(id_voo):
                    return pessoa
        return None
    
    def get_all(self, tipo=None):
        if tipo == 'Passageiro':
            return [str(p.id)+f' | {p.nome}' for p in self.pessoas if type(p) == Passageiro and p.reserva is None]
        elif tipo == 'Piloto':
            return [str(p.id)+f' | {p.nome}' for p in self.pessoas if type(p) == Piloto and p.voo is None]
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

    def update(self, id_pessoa, reserva=None, voo=None):
        for pessoa in self.pessoas:
            if pessoa.id == int(id_pessoa):
                db = DB()
                if type(pessoa) == Passageiro:
                    pessoa.reserva = reserva
                    db.update_passageiro(id_pessoa, reserva.id)
                    db.close()
                    return True
                elif type(pessoa) == Piloto:
                    pessoa.voo = voo
                    db.update_piloto(id_pessoa, voo.id)
                    db.close()
                    return True    
        return False