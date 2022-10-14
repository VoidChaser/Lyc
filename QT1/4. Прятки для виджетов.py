import sys

from PyQt5.QtWidgets import QApplication, QCheckBox, QLCDNumber, QLabel, QLineEdit, QWidget, QPushButton


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 400, 150)
        self.setWindowTitle('Прятки для вивиджетов')

        self.text_pole1 = QLineEdit('Поле edit1', self)
        self.text_pole1.setGeometry(60, 5, 140, 20)

        self.text_pole2 = QLineEdit('Поле edit2', self)
        self.text_pole2.setGeometry(60, 30, 140, 20)

        self.text_pole3 = QLineEdit('Поле edit3', self)
        self.text_pole3.setGeometry(60, 55, 140, 20)

        self.text_pole4 = QLineEdit('Поле edit4', self)
        self.text_pole4.setGeometry(60, 80, 140, 20)

        self.edit1 = QCheckBox('edit1', self)
        self.edit1.setGeometry(10, 5, 50, 20)
        self.edit1.box = self.text_pole1
        self.edit1.clicked.connect(self.show_hide)

        self.edit2 = QCheckBox('edit2', self)
        self.edit2.setGeometry(10, 30, 50, 20)
        self.edit2.box = self.text_pole2
        self.edit2.clicked.connect(self.show_hide)

        self.edit3 = QCheckBox('edit3', self)
        self.edit3.setGeometry(10, 55, 50, 20)
        self.edit3.box = self.text_pole3
        self.edit3.clicked.connect(self.show_hide)

        self.edit4 = QCheckBox('edit4', self)
        self.edit4.setGeometry(10, 80, 50, 20)
        self.edit4.box = self.text_pole4
        self.edit4.clicked.connect(self.show_hide)
        self.texts = [self.text_pole1, self.text_pole2, self.text_pole3, self.text_pole4]

    def show_hide(self):
        if self.edit1.isChecked():
            self.text_pole1.hide()

        else:
            self.text_pole1.show()

        if self.edit2.isChecked():
            self.text_pole2.hide()

        else:
            self.text_pole2.show()

        if self.edit3.isChecked():
            self.text_pole3.hide()

        else:
            self.text_pole3.show()

        if self.edit4.isChecked():
            self.text_pole4.hide()

        else:
            self.text_pole4.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec())
