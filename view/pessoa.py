from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QComboBox, QLabel, QLineEdit, QPushButton


CSS_BUTTON = """
    font-size: 20px;
    width: 100%;
    height: 120%; 
"""
CSS_TITLE = 'font-size: 25px; font-weight: bold'


class TelaCadastroPessoa:
    
    def __init__(janela):
        
        janela.setFixedSize(400,300)
        janela.limparTela()
        
        janela.criarBtn(QLabel,'CADASTRO DE PESSOA',0,3,3,12, CSS_TITLE)
        
        janela.criarBtn(QLabel,'Nome:',3,0,3,6, CSS_BUTTON)
        janela.nomePessoa = janela.criarBtn(QLineEdit,'',3,7,3,10, CSS_BUTTON)
        
        janela.criarBtn(QLabel,'Idade:',6,0,3,6, CSS_BUTTON)
        janela.idadePessoa = janela.criarBtn(QLineEdit,'',6,7,3,10, CSS_BUTTON)
        janela.idadePessoa.setValidator(QIntValidator())
        
        janela.criarBtn(QLabel,'Carteira:',9,0,3,6, CSS_BUTTON)
        janela.numeroCarteira = janela.criarBtn(QLineEdit,'',9,7,3,10, CSS_BUTTON)
        
        janela.criarBtn(QLabel,'Tipo:',12,0,3,6, CSS_BUTTON)
        janela.tipoPessoa = QComboBox()
        janela.tipoPessoa.addItems(['Passageiro', 'Piloto'])
        janela.tipoPessoa.setStyleSheet("""width: 10px;height: 40%;font-size: 16px;""")
        janela.grid.addWidget(janela.tipoPessoa, 12,7,3,10)      
        
    
        janela.criarBtn(QPushButton,'Cadastrar',15,0,3,6,CSS_BUTTON, janela.concluirCadastroPessoa)
        janela.criarBtn(QPushButton,'Voltar',15,6,3,6,CSS_BUTTON, janela.telaInicial)

class TelaRemoverPessoa:
    
    def __init__(janela):
        
        janela.setFixedSize(400,300)
        janela.limparTela()
        
        janela.criarBtn(QLabel,'REMOÇÃO DE PESSOA',0,3,3,12, CSS_TITLE)
        
        janela.criarBtn(QLabel,'Nome:',3,0,3,6, CSS_BUTTON)
        janela.pessoasExistentes = QComboBox()
        janela.pessoasExistentes.addItems(janela.pessoas.get_all())
        janela.pessoasExistentes.setStyleSheet("""width: 10px;height: 40%;font-size: 16px;""")
        janela.grid.addWidget(janela.pessoasExistentes, 3, 7, 3, 10)
        
        
        janela.criarBtn(QPushButton,'Remover',7,0,3,6,CSS_BUTTON, janela.concluirRemoverPessoa)
        janela.criarBtn(QPushButton,'Voltar',7,6,3,6,CSS_BUTTON, janela.telaInicial)
        
    
class TelaVerPessoa:
    
    def __init__(janela):
        janela.setFixedSize(400,300)
        janela.limparTela()
        
        janela.criarBtn(QLabel,'VER PESSOAS',0,3,3,12, CSS_TITLE)
        
        row = 3
        janela.criarBtn(QLabel,'Id',row,0,3,5, CSS_BUTTON)
        janela.criarBtn(QLabel,'Nome',row,5,3,6, CSS_BUTTON)
        janela.criarBtn(QLabel,'Idade',row,11,3,6, CSS_BUTTON)
        janela.criarBtn(QLabel,'Tipo',row,17,3,6, CSS_BUTTON)
        row += 3
        for pessoa in janela.pessoas.pessoas:
            try: 
                _ =  pessoa.numero_carteira
                tipo = 'Piloto'
            except:
                tipo = 'Passageiro'
            
            janela.criarBtn(QLabel,str(pessoa.id),row,0,3,5, CSS_BUTTON)
            janela.criarBtn(QLabel,pessoa.nome,row,5,3,6, CSS_BUTTON)
            janela.criarBtn(QLabel,str(pessoa.idade),row,11,3,6, CSS_BUTTON)
            janela.criarBtn(QLabel,tipo,row,17,3,6, CSS_BUTTON)
            row += 3
        janela.criarBtn(QPushButton,'Voltar',row,0,3,6,CSS_BUTTON, janela.telaInicial)

    