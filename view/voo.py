from PyQt6.QtWidgets import QComboBox, QLabel, QLineEdit, QPushButton, QDateTimeEdit, QMessageBox
from PyQt6.QtCore import QDate


from controller.voo import VooController
from controller.aviao import AviaoController
from controller.pessoa import PessoaController

CSS_BUTTON = """
    font-size: 20px;
    width: 100%;
    height: 120%; 
"""
CSS_TITLE = 'font-size: 25px; font-weight: bold'

class TelaCadastroVoo:
    
    def __init__(self, janela):
        janela.setFixedSize(400,300)
        janela.limparTela()
        
        janela.criarBtn(QLabel,'CADASTRO DE VOO',0,3,3,12, CSS_TITLE)
        
        janela.criarBtn(QLabel,'Origem:',3,0,3,6, CSS_BUTTON)
        janela.origemVoo = janela.criarBtn(QLineEdit,'',3,7,3,10, CSS_BUTTON)
        
        janela.criarBtn(QLabel,'Destino:',6,0,3,6, CSS_BUTTON)
        janela.destinoVoo = janela.criarBtn(QLineEdit,'',6,7,3,10, CSS_BUTTON)
        
        janela.criarBtn(QLabel,'Data:',9,0,3,6, CSS_BUTTON)
        janela.dataVoo = QDateTimeEdit(QDate.currentDate().addDays(1))
        janela.dataVoo.setDisplayFormat("dd-MM-yyyy HH:mm")
        janela.dataVoo.setMinimumDate(QDate.currentDate().addDays(1))
        janela.dataVoo.setMaximumDate(QDate.currentDate().addDays(365))
        janela.grid.addWidget(janela.dataVoo, 9,7,3,10)
        
        
        all_avioes = AviaoController().get_all()
        janela.criarBtn(QLabel,'aviao:',12,0,3,6, CSS_BUTTON)
        janela.aviaoVoo = QComboBox()
        janela.aviaoVoo.addItems([str(av.id) for av in all_avioes])
        janela.aviaoVoo.setStyleSheet("""width: 10px;height: 40%;font-size: 16px;""")
        janela.grid.addWidget(janela.aviaoVoo, 12, 7, 3, 10)
        
        all_pilotos = PessoaController().get_all_pilotos()
        janela.criarBtn(QLabel,'piloto:',15,0,3,6, CSS_BUTTON)
        janela.pilotoVoo = QComboBox()
        janela.pilotoVoo.addItems([f'{p.id} | {p.nome}' for p in all_pilotos])
        janela.pilotoVoo.setStyleSheet("""width: 10px;height: 40%;font-size: 16px;""")
        janela.grid.addWidget(janela.pilotoVoo, 15, 7, 3, 10)
        
    
        janela.criarBtn(QPushButton,'Cadastrar',18,0,3,6,CSS_BUTTON, lambda : self.concluirCadastroVoo(janela))
        janela.criarBtn(QPushButton,'Voltar',18,6,3,6,CSS_BUTTON, janela.menuPrincipal)
        
    def concluirCadastroVoo(self, janela):
        origem = janela.origemVoo.text()
        destino = janela.destinoVoo.text()
        data = janela.dataVoo.text() # TODO: split(' ') para separada data e hora
        info_piloto = janela.pilotoVoo.currentText()  
        id_aviao = janela.aviaoVoo.currentText()
        
        if not origem or not destino or not data or not info_piloto or not id_aviao:
            QMessageBox.warning(janela.cw, 'Erro', 'Algum dado não informado')
            return TelaCadastroVoo(janela)
        
        id_piloto, _ = info_piloto.split(' | ')
        VooController().add(origem, destino, data, id_aviao, id_piloto)
    
        janela.menuPrincipal()
        QMessageBox.information(janela.cw, 'Ação concluida', 'Voo Cadastrado com sucesso!')
        
class TelaRemoverVoo:
    
    def __init__(self, janela):
        janela.setFixedSize(400,300)
        janela.limparTela()
        
        janela.criarBtn(QLabel,'REMOÇÃO DE VOO',0,3,3,12, CSS_TITLE)
        
        janela.criarBtn(QLabel,'Voo:',3,0,3,6, CSS_BUTTON)
        janela.voosExistentes = QComboBox()
        todos_voos = VooController().get_all()
        lista_voos_str = [f'{v.id} | {v.origem} - {v.destino}' for v in todos_voos]
        janela.voosExistentes.addItems(lista_voos_str)
        janela.grid.addWidget(janela.voosExistentes, 3, 7, 3, 10)
        
        janela.criarBtn(QPushButton,'Remover',6,0,3,6,CSS_BUTTON, lambda : self.concluirRemocaoVoo(janela))
        janela.criarBtn(QPushButton,'Voltar',6,6,3,6,CSS_BUTTON, janela.menuPrincipal)
        
    def concluirRemocaoVoo(self, janela):
        info_voo = janela.voosExistentes.currentText()  
        id_voo, _ = info_voo.split(' | ')
        VooController().remove(id_voo)
        janela.menuPrincipal()
        QMessageBox.information(janela.cw, 'Ação concluida', 'Voo Removido com sucesso!')
        
class TelaVerVoo:
        
        def __init__(self, janela):
            janela.setFixedSize(800,600)
            janela.limparTela()
            
            janela.criarBtn(QLabel,'VOOS CADASTRADOS',0,3,3,12, CSS_TITLE)
            
            
            row = 3
            janela.criarBtn(QLabel,'Id',row,0,3,5, CSS_BUTTON)
            janela.criarBtn(QLabel,'Origem',row,5,3,6, CSS_BUTTON)
            janela.criarBtn(QLabel,'Destino',row,11,3,6, CSS_BUTTON)
            janela.criarBtn(QLabel,'Data',row,17,3,6, CSS_BUTTON)
            row += 3
            
            for voo in VooController().get_all():
                janela.criarBtn(QLabel,f'{voo.id}',row,0,3,3, CSS_BUTTON)
                janela.criarBtn(QLabel,f'{voo.origem}',row,3,3,3, CSS_BUTTON)
                janela.criarBtn(QLabel,f'{voo.destino}',row,6,3,3, CSS_BUTTON)
                janela.criarBtn(QLabel,f'{voo.data}',row,9,3,3, CSS_BUTTON)
                row += 3
            
            janela.criarBtn(QPushButton,'Voltar',row,17,3,4,CSS_BUTTON, janela.menuPrincipal)