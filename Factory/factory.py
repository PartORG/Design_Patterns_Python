"""
Factory Pattern.

Factory -- is essentially the idea of implementation of the idea of SRP.
And that is the idea that ones you get too many factory methods
inside the class it might make sense to move them out of the class
or at least to try and group them somehow into a separate entity.
And of course in context of OOP language is that entity is in most cases is a class!
"""

import math
from enum import Enum


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    """Specify in the documentation that there is a PointFactory.
        Like in other languages the Factory class can be an inner class.
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    #  Inconvenient and breaks OCP
    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * math.cos(b)
    #         self.y = a * math.sin(b)

    class PointFactory:
        """ Inside of Point Class"""
        def new_cartesian_point(self, x, y):
            """Factory method. This static method will initialise object for you."""
            p = Point()
            p.x = x
            p.y = y
            return p

        def new_polar_point(self, rho, theta):
            """Factory method. This static method will initialise object for you."""
            return Point(rho * math.cos(theta), rho * math.sin(theta))

    # singleton instance of PointFactory
    factory = PointFactory()


# OUTSIDE THE CLASS
# class PointFactory:
#     @staticmethod
#     def new_cartesian_point(x, y):
#         """Factory method. This static method will initialise object for you."""
#         p = Point()
#         p.x = x
#         p.y = y
#         return p
#
#     @staticmethod
#     def new_polar_point(rho, theta):
#         """Factory method. This static method will initialise object for you."""
#         return Point(rho * math.cos(theta), rho * math.sin(theta))


if __name__ == '__main__':
    p = Point(2, 3)
    p2 = Point.factory.new_polar_point(1, 2)
    print(p)
    print(p2)
