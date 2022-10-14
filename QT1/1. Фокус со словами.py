import sys

from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QPushButton


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 300, 25)
        self.setWindowTitle('Focus')
        self.state = True
        self.btn = QPushButton('->', self)
        self.btn.resize(100, 25)
        self.btn.move(100, 0)

        self.btn.clicked.connect(self.count)

        self.text1 = QLineEdit('Self Political views', self)
        self.text1.setGeometry(0, 0, 100, 25)

        self.text2 = QLineEdit('', self)
        self.text2.setGeometry(200, 0, 300, 25)

    def count(self):
        if self.state:
            self.btn.setText('<-')
            self.state = False
            text = self.text1.text()
            self.text2.setText(text)
            self.text1.setText('')
        else:
            self.btn.setText('->')
            self.state = True
            text = self.text2.text()
            self.text1.setText(text)
            self.text2.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec())