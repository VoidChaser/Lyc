import sys
from PyQt5.QtGui import QFont

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLCDNumber, QLabel, QLineEdit, QWidget, QPushButton, QVBoxLayout

CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..'}


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.gotten_line = QLineEdit(self)
        self.gotten_line.setGeometry(0, 40, 350, 20)
        self.initUI()

    def initUI(self):
        keyss = list(CODE.keys())

        self.setGeometry(0, 0, 400, 100)
        self.setWindowTitle('Morse Translate')
        self.vertical = QVBoxLayout()
        self.horizontal = QHBoxLayout()
        x, width = 0, 20

        for _ in keyss[:19]:
            a = QPushButton(_, self)
            a.setGeometry(x, 0, width, 20)
            a.clicked.connect(self.enter_letter)
            self.horizontal.addWidget(a)
            x += 20

        self.vertical.addItem(self.horizontal)

        self.horizontal_2 = QHBoxLayout()
        x, width = 0, 20

        for _ in keyss[16:]:
            a = QPushButton(_, self)
            a.setGeometry(x, 20, width, 20)
            a.clicked.connect(self.enter_letter)
            self.horizontal.addWidget(a)
            x += 20

        self.vertical.addItem(self.horizontal_2)

    def enter_letter(self, letter):
        charr = self.sender().text()
        old_text = self.gotten_line.text()
        self.gotten_line.setText(old_text + CODE[charr])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec())
