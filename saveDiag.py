from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import uic


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('savediag.ui', self)
        self.setWindowIcon(QIcon("plus.png"))
        self.save_loc.setText("D:\educational")


        self.show()