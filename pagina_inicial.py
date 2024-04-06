from PyQt6.QtWidgets import QGridLayout, QLabel, QMainWindow, QMessageBox, QPushButton, QWidget

from view.aviao import TelaCadastroAviao, TelaRemoverAviao, TelaVerAviao
from controller.aviao import AviaoController

from view.pessoa import TelaCadastroPessoa, TelaRemoverPessoa, TelaVerPessoa
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
        
          
        
    def concluirCadastroAviao(self):
        capacidade = self.capacidadeAviao.text()
        modelo_aviao = self.modeloAviao.text()
        if not capacidade or not modelo_aviao:
            QMessageBox.warning(self.cw, 'Erro', 'Algum campo não informado')
            return TelaCadastroAviao(self)
        AviaoController().add(int(capacidade), modelo_aviao)
        self.menuPrincipal()
        QMessageBox.information(self.cw, 'Ação concluida', 'Avião Cadastrado com sucesso!')
    
    def concluirRemoverAviao(self):
        aviao_excluir = self.avioesExistentes.currentText()
        if not aviao_excluir:
            QMessageBox.warning(self.cw, 'Erro', 'Id do avião não informado')
            return TelaRemoverAviao(self)
        id_aviao, _ = aviao_excluir.split(' | ')
        AviaoController().remove(int(id_aviao))
        self.menuPrincipal()
        QMessageBox.information(self.cw, 'Ação concluida', 'Avião Removido com sucesso!')
    
    def concluirCadastroPessoa(self):
        nome = self.nomePessoa.text()
        idade = self.idadePessoa.text()
        tipo = self.tipoPessoa.currentText()
        numero_carteira = self.numeroCarteira.text()
        if not nome or not idade:
            QMessageBox.warning(self.cw, 'Erro', 'Nome ou idade não informados')
            return TelaCadastroPessoa(self)
        PessoaController().add(nome, int(idade), tipo, numero_carteira)
        self.menuPrincipal()
        QMessageBox.information(self.cw, 'Ação concluida', 'Pessoa Cadastrada com sucesso!')

    def concluirRemoverPessoa(self):
        info_pessoa = self.pessoasExistentes.currentText()
        if not info_pessoa:
            QMessageBox.warning(self.cw, 'Erro', 'Pessoa não informada')
            return TelaRemoverPessoa(self)
        id_pessoa, nome_e_tipo_pessoa = info_pessoa.split(' | ')
        _, tipo_pessoa = nome_e_tipo_pessoa.split(' - ')
        PessoaController().remove(id_pessoa, tipo_pessoa)
        self.menuPrincipal()
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

