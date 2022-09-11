class Bell:
    def __init__(self, *args, **kwargs):
        self.args = list(args)
        self.kwargs = {k: b for k, b in sorted(kwargs.items(), key=lambda x: x[0])}

    def print_info(self):
        kwargs_ret, args_ret = [], self.args
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
        self.bells = list(bells)

    def append(self, el):
        self.bells = self.bells + [el]

    def sound(self):
        for _ in self.bells:
            _.sound()
        print('...')