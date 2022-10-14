from functools import total_ordering


@total_ordering
class Point:
    def __init__(self, name, x, y):
        self.x, self.y, self.name = x, y, name

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
        if (self.name, (self.x, self.y)) == (other.name, (other.x, other.y)):
            return True
        return False

    def __lt__(self, other):
        if (self.name, (self.x, self.y)) < (other.name, (other.x, other.y)):
            return True
        return False
