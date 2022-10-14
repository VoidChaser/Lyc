import sys

from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QWidget, QPushButton


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 330, 100)
        self.setWindowTitle('Evaluating')

        self.lab_eval = QLabel(self)
        self.lab_eval.setText('Выражение:')
        self.lab_eval.move(5, 15)

        self.text_eval = QLineEdit(self)
        self.text_eval.setGeometry(0, 35, 150, 40)

        self.btn = QPushButton('->', self)
        self.btn.clicked.connect(self.Evaluate)

        self.btn.resize(30, 30)
        self.btn.move(150, 35)

        self.lab_res = QLabel(self)
        self.lab_res.setText('Результат:')
        self.lab_res.move(185, 15)

        self.text_res = QLineEdit(self)
        self.text_res.setGeometry(180, 35, 150, 40)

    def Evaluate(self):
        statement = self.text_eval.text()
        if statement:
            result = eval(statement)
        else:
            result = ''  # Предположил случай, когда выражение пустое, тогда вылетает
        self.text_res.setText(str(result))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec())
