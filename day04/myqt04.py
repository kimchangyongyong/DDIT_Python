import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("myqt04.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.pb.clicked.connect(self.myclick)
    
        
    def myclick(self):
        
        # a=self.le.text() 
        # aa = int(a)
        # aa = aa*2
        # self.le.setText(str(aa))
        
        gugu =self.te.toPlainText()
        dan = int(gugu)
        txt=""
      
        for i in range(1,9+1) :
            txt+="{}*{}={}\n".format(dan,i,i*dan)
            
        self.pte.setPlainText(txt)      
       
            
        

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()