from data.aviao import AviaoDB
from model.aviao import Aviao



class AviaoController:


    def add(self, capacidade, modelo):
        aviao = Aviao(0, capacidade, modelo)
        db = AviaoDB()
        id_aviao = db.insert_aviao(aviao)
        db.close()
        aviao.id = id_aviao
        return True


    def get_all(self):
        db = AviaoDB()
        avioes = db.get_all_avioes()
       
        db.close()
        return [Aviao(aviao[0], aviao[1], aviao[2]) for aviao in avioes]
    
    def get_with_id(self, id_aviao):
        db = AviaoDB()
        aviao = db.get_aviao_with_id(id_aviao)
        db.close()
        return Aviao(aviao[0], aviao[1], aviao[2])
    
    def remove(self, id_aviao):
        db = AviaoDB()
        db.remove_aviao(id_aviao)
        db.close()
        return True
    

   