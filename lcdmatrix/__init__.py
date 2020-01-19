from PySide2.QtWidgets import QWidget, QGridLayout, QLCDNumber


class LCDMatrix(QWidget):
    def __init__(self, parent, x,y):
        super(LCDMatrix, self).__init__(parent)
        layout = QGridLayout()
        self.values = {}
        for j in range(y):
            self.values[j] = {}
            for i in range(x):
                print( f"keys: y={j}  x:{i}")
                self.values[j][i] = QLCDNumber()
                layout.addWidget(self.values[j][i], i,j)

        parent.setLayout(layout)

    def setValue(self, x,y,val):
        n = val + self.values[y][x].value()
        self.values[y][x].display(n)
