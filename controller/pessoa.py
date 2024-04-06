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


    def add(self, nome, idade, tipo, numero_carteira):
        db = DB()
        if tipo == 'Passageiro':
            pessoa = Passageiro(0, nome, idade)
            id_pessoa = db.insert_passageiro(nome, idade)
        else:
            pessoa = Piloto(0, nome, idade, numero_carteira)
            id_pessoa = db.insert_piloto(nome, idade, numero_carteira)
        pessoa.id = id_pessoa
        db.close()
        return True


    def get_all(self):
        db = DB()
        todas_pessoas = db.get_all_pessoas()
        return [Passageiro(p[0], p[1], p[2]) if p[-1] == 'Passageiro' else Piloto(p[0], p[1], p[2], p[3]) for p in todas_pessoas]

    
    def remove(self, id, tipo):
        
        db = DB()
        if tipo == 'Passageiro':
            db.remove_passageiro(id)
        else:
            db.remove_piloto(id)
        db.close()
        return True
        

