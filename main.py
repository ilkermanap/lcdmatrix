from PySide.QtGui import *
from PySide.QtCore import *
from ui_lcdmatrix import Ui_Dialog
import sys
import random, time

class LCDMatrix(QWidget):
    def __init__(self, parent, x,y):
        super(LCDMatrix, self).__init__(parent)
        layout = QGridLayout()
        self.values = {}
        for j in range(y):
            self.values[j] = {}
            for i in range(x):
                print "keys: y=", j, " x:",i
                self.values[j][i] = QLCDNumber()
                layout.addWidget(self.values[j][i], i,j)

        parent.setLayout(layout)

    def setValue(self, x,y,val):
        n = val + self.values[y][x].value()
        self.values[y][x].display(n)
        

class MainWindow(QDialog, Ui_Dialog):
    def __init__(self, app = None):
        super(MainWindow, self).__init__()
        self.app = app
        self.cikis_durumu = False
        self.setupUi(self)
        self.lcd = None
        self.show()
        

    def rastgele(self):
        while self.cikis_durumu == False:
            
            x = random.randint(0, int(self.lineEdit_2.text()))
            if x == int(self.lineEdit_2.text()):
                x = 0
            
            y = random.randint(0, int(self.lineEdit.text()))
            if y == int(self.lineEdit.text()):
                y = 0
            val = random.randint(1,5)
            print x,y, val
            self.lcd.setValue(x,y, val)

            QApplication.processEvents()
            time.sleep(random.randint(1,80) / 10000.0)

    def cikis(self):
        self.cikis_durumu = True
        sys.exit()

    def doldur(self):
        self.lcd = LCDMatrix(self.frame, int(self.lineEdit_2.text()), int(self.lineEdit.text()))
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow(app)
    ret = app.exec_()
    app.exit()
    sys.exit(ret)
