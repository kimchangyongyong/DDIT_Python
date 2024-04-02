import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("myqt05.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        arr = list(range(1,45+1) )

        for i in range(360):
            rnd =int(random()*45)
            a=arr[0]
            arr[0]=arr[rnd]
            arr[rnd]=a

        print(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5])
        
        self.sb1.setValue(arr[0])
        self.sb2.setValue(arr[1])
        self.sb3.setValue(arr[2])
        self.sb4.setValue(arr[3])
        self.sb5.setValue(arr[4])
        self.sb6.setValue(arr[5])
       
        

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()