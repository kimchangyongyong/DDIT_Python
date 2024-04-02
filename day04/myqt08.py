import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("myqt08.ui")[0]

class WindowClass(QMainWindow, form_class):
    com=int(random()*99+1)
    
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        print(self.com)
        mine= self.le.text()
        str_new = ""
        
        
        if self.com>int(mine) :
            str_new += "{}보다 up\n".format(mine)
        elif self.com<int(mine) :
            str_new += "{}보다 down\n".format(mine)
        else :
            str_new += "{}정답입니다.\n".format(mine)
            
        str_old = self.pte.toPlainText()
        
        self.pte.setPlainText(str_new+str_old)     

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()