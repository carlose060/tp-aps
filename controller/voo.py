from data.voo import VooDB
from model.voo import Voo
from controller.aviao import AviaoController
from controller.pessoa import PessoaController

class VooController:
    
    def add(self, origem, destino, data, aviao, piloto):
        aviao = AviaoController().get_with_id(int(aviao))
        piloto = PessoaController().get_piloto_with_id(int(piloto))
        voo = Voo(0, origem, destino, data, aviao, piloto)
        db = VooDB()
        id_voo = db.insert_voo(origem, destino, data, aviao.id, piloto.id)
        db.close()
        voo.id = id_voo
        return True


    def get_all(self):
        list_voos = []
        db = VooDB()
        voos = db.get_all_voos()
        db.close()
        for voo in voos:
            aviao = AviaoController().get_with_id(int(voo[4]))
            piloto = PessoaController().get_piloto_with_id(int(voo[5]))
            list_voos.append(Voo(voo[0], voo[1], voo[2], voo[3], aviao, piloto))
        return list_voos
    
    def remove(self, voo):
        if type(voo) == Voo:
            voo = voo.id
        db = VooDB()
        db.remove_voo(int(voo))
        db.close()
        return True