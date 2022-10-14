import sys
from PyQt5.QtGui import QFont

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLCDNumber, QLabel, QLineEdit, QWidget, QPushButton, QVBoxLayout, \
    QRadioButton


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.ng = False
        self.setGeometry(0, 0, 260, 300)
        self.setWindowTitle('Tik Tak Toe')

        self.rb_cross = QRadioButton('X', self)
        self.rb_cross.toggle()
        self.current_state = ''
        self.rb_cross.setGeometry(90, 10, 40, 20)
        self.rb_o = QRadioButton('O', self)
        self.rb_o.setGeometry(145, 10, 40, 20)

        self.new_game = QPushButton('Начать новую игру', self)
        self.new_game.setGeometry(50, 250, 150, 20)

        self.result = QLabel(self)
        self.result.setGeometry(95, 220, 150, 20)

        self.hod = QLabel('Ходит: O', self)
        self.hod.setGeometry(95, 205, 150, 20)

        self.new_game.clicked.connect(self.do_new_game)

        self.matrix = [['', '', ''], ['', '', ''], ['', '', '']]
        self.vertical = QVBoxLayout()
        self.horizontal = QHBoxLayout()
        self.buttons = []

        x, y, width = 50, 50, 50
        for _ in range(3):
            a = QPushButton(self)
            a.point = (0, _)
            a.setGeometry(x, y, width, 50)
            a.clicked.connect(self.do_cross_o)
            self.buttons.append(a)
            self.buttons.append(a)
            self.horizontal.addWidget(a)
            x = x + 50

        x, y = 50, y + 50

        for _ in range(3):
            a = QPushButton(self)
            a.point = (1, _)
            a.setGeometry(x, y, width, 50)
            a.clicked.connect(self.do_cross_o)
            self.buttons.append(a)
            self.horizontal.addWidget(a)
            x = x + 50

        x, y = 50, y + 50

        for _ in range(3):
            a = QPushButton(self)
            a.point = (2, _)
            a.setGeometry(x, y, width, 50)
            a.clicked.connect(self.do_cross_o)
            self.buttons.append(a)
            self.horizontal.addWidget(a)
            x = x + 50

        self.vertical.addItem(self.horizontal)
        self.check()

    def take_current_state(self):
        self.current_state = 'X' if self.rb_cross.isChecked() else 'O'

    def check_hod(self):
        if self.current_state == '':
            self.take_current_state()
            self.hod.setText(f"Ходит: {self.current_state}")

    def do_cross_o(self):
        self.check_hod()
        point = self.sender().point
        self.sender().setText(self.current_state)
        self.matrix[point[0]][point[1]] = self.current_state
        self.current_state = 'X' if self.current_state == 'O' else 'O'
        self.check()

    def check(self):

        self.hod.setText(f"Ходит: {self.current_state}")
        m = self.matrix
        f_h, s_h, t_h, f_v, s_v, t_v, lr_dia, rl_dia = m[0], m[1], m[2], list(map(lambda x: x[0], m)), list(
            map(lambda x: x[1], m)), list(map(lambda x: x[2], m)), [m[0][0], m[1][1], m[2][2]], [m[0][2], m[1][1],
                                                                                                 m[2][0]]
        lines = [f_h, s_h, t_h, f_v, s_v, t_v, lr_dia, rl_dia]
        usl_win = list(filter(lambda x: len(set(x)) == 1 and list(set(x)) != [''], lines))
        usl_tie = all(list(map(lambda x: '' not in x, lines)))
        if usl_tie:
            self.result.setText('Ничья!')
            self.ng = True
        elif usl_win:
            self.result.setText('Выиграл ' + str(usl_win[0][0]) + '!')
            self.ng = True
        if self.ng:
            self.hod.setText('')
            self.current_state = ''
            for ___ in self.buttons:
                ___.setEnabled(False)

    def do_new_game(self):

        self.ng = False
        self.result.setText('')
        for ___ in self.buttons:
            ___.setText('')
            self.matrix = self.matrix = [['', '', ''], ['', '', ''], ['', '', '']]
            ___.setEnabled(True)
        self.check()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec())
