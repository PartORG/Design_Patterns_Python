"""
Bridge Coding Exercise

You are given an example of an inheritance hierarchy
which results in Cartesian-product duplication.

Please refactor this hierarchy, giving the base class Shape
a constructor that takes an interface Renderer  defined as

class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None

as well as VectorRenderer  and RasterRenderer  classes.
Each inheritor of the Shape  abstract class should have a constructor
that takes a Renderer  such that, subsequently,
each constructed object's __str__()  operates correctly, for example,

str(Triangle(RasterRenderer()) # returns "Drawing Triangle as pixels"
"""
from abc import ABC


# class Shape:
#     def __init__(self):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None

# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer


class VectorRenderer(Renderer):
    def what_to_render_as(self):
        return 'lines'


class RasterRenderer(Renderer):
    def what_to_render_as(self):
        return 'pixels'


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer
        self.name = None

    def __str__(self):
        return f'Drawing {self.name} as {self.renderer.what_to_render_as()}'


class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Triangle'


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Square'


if __name__ == '__main__':
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()

    vector_square = Square(vector_renderer)
    raster_square = Square(raster_renderer)
    vector_triangle = Triangle(vector_renderer)
    raster_triangle = Triangle(raster_renderer)

    print(vector_square)  # Output: Drawing lines Square
    print(raster_square)  # Output: Drawing pixels Square
    print(vector_triangle)  # Output: Drawing lines Triangle
    print(raster_triangle)  # Output: Drawing pixels Triangle