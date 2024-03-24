from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QComboBox, QLabel, QLineEdit, QPushButton


CSS_BUTTON = """
    font-size: 20px;
    width: 100%;
    height: 120%; 
"""
CSS_TITLE = 'font-size: 25px; font-weight: bold'


class AviaoView:
    
    @staticmethod
    def telaCadastroAviao(janela):
        
        janela.setFixedSize(400,300)
        janela.limparTela()
        
        janela.criarBtn(QLabel,'CADASTRO DE AVIÃO',0,3,3,12, CSS_TITLE)
        
        janela.criarBtn(QLabel,'Capacidade:',3,0,3,6, CSS_BUTTON)
        janela.capacidadeAviao = janela.criarBtn(QLineEdit,'',3,7,3,10, CSS_BUTTON)
        janela.capacidadeAviao.setValidator(QIntValidator())
        
        
        janela.criarBtn(QPushButton,'Cadastrar',7,0,3,6,CSS_BUTTON, janela.concluirCadastroAviao)
        janela.criarBtn(QPushButton,'Voltar',7,6,3,6,CSS_BUTTON, janela.telaInicial)

    @staticmethod
    def telaRemoverAviao(janela):
        
        janela.setFixedSize(400,300)
        janela.limparTela()
        
        janela.criarBtn(QLabel,'REMOÇÃO DE AVIÃO',0,3,3,12, CSS_TITLE)
        
        janela.criarBtn(QLabel,'Id do avião:',3,0,3,6, CSS_BUTTON)
        janela.avioesExistentes = QComboBox()
        janela.avioesExistentes.addItems(janela.avioes.get_all())
        janela.avioesExistentes.setStyleSheet("""width: 10px;height: 40%;font-size: 16px;""")
        janela.grid.addWidget(janela.avioesExistentes, 3, 7, 3, 10)
        
        
        janela.criarBtn(QPushButton,'Remover',7,0,3,6,CSS_BUTTON, janela.concluirRemoverAviao)
        janela.criarBtn(QPushButton,'Voltar',7,6,3,6,CSS_BUTTON, janela.telaInicial)
        
    @staticmethod
    def telaVerAviao(janela):
        janela.setFixedSize(400,300)
        janela.limparTela()
        
        janela.criarBtn(QLabel,'VER AVIÕES',0,3,3,12, CSS_TITLE)
        
        row = 3
        janela.criarBtn(QLabel,'Id',row,0,3,5, CSS_BUTTON)
        janela.criarBtn(QLabel,'Capacidade',row,5,3,5, CSS_BUTTON)
        row += 3
        for aviao in janela.avioes.avioes:
            janela.criarBtn(QLabel,str(aviao.id),row,0,3,5, CSS_BUTTON)
            janela.criarBtn(QLabel,str(aviao.capacidade),row,5,3,5, CSS_BUTTON)
            row += 3
        janela.criarBtn(QPushButton,'Voltar',row,0,3,6,CSS_BUTTON, janela.telaInicial)
        

    