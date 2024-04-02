import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("myqt06.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        
        mine = self.le_mine.text()
        
        com = random()

        if com>0.5 :
            com="홀"
        else :
            com="짝"

        self.le_com.setText(com)
        
        if com==mine :
            self.le_result.setText("이김")
        else :
            self.le_result.setText("짐")
       

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()