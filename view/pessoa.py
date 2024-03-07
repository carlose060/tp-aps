from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QComboBox, QLabel, QLineEdit, QPushButton


CSS_BUTTON = """
    font-size: 20px;
    width: 100%;
    height: 120%; 
"""
CSS_TITLE = 'font-size: 25px; font-weight: bold'


class PessoaView:
    
    @staticmethod
    def telaCadastroPessoa(self):
        
        self.setFixedSize(400,300)
        self.limparTela()
        
        self.criarBtn(QLabel,'CADASTRO DE PESSOA',0,3,3,12, CSS_TITLE)
        
        self.criarBtn(QLabel,'Nome:',3,0,3,6, CSS_BUTTON)
        self.nomePessoa = self.criarBtn(QLineEdit,'',3,7,3,10, CSS_BUTTON)
        
        self.criarBtn(QLabel,'Idade:',6,0,3,6, CSS_BUTTON)
        self.idadePessoa = self.criarBtn(QLineEdit,'',6,7,3,10, CSS_BUTTON)
        self.idadePessoa.setValidator(QIntValidator())
        
        self.criarBtn(QLabel,'Tipo:',9,0,3,6, CSS_BUTTON)
        self.tipoPessoa = self.criarBtn(QComboBox,'',9,7,3,10, CSS_BUTTON)
        self.tipoPessoa.addItems(['Passageiro', 'Piloto'])
        
    
        self.criarBtn(QPushButton,'Cadastrar',12,0,3,6,CSS_BUTTON, self.ConcluirCadastroPessoa)
        self.criarBtn(QPushButton,'Voltar',12,6,3,6,CSS_BUTTON, self.telaInicial)

    @staticmethod
    def telaRemoverPessoa(self):
        
        self.setFixedSize(400,300)
        self.limparTela()
        
        self.criarBtn(QLabel,'REMOÇÃO DE PESSOA',0,3,3,12, CSS_TITLE)
        
        self.criarBtn(QLabel,'Nome:',3,0,3,6, CSS_BUTTON)
        self.pessoas_existentes = QComboBox()
        self.pessoas_existentes.addItems(self.pessoas.get_all())
        self.pessoas_existentes.setStyleSheet("""width: 10px;height: 40%;font-size: 16px;""")
        self.grid.addWidget(self.pessoas_existentes, 3, 7, 3, 10)
        
        
        self.criarBtn(QPushButton,'Remover',7,0,3,6,CSS_BUTTON, self.ConcluirRemoverPessoa)
        self.criarBtn(QPushButton,'Voltar',7,6,3,6,CSS_BUTTON, self.telaInicial)
        
        

    