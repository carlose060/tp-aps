
# from controller.reserva import Reserva
# from controller.voo import Voo
# from controller.pessoa import Passageiro, Piloto

from sys import exit
from PyQt6.QtGui import QAction, QIntValidator
from PyQt6.QtWidgets import (QComboBox, QGridLayout, QLabel, QLineEdit,
                             QMainWindow, QMessageBox, QPushButton, QWidget, QInputDialog)

from view.aviao import AviaoView
from controller.aviao import AviaoController

from view.pessoa import PessoaView
from controller.pessoa import PessoaController

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
        self.avioes = AviaoController()
        self.pessoas = PessoaController()
        self.telaInicial()
    
    
    def telaInicial(self):
        self.setWindowTitle('Trabalho pratico | Analise e projeto de software 2024.1')
        self.setFixedSize(800,500)
        self.limparTela()
        
        self.criarBtn(QLabel,'SEJA BEM-VINDO',0,9,3,4, CSS_TITLE)

       
        self.criarBtn(QPushButton,'Cadastrar avião',3,4,3,7,CSS_BUTTON, lambda: AviaoView.telaCadastroAviao(self))
        self.criarBtn(QPushButton,'Remover avião',3,11,3,7,CSS_BUTTON,  lambda: AviaoView.telaRemoverAviao(self))
        
        self.criarBtn(QPushButton,'Cadastrar pessoas',6,4,3,7,CSS_BUTTON)
        self.criarBtn(QPushButton,'Remover pessoas',6,11,3,7,CSS_BUTTON)
        
        self.criarBtn(QPushButton,'Cadastrar voos',9,4,3,7,CSS_BUTTON)
        self.criarBtn(QPushButton,'Remover voos',9,11,3,7,CSS_BUTTON)
        
        self.criarBtn(QPushButton,'Fazer reservas',12,4,3,7,CSS_BUTTON)
        self.criarBtn(QPushButton,'Alterar reservas',12,11,3,7,CSS_BUTTON)
        
    def ConcluirCadastroAviao(self):
        capacidade = self.capacidadeAviao.text()
        self.avioes.add(int(capacidade))
        self.telaInicial()
        QMessageBox.information(self.cw, 'Ação concluida', 'Avião Cadastrado com sucesso!')
    
    def ConcluirRemoverAviao(self):
        id_aviao = self.avioes_existentes.currentText()
        self.avioes.remove(id_aviao)
        self.telaInicial()
        QMessageBox.information(self.cw, 'Ação concluida', 'Avião Removido com sucesso!')
    
    def ConcluirCadastroPessoa(self):
        nome = self.nomePessoa.text()
        idade = self.idadePessoa.text()
        tipo = self.tipoPessoa.currentText()
        self.pessoas.add(nome, int(idade), tipo)
        self.telaInicial()
        QMessageBox.information(self.cw, 'Ação concluida', 'Pessoa Cadastrada com sucesso!')

    def ConcluirRemoverPessoa(self):
        nome_pessoa = self.pessoas_existentes.currentText()
        self.pessoas.remove(nome_pessoa)
        self.telaInicial()
        QMessageBox.information(self.cw, 'Ação concluida', 'Pessoa Removida com sucesso!')

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

