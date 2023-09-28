"""
Facade Pattern.

Exposing several components through
a single interface.

Facade - provides a simple, easy to understand/user interface
over a large and sophisticated body of code.

It hides all the complexity.
"""


class Buffer:
    def __init__(self, width=30, height=20):
        self.width = width
        self.height = height
        self.buffer = [' ']* (width*height)

    def __getattr__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.buffer += text


class Viewport:
    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offset = 0

    def get_character_at(self, index):
        return self.buffer[index + self.offset]

    def append(self, text):
        self.buffer.write(text)


# facade
class Console:
    """Makes everything usable."""
    def __init__(self):
        b = Buffer()
        self.current_viewport = Viewport(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    def write(self, text):
        self.current_viewport.buffer.write(text)

    def get_char_at(self, index):
        return self.current_viewport.get_character_at(index)


if __name__ == '__main__':
    c = Console()
    c.write('hello')
    ch = c.get_char_at(0)
