from data.pessoa import PessoaDB
from model.pessoa import Passageiro, Piloto


class PessoaController:


    def add(self, nome, idade, tipo, numero_carteira):
        db = PessoaDB()
        if tipo == 'Passageiro':
            pessoa = Passageiro(0, nome, idade)
            id_pessoa = db.insert_passageiro(nome, idade)
        else:
            pessoa = Piloto(0, nome, idade, numero_carteira)
            id_pessoa = db.insert_piloto(nome, idade, numero_carteira)
        pessoa.id = id_pessoa
        db.close()
        return True

    def get_all_pilotos(self):
        db = PessoaDB()
        todos_pilotos = db.get_all_pilotos()
        db.close()
        return [Piloto(p[0], p[1], p[2], p[3]) for p in todos_pilotos]
    
    def get_all(self):
        db = PessoaDB()
        todas_pessoas = db.get_all_pessoas()
        return [Passageiro(p[0], p[1], p[2]) if p[-1] == 'Passageiro' else Piloto(p[0], p[1], p[2], p[3]) for p in todas_pessoas]

    def get_piloto_with_id(self, id):
        db = PessoaDB()
        piloto = db.get_piloto_with_id(id)
        db.close()
        return Piloto(piloto[0], piloto[1], piloto[2], piloto[3])
    
    def remove(self, id, tipo):
        
        db = PessoaDB()
        if tipo == 'Passageiro':
            db.remove_passageiro(id)
        else:
            db.remove_piloto(id)
        db.close()
        return True
        

