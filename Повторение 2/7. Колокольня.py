class BellTower:
    def __init__(self, *bells):
        self.bells = list(bells)

    def append(self, el):
        self.bells = self.bells + [el]

    def sound(self):
        for _ in self.bells:
            _.sound()
        print('...')


class LittleBell:
    def sound(self):
        print('ding')


class BigBell:
    def __init__(self):
        self.s = 'ding'

    def sound(self):
        print(self.s)
        if self.s == 'ding':
            self.s = 'dong'
        else:
            self.s = 'ding'
            
