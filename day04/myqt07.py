import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("myqt07.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):

        a=self.sb_first.value()
        b=self.sb_last.value()
   
        txt=""
        
        for i in range(a,b+1) :
            txt +="*"*i
            txt +="\n" 
        self.te.setPlainText(txt)
        
        
            

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()