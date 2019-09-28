import sys
import os

from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class TreeView(QMainWindow):
    def __init__(self):
        super(TreeView, self).__init__()

        uic.loadUi('FileEx.ui', self)
        self.setWindowTitle("Files")
        self.setWindowIcon(QIcon("opened.png"))
        self.statusbar.showMessage("Explorer")
        save_file = QAction(QIcon("document.png"), "Save File", self)
        back = QAction(QIcon("left.png"), "Back", self)
        self.toolbar.addAction(back)
        self.toolbar.addAction(save_file)

        back.triggered.connect(self.Back)



        #Telling that we are using a custom context menu
        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        #connecting the custom menu to our function
        self.treeView.customContextMenuRequested.connect(self.context_menu)
        self.populate()
        self.show()

    def populate(self):
        self.path = "D:"
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(self.path))
        #self.treeView.setSortingEnabled(True)

    def context_menu(self):
        menu = QMenu()
        self.open = menu.addAction("Open")
        self.open.triggered.connect(self.openFile)

        curser = QCursor()
        menu.exec_(curser.pos())


    def openFile(self):


        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        file_info = self.model.fileInfo(index)
        os.startfile(file_path)
        #file = open(file_path,'r')
        #self.file_data = file.read()
        #print(self.file_data)



        #os.startfile(file_path)

    def Back(self):
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())
        self.treeView.setModel(self.model)

'''
App = QApplication(sys.argv)
window = TreeView()

sys.exit(App.exec())
'''