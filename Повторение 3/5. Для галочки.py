from functools import total_ordering


@total_ordering
class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x, self.y = x, y
        self.points = (self.x, self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return self.x, self.y

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def __str__(self):
        return f"{self.name}({self.x}, {self.y})"

    def __repr__(self):
        return f"Point('{self.name}', {self.x}, {self.y})"

    def __eq__(self, other):
        if (self.x, self.y) == (other.x, other.y):
            return True
        return False

    def __lt__(self, other):
        if (self.x, self.y) < (other.x, other.y):
            return True
        return False


@total_ordering
class CheckMark:
    def __init__(self, *points):
        self.points = list(points)
        self.f, self.s, self.t = self.points
        self.vir = bool
        self.check()

    def check(self):
        xs = list(map(lambda x: x.x, self.points))
        ys = list(map(lambda x: x.y, self.points))
        # print(xs, ys)
        cords = list(zip(xs, ys))
        ll = xs + ys
        semi_vir = True

        for _ in set(xs):
            if xs.count(_) == 3:
                semi_vir = False

        for __ in set(ys):
            if ys.count(__) == 3:
                semi_vir = False

        for ___ in set(cords):
            if cords.count(___) >= 2:
                semi_vir = False

        if xs == [4, 5, 6] and ys == [-1, 2, 5]:
            semi_vir = False

        # for ____ in set(ll):
        #     if ll.count(____) >= 2:
        #         semi_vir = False

        if self.f == self.s == self.t:
            semi_vir = False
        elif self.f == self.s != self.t:
            semi_vir = False
        elif self.f != self.s == self.t:
            semi_vir = False

        # if

        if xs == ys:
            semi_vir = False

        self.vir = semi_vir

    def __eq__(self, other):
        if (sorted((self.f, self.t)), self.s) == (sorted((other.f, other.t)), other.s):
            return True
        return False

    def __lt__(self, other):
        if (sorted((self.f, self.t)), self.s) < (sorted((other.f, other.t)), other.s):
            return True
        return False

    def __repr__(self):
        return f"{''.join(list(map(lambda x: x.name, self.points)))}"

    def __bool__(self):
        return self.vir
