"""
Bridge Pattern.

Connecting components together through abstractions.

Bridge - a mechanism that decouples an interface (hierarchy)
from an implementation (hierarchy).

It violates OCP.
"""
from abc import ABC


# draw circle square
# render them in rastre and vector form


# one approach: create 4 classes:
# VectorCircle, VectorSquare, RasterCircle and RasterSquare.
# Such approach does not SCALE!
# end up with complexity explosions!


class Renderer(ABC):
    def render_circle(self, radius):
        pass

    # render_square ...


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for a circle of radius {radius}')


class Shape:
    # this is basic bridge implementation
    def __init__(self, renderer):
        self.renderer = renderer
    
    def draw(self):
        pass
    
    def resize(self, factor):
        pass
    

class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius
        
    def draw(self):
        # use Bridge here
        self.renderer.render_circle(self.radius)
        
    def resize(self, factor):
        self.radius *= factor


if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    # for vector
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()

    # for raster
    circle = Circle(raster, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
