from PyQt6.QtWidgets import QGridLayout, QLabel, QMainWindow, QPushButton, QWidget

from view.voo import TelaCadastroVoo, TelaRemoverVoo, TelaVerVoo
from view.aviao import TelaCadastroAviao, TelaRemoverAviao, TelaVerAviao
from view.pessoa import TelaCadastroPessoa, TelaRemoverPessoa, TelaVerPessoa

CSS_BUTTON = """
    font-size: 20px;
    width: 100%;
    height: 120%; 
"""
CSS_FORM = """ 
    width: 85%;
    max-height: 90%;
    font-size: 16px;
"""
CSS_TITLE = 'font-size: 25px; font-weight: bold'
CSS_TITLE_2 = 'font-size: 25px; font-weight: bold; '



class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
    
        self.cw = None
        self.menuPrincipal()
    
    
    def menuPrincipal(self):
        self.setWindowTitle('Trabalho pratico | Analise e projeto de software 2024.1')
        self.setFixedSize(800,500)
        self.limparTela()
        
        self.criarBtn(QLabel,'SEJA BEM-VINDO',0,9,3,4, CSS_TITLE)

       
        self.criarBtn(QPushButton,'Cadastrar avião',3,0,3,7,CSS_BUTTON, lambda: TelaCadastroAviao(self))
        self.criarBtn(QPushButton,'Remover avião',3,7,3,7,CSS_BUTTON,  lambda: TelaRemoverAviao(self))
        self.criarBtn(QPushButton,'Visualizar aviões',3,14,3,7,CSS_BUTTON, lambda: TelaVerAviao(self))
        
        self.criarBtn(QPushButton,'Cadastrar pessoa',6,0,3,7,CSS_BUTTON, lambda: TelaCadastroPessoa(self))
        self.criarBtn(QPushButton,'Remover pessoa',6,7,3,7,CSS_BUTTON, lambda: TelaRemoverPessoa(self))
        self.criarBtn(QPushButton,'Visualizar pessoas',6,14,3,7,CSS_BUTTON, lambda: TelaVerPessoa(self))
         
        self.criarBtn(QPushButton,'Cadastrar voo',9,0,3,7,CSS_BUTTON, lambda: TelaCadastroVoo(self))
        self.criarBtn(QPushButton,'Remover voo',9,7,3,7,CSS_BUTTON, lambda: TelaRemoverVoo(self))
        self.criarBtn(QPushButton,'Visualizar voos',9,14,3,7,CSS_BUTTON, lambda: TelaVerVoo(self))
    def criarBtn(self,obj, title, row, col, rowspan, colspan, css=None, eventClick=None):
        btn = obj()
        btn.setText(title)
        if css:
            btn.setStyleSheet(css)
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if eventClick:
            btn.clicked.connect(eventClick)
        return btn

    def limparTela(self):
        if self.cw:
            self.cw.destroy()
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.setCentralWidget(self.cw)
        for j in range(0,21):
            for i in range(0,21): self.criarBtn(QLabel,f'',j,i,1,1)

