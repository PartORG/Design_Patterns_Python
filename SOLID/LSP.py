"""
Liskov Substitution Principle
If you have some interface that takes some sort of Base Class
you should be able to stick a derived class in there
and everything should work.
"""


class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        """Getter for the width"""
        return self._width

    @width.setter
    def width(self, value):
        """Setter for the width"""
        self._width = value

    @property
    def height(self):
        """Getter for the height"""
        return self._height

    @height.setter
    def height(self, value):
        """Setter for the height"""
        self._height = value


# class that breaks LSP:
class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f'Expected an area of {expected}, got {rc.area}')


rc = Rectangle(2, 3)
use_it(rc)

# breaking LSP here
sq = Square(5)
use_it(sq)

# to fix this -- we do not need Square inherited class, just add boolean property on rectangle,
# or you can have a Factory method which will make a square instead of Rectangle