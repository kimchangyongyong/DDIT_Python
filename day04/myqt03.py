import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from Cython.Compiler.Naming import self_cname

form_class = uic.loadUiType("myqt03.ui")[0]


class MainClass(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.show()

        self.pb.clicked.connect(self.btnClick)

    def myclick(self):
        a=self.le1.text()
        b=self.le2.text()
        aa = int(a)
        bb = int(b)
        min = aa-bb
        
        self.le3.setText(str(min))
       


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainClass()
    app.exec_()


        
