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
    def telaCadastroAviao(self):
        
        self.setFixedSize(400,300)
        self.limparTela()
        
        self.criarBtn(QLabel,'CADASTRO DE AVIÃO',0,3,3,12, CSS_TITLE)
        
        self.criarBtn(QLabel,'Capacidade:',3,0,3,6, CSS_BUTTON)
        self.capacidadeAviao = self.criarBtn(QLineEdit,'',3,7,3,10, CSS_BUTTON)
        self.capacidadeAviao.setValidator(QIntValidator())
        
        
        self.criarBtn(QPushButton,'Cadastrar',7,0,3,6,CSS_BUTTON, self.ConcluirCadastroAviao)
        self.criarBtn(QPushButton,'Voltar',7,6,3,6,CSS_BUTTON, self.telaInicial)

    @staticmethod
    def telaRemoverAviao(self):
        
        self.setFixedSize(400,300)
        self.limparTela()
        
        self.criarBtn(QLabel,'REMOÇÃO DE AVIÃO',0,3,3,12, CSS_TITLE)
        
        self.criarBtn(QLabel,'Id do avião:',3,0,3,6, CSS_BUTTON)
        self.avioes_existentes = QComboBox()
        self.avioes_existentes.addItems(self.avioes.get_all())
        self.avioes_existentes.setStyleSheet("""width: 10px;height: 40%;font-size: 16px;""")
        self.grid.addWidget(self.avioes_existentes, 3, 7, 3, 10)
        
        
        self.criarBtn(QPushButton,'Remover',7,0,3,6,CSS_BUTTON, self.ConcluirRemoverAviao)
        self.criarBtn(QPushButton,'Voltar',7,6,3,6,CSS_BUTTON, self.telaInicial)
        
        

    