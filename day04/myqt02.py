import sys
from PyQt5.QtWidgets import QMainWindow,  QApplication
from PyQt5 import uic

form_class = uic.loadUiType("myqt02.ui")[0]


class MainClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.Click)
        self.show()

    def myClick(self):
        a=self.le.text() 
        aa = int(a)
        aa = aa*2
        self.le.setText(str(aa))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainClass()
    app.exec_()


        
