from PyQt6.QtGui import QAction, QIntValidator
from PyQt6.QtWidgets import (QComboBox, QGridLayout, QLabel, QLineEdit,
        QMainWindow, QMessageBox, QPushButton, QWidget, QInputDialog)

from view.aviao import AviaoView
from controller.aviao import AviaoController

from view.pessoa import PessoaView
from controller.pessoa import PessoaController

from view.voo import VooView
from controller.voo import VooController

from view.reserva import ReservaView
from controller.reserva import ReservaController

from data.db import DB

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
        self.voos = VooController()
        self.reservas = ReservaController()
        db = DB()
        db.load_data(self.avioes, self.pessoas, self.voos, self.reservas)
        self.telaInicial()
    
    
    def telaInicial(self):
        self.setWindowTitle('Trabalho pratico | Analise e projeto de software 2024.1')
        self.setFixedSize(800,500)
        self.limparTela()
        
        self.criarBtn(QLabel,'SEJA BEM-VINDO',0,9,3,4, CSS_TITLE)

       
        self.criarBtn(QPushButton,'Cadastrar avião',3,0,3,7,CSS_BUTTON, lambda: AviaoView.telaCadastroAviao(self))
        self.criarBtn(QPushButton,'Remover avião',3,7,3,7,CSS_BUTTON,  lambda: AviaoView.telaRemoverAviao(self))
        self.criarBtn(QPushButton,'Visualizar aviões',3,14,3,7,CSS_BUTTON,)
        
        self.criarBtn(QPushButton,'Cadastrar pessoa',6,0,3,7,CSS_BUTTON, lambda: PessoaView.telaCadastroPessoa(self))
        self.criarBtn(QPushButton,'Remover pessoa',6,7,3,7,CSS_BUTTON, lambda: PessoaView.telaRemoverPessoa(self))
        self.criarBtn(QPushButton,'Visualizar pessoas',6,14,3,7,CSS_BUTTON, )
        
        self.criarBtn(QPushButton,'Cadastrar voo',9,0,3,7,CSS_BUTTON, lambda: VooView.telaCadastroVoo(self))
        self.criarBtn(QPushButton,'Remover voo',9,7,3,7,CSS_BUTTON, lambda: VooView.telaRemoverVoo(self))
        self.criarBtn(QPushButton,'Visualizar voos',9,14,3,7,CSS_BUTTON, )
        
        self.criarBtn(QPushButton,'Fazer reservas',12,0,3,7,CSS_BUTTON, lambda: ReservaView.telaFazerReserva(self))
        self.criarBtn(QPushButton,'Alterar reservas',12,7,3,7,CSS_BUTTON)
          
        
    def concluirCadastroAviao(self):
        capacidade = self.capacidadeAviao.text()
        if not capacidade:
            QMessageBox.warning(self.cw, 'Erro', 'Capacidade não informada')
            return AviaoView.telaCadastroAviao(self)
        self.avioes.add(int(capacidade))
        self.telaInicial()
        QMessageBox.information(self.cw, 'Ação concluida', 'Avião Cadastrado com sucesso!')
    
    def concluirRemoverAviao(self):
        id_aviao = self.avioesExistentes.currentText()
        if not id_aviao:
            QMessageBox.warning(self.cw, 'Erro', 'Id do avião não informado')
            return AviaoView.telaRemoverAviao(self)
        self.avioes.remove(id_aviao)
        self.telaInicial()
        QMessageBox.information(self.cw, 'Ação concluida', 'Avião Removido com sucesso!')
    
    def concluirCadastroPessoa(self):
        nome = self.nomePessoa.text()
        idade = self.idadePessoa.text()
        tipo = self.tipoPessoa.currentText()
        if not nome or not idade:
            QMessageBox.warning(self.cw, 'Erro', 'Nome ou idade não informados')
            return PessoaView.telaCadastroPessoa(self)
        self.pessoas.add(nome, int(idade), tipo)
        self.telaInicial()
        QMessageBox.information(self.cw, 'Ação concluida', 'Pessoa Cadastrada com sucesso!')

    def concluirRemoverPessoa(self):
        nome_pessoa = self.pessoasExistentes.currentText()
        if not nome_pessoa:
            QMessageBox.warning(self.cw, 'Erro', 'Nome da pessoa não informado')
            return PessoaView.telaRemoverPessoa(self)
        self.pessoas.remove(nome_pessoa)
        self.telaInicial()
        QMessageBox.information(self.cw, 'Ação concluida', 'Pessoa Removida com sucesso!')
    
    def concluirCadastroVoo(self):
        origem = self.origemVoo.text()
        destino = self.destinoVoo.text()
        data = self.dataVoo.text() # TODO: split(' ') para separada data e hora
        info_piloto = self.pilotoVoo.currentText()  
        aviao = self.aviaoVoo.currentText()
        
        if not origem or not destino or not data or not info_piloto or not aviao:
            QMessageBox.warning(self.cw, 'Erro', 'Algum dado não informado')
            return VooView.telaCadastroVoo(self)

        info_piloto, _ = info_piloto.split(' | ')
        aviao_voo = self.avioes.get(aviao)
        piloto_voo = self.pessoas.get(info_piloto)
        
        voo_criado = self.voos.add(origem, destino, data, aviao_voo, piloto_voo)
        self.pessoas.update(piloto_voo.id, voo=voo_criado)
        piloto_voo.voo = voo_criado
        
        self.reservas.add(aviao_voo.assentos, voo_criado)
        
        self.telaInicial()
        QMessageBox.information(self.cw, 'Ação concluida', 'Voo Cadastrado com sucesso!')
        
    def concluirRemoverVoo(self):
        info_voo = self.voosExistentes.currentText()
        info_voo, _ = info_voo.split(' | ')
        if not info_voo:
            QMessageBox.warning(self.cw, 'Erro', 'Voo não informado')
            return VooView.telaRemoverVoo(self)
        
        voo_selecionado = self.voos.get(info_voo)
        
        piloto_voo = self.pessoas.get_with_voo(voo_selecionado.id)
        piloto_voo.voo = None
        self.pessoas.update(piloto_voo.id, voo=None)
        
        self.voos.remove(voo_selecionado)
        self.telaInicial()
        QMessageBox.information(self.cw, 'Ação concluida', 'Voo Removido com sucesso!')
        
    def concluirFazerReserva(self):
        numero_assento_selecionado = self.selecionarAssento.currentText()
        assento = self.dict_assentos[numero_assento_selecionado]
        
        reserva = self.reservas.get(assento.id, self.id_voo_selecionado) 
        self.pessoas.update(self.id_passageiro_selecionado, reserva=reserva)
        
        self.avioes.assentos_controller.update(assento, ocupado=True)
        QMessageBox.information(self.cw, 'Ação concluida', 'Reserva feita com sucesso!')
        return self.telaInicial()

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

