class Bell:
    def __init__(self, *args, **kwargs):
        self.bells = list(args)
        self.kwargs = {k: b for k, b in sorted(kwargs.items(), key=lambda x: x[0])}

    def print_info(self):
        kwargs_ret, args_ret = [], self.bells
        if self.kwargs:
            for k, v in self.kwargs.items():
                kwargs_ret.append(f'{k}: {v}')
        if kwargs_ret and args_ret:
            print(f"{', '.join(kwargs_ret)}; {', '.join(args_ret)}".rstrip('; '))
        elif kwargs_ret and not args_ret:
            print(f"{', '.join(kwargs_ret)}")
        elif not kwargs_ret and args_ret:
            print(f"{', '.join(args_ret)}".rstrip('; '))
        else:
            print('-')


class LittleBell(Bell):
    def sound(self):
        print('ding')


class BigBell(Bell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.s = 'ding'

    def sound(self):
        print(self.s)
        if self.s == 'ding':
            self.s = 'dong'
        else:
            self.s = 'ding'


class BellTower:
    def __init__(self, *bells):
        self.bells = list(bells, )
        if type(self.bells[0]) is tuple:
            self.bells = list(*self.bells)

    def append(self, el):
        self.bells = self.bells + [el]

    def sound(self):
        for _ in self.bells:
            _.sound()
        print('...')

    def print_info(self):
        for _ in range(1, len(self.bells) + 1, 1):
            print(_, self.bells[_ - 1].__class__.__name__)
            self.bells[_ - 1].print_info()
        print()
        # if self.kwargs:


class SizedBellTower(BellTower):
    def __init__(self, *bells, size=10):
        ambi = len(bells) - size
        super().__init__(tuple(bells[ambi if ambi >= 0 else 0:]))
        self.size = size

    def append(self, el):
        if len(self.bells) == self.size:
            self.bells = self.bells[1:] + [el]
        else:
            self.bells = self.bells + [el]


class TypedBellTower(BellTower):
    def __init__(self, *bells, bell_type=LittleBell):
        super().__init__(tuple(list(filter(lambda x: isinstance(x, bell_type), bells))))
        self.bell_type = bell_type

    def append(self, el):
        if isinstance(el, self.bell_type):
            self.bells = self.bells + [el]
