from PyQt6.QtWidgets import QComboBox, QLabel, QLineEdit, QPushButton, QDateTimeEdit, QMessageBox
from PyQt6.QtCore import QDate

from controller.reserva import ReservaController
from controller.voo import VooController
from controller.pessoa import PessoaController
CSS_BUTTON = """
    font-size: 20px;
    width: 100%;
    height: 120%; 
"""
CSS_TITLE = 'font-size: 25px; font-weight: bold'

class TelaCadastroReserva:
    
    
    def __init__(self, janela):
        janela.setFixedSize(400,300)
        janela.limparTela()
        
        janela.criarBtn(QLabel,'CADASTRO DE RESERVA',0,3,3,12, CSS_TITLE)
        
        janela.criarBtn(QLabel,'Preço:',3,0,3,6, CSS_BUTTON)
        janela.preco = janela.criarBtn(QLineEdit,'',3,7,3,10, CSS_BUTTON)
        

        
        all_voos = VooController().get_all()
        janela.criarBtn(QLabel,'voo:',6,0,3,6, CSS_BUTTON)
        janela.vooReserva = QComboBox()
        janela.vooReserva.addItems([f'{str(av.id)} | {av.destino}' for av in all_voos])
        janela.vooReserva.setStyleSheet("""width: 10px;height: 40%;font-size: 16px;""")
        janela.grid.addWidget(janela.vooReserva, 6, 7, 3, 10)
        
        all_passageiros = PessoaController().get_all_passageiros()
        janela.criarBtn(QLabel,'passageiro:',9,0,3,6, CSS_BUTTON)
        janela.passageiroReserva = QComboBox()
        janela.passageiroReserva.addItems([f'{str(p.id)} | {p.nome}' for p in all_passageiros])
        janela.passageiroReserva.setStyleSheet("""width: 10px;height: 40%;font-size: 16px;""")
        janela.grid.addWidget(janela.passageiroReserva , 9, 7, 3, 10)
        
        
        janela.criarBtn(QPushButton,'Escolher assento',12,0,3,6,CSS_BUTTON, lambda : TelaCadastroReserva2(janela))
        janela.criarBtn(QPushButton,'Voltar',12,6,3,6,CSS_BUTTON, janela.menuPrincipal)

class TelaCadastroReserva2:
    
    def __init__(self, janela):
        
        values = (janela.preco.text(), janela.vooReserva.currentText(), janela.passageiroReserva.currentText())
        janela.setFixedSize(400,300)
        janela.limparTela()
        
        janela.criarBtn(QLabel,'CADASTRO DE RESERVA',0,3,3,12, CSS_TITLE)
        
        
        voo = values[1]
        
        lis_assentos = ReservaController().get_assentos_disponiveis(voo.split(' | ')[0])
        janela.criarBtn(QLabel,'assento:',3,0,3,6, CSS_BUTTON)
        janela.assentoReserva = QComboBox()
        janela.assentoReserva.addItems(lis_assentos)
        janela.assentoReserva.setStyleSheet("""width: 10px;height: 40%;font-size: 16px;""")
        janela.grid.addWidget(janela.assentoReserva, 3, 7, 3, 10)
        
        
        janela.criarBtn(QPushButton,'Cadastrar',6,0,3,6,CSS_BUTTON, lambda : self.concluirInserirReserva(janela, values))
        
    def concluirInserirReserva(self, janela, values):
        assento = janela.assentoReserva.currentText()
        
        if not values[0] or not values[1] or not values[2] or not assento:
            QMessageBox.warning(janela.cw, 'Erro', 'Nome ou idade não informados')
            return TelaCadastroReserva(janela)
        reserva = ReservaController().add(values[0], values[1].split(' | ')[0],assento)
        PessoaController().update_reserva_passageiro(values[2].split(' | ')[0], reserva)
        janela.menuPrincipal()
        QMessageBox.information(janela.cw, 'Ação concluida', 'Reserva Cadastrada com sucesso!')
        
class TelaRemoverReserva:
    
    def __init__(self, janela):
        janela.setFixedSize(600,800)
        janela.limparTela()
        
        janela.criarBtn(QLabel,'REMOVER RESERVAS',0,3,3,12, CSS_TITLE)
        janela.criarBtn(QLabel,'id:',3,0,3,6, CSS_BUTTON)
        janela.reservasExistentes = QComboBox()
        todas_reservas = ReservaController().get_all()
        janela.reservasExistentes.addItems([f'{rs.id} | {rs.assento}' for rs in todas_reservas])
        janela.reservasExistentes.setStyleSheet("""width: 10px;height: 40%;font-size: 16px;""")
        janela.grid.addWidget(janela.reservasExistentes, 3, 7, 3, 10)
        
        
        janela.criarBtn(QPushButton,'Remover',7,0,3,6,CSS_BUTTON, lambda : self.concluirRemoverReserva(janela))
        janela.criarBtn(QPushButton,'Voltar',7,6,3,6,CSS_BUTTON, janela.menuPrincipal)
        
    def concluirRemoverReserva(self, janela):
        id_reserva = janela.reservasExistentes.currentText().split(' | ')[0]
        ReservaController().remove(int(id_reserva))
        janela.menuPrincipal()
        QMessageBox.information(janela.cw, 'Ação concluida', 'Reserva removida com sucesso!')
        
class TelaVerReserva:
    
    def __init__(self, janela):
        janela.setFixedSize(600,800)
        janela.limparTela()
        
        janela.criarBtn(QLabel,'VER RESERVAS',0,3,3,12, CSS_TITLE)
        
        
    
        
        row = 3
        janela.criarBtn(QLabel,'Id',row,0,3,3, CSS_BUTTON)
        janela.criarBtn(QLabel,'preco',row,3,3,6, CSS_BUTTON)
        janela.criarBtn(QLabel,'assento',row,9,3,6, CSS_BUTTON)
        janela.criarBtn(QLabel,'origem',row,15,3,6, CSS_BUTTON)
        janela.criarBtn(QLabel,'destino',row,21,3,6, CSS_BUTTON)
        row += 3
        all_reservas = ReservaController().get_all()
        
        for reserva in all_reservas:
            janela.criarBtn(QLabel,f'{reserva.id}', row, 0, 3, 3, CSS_BUTTON)
            janela.criarBtn(QLabel,f'{reserva.preco}', row, 3, 3, 6, CSS_BUTTON)
            janela.criarBtn(QLabel,f'{reserva.assento}', row, 9, 3, 6, CSS_BUTTON)
            janela.criarBtn(QLabel,f'{reserva.voo.origem}', row, 15, 3, 6, CSS_BUTTON)
            janela.criarBtn(QLabel,f'{reserva.voo.destino}', row, 21, 3, 6, CSS_BUTTON)
            row += 3
        
        janela.criarBtn(QPushButton,'Voltar',row,0,3,6,CSS_BUTTON, janela.menuPrincipal)
        