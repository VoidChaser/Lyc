class Point():
    def __init__(self, name, x, y):
        self.x, self.y, self.name = x, y, name

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return (self.x, self.y)

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def __str__(self):
        return f'{self.name}({self.x}, {self.y})'


class ColoredPoint(Point):
    def __init__(self, name, x, y, rgb=(0, 0, 0)):
        super().__init__(name, x, y)
        self.rgb = rgb if rgb else (0, 0, 0)

    def get_color(self):
        return self.rgb

    def __invert__(self):
        return ColoredPoint(self.name, self.y, self.x, tuple(list(map(lambda x: abs(x - 255), self.rgb))))

