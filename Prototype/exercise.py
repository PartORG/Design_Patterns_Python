"""
Prototype Coding Exercise
Given the definitions shown in code,
you are asked to implement Line.deep_copy()
to perform a deep copy of the given Line  object.
This method should return a copy of a Line
that contains copies of its start/end points.

Note: please do not confuse deep_copy() with __deepcopy__()!
"""
import copy


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        start_copy = Point(self.start.x, self.start.y)
        end_copy = Point(self.end.x, self.end.y)
        return Line(start_copy, end_copy)


if __name__ == '__main__':
    point1 = Point(0, 0)
    point2 = Point(5, 5)
    line = Line(point1, point2)

    line_copy = line.deep_copy()

    # Modify the original line's start point
    line.start.x = 10

    # The copy remains unaffected
    print(line_copy.start.x)  # Output: 0
    print(line_copy.start.y)  # Output: 0

    print(line_copy.end.x)  # Output: 5
    print(line_copy.end.y)  # Output: 5

