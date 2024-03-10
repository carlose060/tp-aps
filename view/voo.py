from PyQt6.QtWidgets import QComboBox, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QDateTimeEdit


CSS_BUTTON = """
    font-size: 20px;
    width: 100%;
    height: 120%; 
"""
CSS_TITLE = 'font-size: 25px; font-weight: bold'


class VooView:
    
    @staticmethod
    def telaCadastroVoo(janela):
        
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
        
        
                
        janela.criarBtn(QLabel,'aviao:',12,0,3,6, CSS_BUTTON)
        janela.aviaoVoo = QComboBox()
        janela.aviaoVoo.addItems(janela.avioes.get_all())
        janela.aviaoVoo.setStyleSheet("""width: 10px;height: 40%;font-size: 16px;""")
        janela.grid.addWidget(janela.aviaoVoo, 12, 7, 3, 10)
        
        
        janela.criarBtn(QLabel,'piloto:',15,0,3,6, CSS_BUTTON)
        janela.pilotoVoo = QComboBox()
        janela.pilotoVoo.addItems(janela.pessoas.get_all('Piloto'))
        janela.pilotoVoo.setStyleSheet("""width: 10px;height: 40%;font-size: 16px;""")
        janela.grid.addWidget(janela.pilotoVoo, 15, 7, 3, 10)
        
    
        janela.criarBtn(QPushButton,'Cadastrar',18,0,3,6,CSS_BUTTON, janela.concluirCadastroVoo)
        janela.criarBtn(QPushButton,'Voltar',18,6,3,6,CSS_BUTTON, janela.telaInicial)

    @staticmethod
    def telaRemoverVoo(janela):
        
        janela.setFixedSize(400,300)
        janela.limparTela()
        
        janela.criarBtn(QLabel,'REMOÇÃO DE VOO',0,3,3,12, CSS_TITLE)
        
        janela.criarBtn(QLabel,'Voos:',3,0,3,6, CSS_BUTTON)
        janela.voosExistentes = QComboBox()
        janela.voosExistentes.addItems(janela.avioes.get_all())
        janela.voosExistentes.setStyleSheet("""width: 10px;height: 40%;font-size: 16px;""")
        janela.grid.addWidget(janela.voosExistentes, 3, 7, 3, 10)
        
        
        janela.criarBtn(QPushButton,'Remover',6,0,3,6,CSS_BUTTON, janela.concluirRemoverVoo)
        janela.criarBtn(QPushButton,'Voltar',6,6,3,6,CSS_BUTTON, janela.telaInicial)