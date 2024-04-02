import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
from Cython.Compiler.Naming import self_cname

form_class = uic.loadUiType("myqt08.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.pb.clicked.connect(self.myclick)
        self.show()
        self.setCom()
    
    def setCom(self):
        self.com = int(random()*99)+1
        print("self.com",self.com)
        
    def myclick(self):
        mine= self.le.text()
        imine = int(mine)
        str_new = ""
        
        if self.com>imine :
            str_new += "{}보다 up\n".format(mine)
        elif self.com<imine :
            str_new += "{}보다 down\n".format(mine)
        else :
            str_new += "{}정답입니다.\n".format(mine)
            QMessageBox.about(self,'UP&DOWN','정답입니다.')
        # QPlainTextEdit().setPlainText()
        str_old = self.pte.toPlainText()
        
        self.pte.setPlainText(str_new+str_old) 
        self.le.setText("")    
        
        

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()