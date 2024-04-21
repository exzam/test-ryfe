# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit)

from instr import *
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_apper()
        self.initUI()
        self.connects()
        self.show()
        def set_apper(self):
            self.setWindowTitle('')
            self.resise(win_width, win_height)
            self.move(win_width, win_height)
        def initUI(self):
            btn1 = QPushButton(txt_starttest1)
            self.h_line = QHBoxLayout()
            self.r_line = QVBoxLayout()
            self.l_line = QVBoxLayout()
        def connects(self):
            pass
    