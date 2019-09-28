import sys
import test
import saveDiag
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *
from PyQt5 import QtWidgets, uic
import os
import encrypt
import hashlib
import base64
from cryptography.fernet import Fernet
import FileExp



class Button():

    def __init__(self,bname,tip,icon):

        self.bname = bname
        self.Create_button = QPushButton(bname)
        self.tip=tip
        self.Create_button.setToolTip(tip)
        self.icon = icon
        self.Create_button.setIcon(QIcon(icon))
        self.Create_button.setIconSize(QSize(20,20))

        self.Create_button.clicked.connect(lambda: window.handleInput(self.bname))





class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.top = 50
        self.left = 50
        self.width = 1200
        self.height = 600

        self.InitUi()

    def InitUi(self):
        self.setWindowTitle("Crypto Cipher")
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.setStyleSheet("background-color:darkcyan")
        self.setWindowIcon(QIcon("key.png"))


        gbox = QGroupBox("Quick Access")
        gbox.resize(20,50)
        vertigbox = QVBoxLayout()
        verti = QVBoxLayout()
        hori_main = QHBoxLayout()

        #hori.setContentsMargins(0,0,0,0)
        #hori.setSpacing(0)

        self.mainMenu = QMenuBar()
        fileMenu = self.mainMenu.addMenu("File")
        viewMenu = self.mainMenu.addMenu("View")
        editMenu = self.mainMenu.addMenu("Edit")
        searchMenu = self.mainMenu.addMenu("Search")
        toolMenu = self.mainMenu.addMenu("Tools")
        helpMenu = self.mainMenu.addMenu("Help")

        #Menu Actions
        new_file = QAction(QIcon("file.png"), "New File", self)
        new_file.setShortcut("Ctrl+N")
        fileMenu.addAction(new_file)
        new_file.triggered.connect(self.newFileClicked)

        save_file = QAction(QIcon("document.png"), "Save File", self)
        save_file.setShortcut("Ctrl+S")
        fileMenu.addAction(save_file)
        save_file.triggered.connect(self.ADDClicked)

        open_file = QAction(QIcon("opened.png"), "Open File", self)
        open_file.setShortcut("Ctrl+O")
        fileMenu.addAction(open_file)
        open_file.triggered.connect(self.OpenFile)


        exit_button = QAction(QIcon("exiticon"),'Exit',self)
        exit_button.setShortcut("Ctrl+E")
        exit_button.setStatusTip("Exit Application")
        exit_button.triggered.connect(self.Close)
        fileMenu.addAction(exit_button)

        viewStatusBar = QAction(QIcon("menu.png"), "Status Bar",self, checkable = True,)
        viewStatusBar.setStatusTip("Show Status bar")
        viewStatusBar.setChecked(True)
        viewStatusBar.triggered.connect(self.toggleStatusBar)
        viewMenu.addAction(viewStatusBar)

        encryptAction = QAction(QIcon("lock.png"), "Encrypt File", self)
        encryptAction.setStatusTip("Encrypt Current file")
        encryptAction.triggered.connect(self.Encrypt)
        editMenu.addAction(encryptAction)

        decryptAction = QAction(QIcon("padlock.png"), "Decrypt File", self)
        decryptAction.setStatusTip("Decrypt Current file")
        decryptAction.triggered.connect(self.Decrypt)
        editMenu.addAction(decryptAction)

        searchAction = QAction(QIcon("search.png"), "Search", self)
        toolMenu.addAction(searchAction)


        #status bar
        self.status_bar = QStatusBar()
        self.status_bar.showMessage("App is Ready")


        # toolbar
        toolbar = QToolBar("Toolbar")
        toolbar.setIconSize(QSize(25,25))
        #toolbar.setStyleSheet("backgroundcolor = blue")
        toolbar.addSeparator()
        toolbar.addAction(new_file)
        toolbar.addAction(save_file)
        toolbar.addAction(open_file)
        toolbar.addAction(viewStatusBar)
        toolbar.addAction(encryptAction)
        toolbar.addAction(decryptAction)
        toolbar.addAction(searchAction)
        toolbar.addSeparator()
        toolbar.addAction(exit_button)

        verti.addWidget(self.mainMenu)
        verti.addWidget(toolbar)

        #TextBoxEdit
        self.textEdit = QTextEdit()
        self.textEdit.setFontWeight(10)
        self.textEdit.setFontPointSize(14.4)
        hori_main.addWidget(self.textEdit)

        #Quick Access Butons
        buttons = ["New File","Encrypt","Decrypt","Settings","Open","Search", "About","Exit"]
        tooltips = ["Add new entry", "Into Secret Codes", "Into Simple msg", "See the Stats", "Open a file",
                    "Search","Details about", "Exit the App"]

        icons = ["file.png", "lock.png", "padlock.png", "settings.png", "opened.png","search.png", "about.png", "cancel.png"]



        i = 0
        for button in buttons:
            bobj = Button(button,tooltips[i],icons[i])
            vertigbox.addWidget(bobj.Create_button)
            i+=1
        #vertigbox.addStretch()
        #hori2 = QHBoxLayout()
        #hori2.addWidget(self.status_bar)
        vertigbox.addStretch()
        vertigbox.setSpacing(0)
        gbox.setLayout(vertigbox)
        verti.addLayout(hori_main)

        hori_main.addWidget(gbox)
        verti.addWidget(self.status_bar)

        self.setLayout(verti)

        print("stats ",self.status_bar.getContentsMargins())
        print("man ",self.mainMenu.getContentsMargins())
        print("tool",toolbar.getContentsMargins())

        self.show()


     #handleing inputs of buttons
    def handleInput(self,txt):
        if txt == "Exit":
            self.Close()
        elif txt == "About":
            self.AboutClicked()
        elif txt == "Profit":
            self.OpenClicked()
        elif txt == "New File":
            self.ADDClicked()
        elif txt == "Encrypt":
            self.Encrypt()
        elif txt == "Decrypt":
            self.Decrypt()
        elif txt == "Open":
            self.OpenFile()
        else:
            pass

    #Menu ACtions toggling status bar
    def toggleStatusBar(self,state):
        if state:
            self.status_bar.show()
        else:
            self.status_bar.hide()

    # input FUNCTIONS

    def ADDClicked(self):

        self.saveWind = saveDiag.MyWindow()
        #self.saveWind.show()
        self.saveWind.saveButton.clicked.connect(self.SaveClicked)
        self.saveWind.cancelButton.clicked.connect(self.Cancel)

    def SaveClicked(self):

        outfile = self.saveWind.save_loc.text() +'\\'+ self.saveWind.file_name.text()
        self.TextFile(outfile,self.textEdit.toPlainText())
        self.saveWind.close()
        self.status_bar.showMessage("File Saved")
    def Cancel(self):

        self.saveWind.close()



    def TextFile(self, filedetail,file_data):
        txtfile = open(filedetail, 'w')
        txtfile.write(file_data)
        txtfile.close()



    def newFileClicked(self):
        self.textEdit.clear()
        self.status_bar.showMessage("File Not Saved")



        #self.savediag.saveButton.clicked.connect(self.AboutClicked)


    def Close(self):
        reply = QMessageBox.question(self ,"Warning", "Are you sure to close",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()


    def AboutClicked(self):
        msg = QMessageBox()
        msg.about(self,"About"," This SW is Being Developed by Himanshu Sharma")

        pass
    def OpenClicked(self):
        message = QMessageBox.question(self,"Question Message", "Do You Want To Learn How To Earn Profit?",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if message == QMessageBox.Yes:
            print("Yes teach")
        else:
            print("No need")


    def Encrypt(self):
        self.keyDiag = encrypt.KeyDialog()
        self.keyDiag.okButton.clicked.connect(self.GettingKey)
        self.keyDiag.cancelButton.clicked.connect(self.Cancel2)

    def GettingKey(self):

        keyword = self.keyDiag.key_line_edit.text()
        self.msg = self.textEdit.toPlainText()
        keyword = keyword.encode()
        key = hashlib.sha3_256(keyword)
        digestkey = key.digest()
        key_bytes = key.digest()
        fernet_key = base64.urlsafe_b64encode(key_bytes)
        custom_cipher = Fernet(fernet_key)



        encrypted_msg = custom_cipher.encrypt(self.msg.encode())
        decrypted_msg = custom_cipher.decrypt(encrypted_msg)
        self.msg = decrypted_msg.decode()

        self.textEdit.setText(encrypted_msg.decode())

        self.keyDiag.close()
        self.status_bar.showMessage("This is Your encrypted message, dont forget to save it!!")

    def Cancel2(self):
        self.keyDiag.close()

    def Decrypt(self):
        self.keyDiag = encrypt.KeyDialog()
        self.keyDiag.okButton.clicked.connect(self.GivingKey)
        self.keyDiag.cancelButton.clicked.connect(self.Cancel2)

    def GivingKey(self):
        try:
            keyword = self.keyDiag.key_line_edit.text()
            msg = self.textEdit.toPlainText()
            msg = msg.encode()
            keyword = keyword.encode()
            key = hashlib.sha3_256(keyword)
            digestkey = key.digest()
            key_bytes = key.digest()
            fernet_key = base64.urlsafe_b64encode(key_bytes)
            custom_cipher = Fernet(fernet_key)

            #encrypted_msg = custom_cipher.encrypt(self.msg.encode())
            decrypted_msg = custom_cipher.decrypt(msg)
            msg = decrypted_msg.decode()
            # print(self.msg)
            # print(encrypted_msg)
            self.textEdit.setText(msg)

            self.keyDiag.close()
            self.status_bar.showMessage("This is Your Decrypted message, dont forget to save it!!")

        except:
            #self.status_bar.showMessage("You Have Entered Wrong Key")
            #self.keyDiag.cancelButton.clicked.connect(lambda :self.status_bar.showMessage("Try to Remember the key"))
            self.keyDiag.close()
            Errormsg = QMessageBox()
            Errormsg.about(self, "Wrong Key", " You Have Entered Worng Key")

    def OpenFile(self):
        self.fileExpobj = FileExp.TreeView()
        self.fileExpobj.openButton.clicked.connect(self.readFile)
        self.fileExpobj.cancelButton.clicked.connect(self.openFileWindowClose)

    def readFile(self):
        try:
            index = self.fileExpobj.treeView.currentIndex()

            file_path = self.fileExpobj.model.filePath(index)

            #file_info = self.model.fileInfo(index)
            opened_file = open(file_path,'r')
            opened_file_data = opened_file.read()
            #print(self.opened_file_data)
            #os.startfile(file_path)
            self.textEdit.setText(opened_file_data)
            self.fileExpobj.close()
        except:
            #self.status_bar.showMessage("Choose a file")
            self.fileExpobj.statusbar.showMessage("Choose A File")
    def openFileWindowClose(self):
        self.fileExpobj.close()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())


