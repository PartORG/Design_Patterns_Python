"""
Proxy Pattern.

Virtual. It is similar to original object
but can provide additional functionality
and act similarly or differently.

"""


class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        # expensive process
        print(f'Loading image from {self.filename}')

    def draw(self):
        print(f'Drawing image {self.filename}')


# Virtual proxy
class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()


def draw_image(image):
    print('About to draw image.')
    image.draw()
    print('Done drawing an image.')


if __name__ == '__main__':
    bmp = Bitmap('facepalm.jpg')
    draw_image(bmp)

    # How can we avoid loading the image
    # if we do not drawing it?

    lbmp = LazyBitmap('Lazy_facepalm.jpg')
    draw_image(lbmp)
    draw_image(lbmp)  # loading image is done only ones
