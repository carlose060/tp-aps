#!/usr/bin/env python3
from pagina_inicial import Window
from PyQt6.QtWidgets import QApplication
from sys import argv




if __name__ == '__main__':


    qt = QApplication(argv)
    app = Window()
    app.show()
    qt.exec()
