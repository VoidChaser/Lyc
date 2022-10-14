import sys
from PyQt5.QtGui import QFont

from PyQt5.QtWidgets import QApplication, QLCDNumber, QLabel, QLineEdit, QWidget, QPushButton


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 320, 100)
        self.setWindowTitle('A Rime moment R')

        self.first_num = QLineEdit(self)
        self.first_num.setGeometry(5, 10, 50, 30)

        self.plus = QPushButton('+', self)
        self.plus.setGeometry(55, 11, 30, 30)
        self.plus.clicked.connect(self.summ)

        self.minus = QPushButton('-', self)
        self.minus.setGeometry(85, 11, 30, 30)
        self.minus.clicked.connect(self.subb)

        self.mult = QPushButton('*', self)
        self.mult.setGeometry(115, 11, 30, 30)
        self.mult.clicked.connect(self.mull)

        self.second_num = QLineEdit(self)
        self.second_num.setGeometry(145, 10, 50, 30)

        self.eqv = QLabel('=', self)
        self.eqv.setGeometry(195, 20, 5, 5)

        self.eva = QLineEdit('0', self)
        self.eva.setGeometry(202, 10, 50, 30)
        self.eva.setDisabled(True)

    def summ(self):
        num1, num2 = int(self.first_num.text()), int(self.second_num.text())
        self.eva.setText(str(num1 + num2))

    def subb(self):
        num1, num2 = int(self.first_num.text()), int(self.second_num.text())
        self.eva.setText(str(num1 - num2))

    def mull(self):
        num1, num2 = int(self.first_num.text()), int(self.second_num.text())
        self.eva.setText(str(num1 * num2))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec())
