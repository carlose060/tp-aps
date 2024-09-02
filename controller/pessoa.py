from data.pessoa import PessoaDAOimp
from model.pessoa import Passageiro, Piloto


    
    
class PessoaController:


    def add(self, nome, idade, tipo, numero_carteira):
        db = PessoaDAOimp()
        
        if tipo == 'Passageiro':
            pessoa = Passageiro(0, nome, idade)
        else:
            pessoa = Piloto(0, nome, idade, numero_carteira)

        id_pessoa = db.insert(pessoa)
        pessoa.id = id_pessoa
        db.close()
        return True

    def get_all(self):
        db = PessoaDAOimp()
        todas_pessoas = db.get_all()
        return [Passageiro(p[0], p[1], p[2]) if p[-1] == 'Passageiro' else Piloto(p[0], p[1], p[2], p[3]) for p in todas_pessoas]


    def remove(self, id, tipo):
        db = PessoaDAOimp()
        db.remove(id, tipo)
        db.close()
        return True
    
    def get_passageiro_with_id(self, id):
        db = PessoaDAOimp()
        passageiro = db.get_with_id(id, 'Passageiro')
        db.close()
        return Passageiro(passageiro[0], passageiro[1], passageiro[2], passageiro[3])
    
    
    def get_piloto_with_id(self, id):
        db = PessoaDAOimp()
        piloto = db.get_with_id(id, 'Piloto')
        db.close()
        return Piloto(piloto[0], piloto[1], piloto[2], piloto[3])
    
    def get_all_pilotos(self):
        db = PessoaDAOimp()
        todos_pilotos = db.get_all_pilotos()
        db.close()
        return [Piloto(p[0], p[1], p[2], p[3]) for p in todos_pilotos]

    def get_all_passageiros(self):
        db = PessoaDAOimp()
        todos_passageiros = db.get_all_passageiros()
        db.close()
        return [Passageiro(p[0], p[1], p[2]) for p in todos_passageiros]
    
    
    def update_reserva_passageiro(self, id_passageiro, reserva):
        db = PessoaDAOimp()
        db.update_reserva_passageiro(int(id_passageiro), reserva.id)
        db.close()
        return True
    
    
        

