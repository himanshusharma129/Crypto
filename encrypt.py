import hashlib
import base64
from PyQt5.QtWidgets import QDialog,QHBoxLayout,QPushButton,QLineEdit,QLabel,QVBoxLayout
from PyQt5.QtGui import *
from cryptography.fernet import Fernet


class KeyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enter The Custom Key")
        self.setWindowIcon(QIcon("lock.png"))
        self.setGeometry(200,200,300,100)

        self.ver = QVBoxLayout()

        self.Hlayout1 = QHBoxLayout()
        self.Hlayout2 = QHBoxLayout()

        self.key_line_edit = QLineEdit()
        self.okButton = QPushButton("OK")
        self.cancelButton = QPushButton("Cancel")
        self.label = QLabel("Enter Key")
        self.Hlayout1.addWidget(self.label)
        self.Hlayout1.addWidget(self.key_line_edit)
        self.Hlayout2.addWidget(self.okButton)
        self.Hlayout2.addWidget(self.cancelButton)

        self.ver.addLayout(self.Hlayout1)
        self.ver.addLayout(self.Hlayout2)
        self.setLayout(self.ver)


        self.show()
