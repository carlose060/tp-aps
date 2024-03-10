from PyQt6.QtWidgets import QComboBox, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QDateTimeEdit


CSS_BUTTON = """
    font-size: 20px;
    width: 100%;
    height: 120%; 
"""
CSS_TITLE = 'font-size: 25px; font-weight: bold'


class ReservaView:
    
    
    @staticmethod
    def telaEscolherAssentoReserva(janela):
        
        id_voo_selecionado = janela.vooExistentes.currentText().split(' | ')[0]
        voo_selecionado = janela.voos.get(id_voo_selecionado)
        id_aviao_selecionado = voo_selecionado.id_aviao
        aviao_selecionado = janela.avioes.get(id_aviao_selecionado)
        
        id_passageiro_selecionado = janela.passageirosExistentes.currentText().split(' | ')[0]
        janela.id_voo_selecionado = id_voo_selecionado
        janela.id_passageiro_selecionado = id_passageiro_selecionado
        
        janela.setFixedSize(400,300)
        janela.limparTela()
        
        
        janela.criarBtn(QLabel,'ESCOLHER ASSENTO',0,3,3,12, CSS_TITLE)
        
        linha = 3
        coluna = 0
        css_1 = """font-size: 15px; width: 100%; height: 120%; background-color: red;"""
        css_2 = """font-size: 15px; width: 100%; height: 120%; background-color: green;"""
        janela.dict_assentos = {str(a.numero): a for a in aviao_selecionado.assentos}
        list_assentos = []
        for assento in aviao_selecionado.assentos:
            if assento.ocupado:
                janela.criarBtn(QPushButton, str(assento.numero), linha, coluna, 2, 2, css_1)
            else:
                list_assentos.append(str(assento.numero))
                janela.criarBtn(QPushButton, str(assento.numero), linha, coluna, 2, 2, css_2)
            
            coluna += 2
            if coluna > 18:
                coluna = 0
                linha += 3
       
        if not coluna == 0: linha += 3; coluna = 0
        
        
        janela.selecionarAssento = QComboBox()
        janela.selecionarAssento.addItems(list_assentos)
        janela.selecionarAssento.setStyleSheet("""width: 10px;height: 40%;font-size: 16px;""")
        janela.grid.addWidget(janela.selecionarAssento, linha, coluna, 3, 5)
        
        janela.criarBtn(QPushButton,'Selecionar',linha,coluna+5,3,6,CSS_BUTTON, janela.concluirFazerReserva)
        janela.criarBtn(QPushButton,'Voltar',linha,coluna+11,3,6,CSS_BUTTON, janela.telaInicial)
        
        

    @staticmethod
    def telaFazerReserva(janela):
        
        janela.setFixedSize(400,300)
        janela.limparTela()
        
        janela.criarBtn(QLabel,'FAZER RESERVA',0,3,3,12, CSS_TITLE)
        
        janela.criarBtn(QLabel,'Voos:',3,0,3,6, CSS_BUTTON)
        janela.vooExistentes = QComboBox()
        janela.vooExistentes.addItems(janela.voos.get_all())
        janela.vooExistentes.setStyleSheet("""width: 10px;height: 40%;font-size: 16px;""")
        janela.grid.addWidget(janela.vooExistentes, 3, 6, 3, 12)
        
        janela.criarBtn(QLabel,'Passageiro:',6,0,3,6, CSS_BUTTON)
        janela.passageirosExistentes = QComboBox()
        janela.passageirosExistentes.addItems(janela.pessoas.get_all('Passageiro'))
        janela.passageirosExistentes.setStyleSheet("""width: 10px;height: 40%;font-size: 16px;""")
        janela.grid.addWidget(janela.passageirosExistentes, 6, 6, 3, 12)
        
        
        janela.criarBtn(QPushButton,'Selecionar',9,0,3,6,CSS_BUTTON, lambda: ReservaView.telaEscolherAssentoReserva(janela))
        janela.criarBtn(QPushButton,'Voltar',9,6,3,6,CSS_BUTTON, janela.telaInicial)