import sys
from PyQt5.QtGui import QFont

from PyQt5.QtWidgets import QApplication, QLCDNumber, QLabel, QLineEdit, QWidget, QPushButton


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 450, 150)
        self.setWindowTitle('Манякалькулятор')

        self.first_num = QLabel(self)
        self.first_num.setText('Первое число(целое):')
        self.first_num.move(10, 15)
        self.first_num.setFont(QFont('Arial', 12))

        self.text_num1 = QLineEdit(self)
        self.text_num1.setGeometry(10, 35, 100, 20)

        self.second_num = QLabel(self)
        self.second_num.setText('Второе число(целое):')
        self.second_num.move(10, 80)
        self.second_num.setFont(QFont('Arial', 12))

        self.text_num2 = QLineEdit(self)
        self.text_num2.setGeometry(10, 100, 100, 20)

        self.button = QPushButton(self)
        self.button.clicked.connect(self.evaluate)
        self.button.move(120, 50)
        self.button.setGeometry(130, 50, 80, 25)
        self.button.setText('->')
        self.button.setFont(QFont('Arial', 14))

        self.lcd_sum = QLCDNumber(self)
        self.lcd_sum.setGeometry(330, 10, 100, 30)

        self.text_sum = QLabel(self)
        self.text_sum.setText('Cумма:')
        self.text_sum.move(260, 15)
        self.text_sum.setFont(QFont('Arial', 12))

        self.lcd_sub = QLCDNumber(self)
        self.lcd_sub.setGeometry(330, 40, 100, 30)

        self.text_sub = QLabel(self)
        self.text_sub.setText('Разность:')
        self.text_sub.move(250, 45)
        self.text_sub.setFont(QFont('Arial', 12))

        self.lcd_mul = QLCDNumber(self)
        self.lcd_mul.setGeometry(330, 70, 100, 30)

        self.text_mul = QLabel(self)
        self.text_mul.setText('Произведение:')
        self.text_mul.move(220, 75)
        self.text_mul.setFont(QFont('Arial', 12))

        self.lcd_div = QLCDNumber(self)
        self.lcd_div.setGeometry(330, 100, 100, 30)

        self.text_div = QLabel(self)
        self.text_div.setText('Частное:')
        self.text_div.move(255, 105)
        self.text_div.setFont(QFont('Arial', 12))

    def evaluate(self):
        num1, num2 = int(self.text_num1.text()), int(self.text_num2.text())
        summ = num1 + num2
        subb = num1 - num2
        mull = num1 * num2
        divv = float(num1) / float(num2) if num2 != 0 else 'Error'
        self.lcd_sum.display(summ)
        self.lcd_sub.display(subb)
        self.lcd_mul.display(mull)
        self.lcd_div.display(divv)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec())
