from abc import ABC, abstractmethod


class Engine2D:
    """
    The class allows you to draw shapes on the canvas. The canvas is a list of instances of shape classes.
    Shapes must be subclasses of the Shape class and have a method draw(). The class allows you to set the color
    of a shape, but can also draw without specifying a color.
    """
    def __init__(self):
        self.canvas = []
        self.color = ''

    def add_shape(self, shape):
        self.shape = shape
        if issubclass(type(self.shape), Shape):
            self.canvas.append(self.shape)
        else:
            raise ValueError('Argument must be subclass of the Shape class')

    def add_shapes(self, *args):
        self.shapes = args
        if len(self.shapes) < 1:
            raise ValueError('No arguments passed')
        elif not all([issubclass(type(i), Shape) for i in self.shapes]):
            raise ValueError('Arguments must be subclasses of the Shape class')
        else:
            [self.canvas.append(i) for i in self.shapes]

    def draw(self):
        if all([issubclass(type(i), Shape) for i in self.canvas]):
            for shape in self.canvas:
                if self._check_color():
                    shape.draw()
                else:
                    print(f'Color: {self.color}. ', end='')
                    shape.draw()
            self.canvas = []
        else:
            self.canvas = []
            raise TypeError('Arguments must be subclasses of the Shape class')

    def set_color(self, color):
        self.color = color
        if not self._validate_color():
            raise TypeError('The type of the argument "color" must be a string')

    def _validate_color(self):
        return isinstance(self.color, str)

    def _check_color(self):
        return self.color == ''


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        if self._validate_circle():
            print(f'Drawing {self.__class__.__name__}: A{(self.x, self.y)} with radius {self.radius}')
        else:
            raise ValueError("Can't draw a circle with the given arguments")

    def _validate_circle(self):
        return all([type(i) in (int, float) for i in (self.x, self.y, self.radius)]) and self.radius > 0


class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def draw(self):
        if self._validate_triangle():
            print(f'Drawing {self.__class__.__name__}: A{self.x1, self.y1}, B{self.x2, self.y2}, C{self.x3, self.y3}')
        else:
            raise ValueError("Can't draw a triangle with the given arguments")

    def _validate_triangle(self):
        return all([type(i) in (int, float) for i in (self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)]) \
            and (self.x1, self.y1) != (self.x2, self.y2) and (self.x1, self.y1) != (self.x3, self.y3) \
            and (self.x1, self.y1) != (self.x3, self.y3)


class Rectangle(Shape):
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def draw(self):
        if self._validate_rectangle():
            print(f'Drawing {self.__class__.__name__}: A{self.x, self.y}, B{self.x + self.width, self.y}, '
                  f'C{self.x + self.width, self.y + self.height}, D{self.x, self.y + self.height}')
        else:
            raise ValueError("Can't draw a rectangle with the given arguments")

    def _validate_rectangle(self):
        return all([type(i) in (int, float) for i in (self.x, self.y, self.height, self.width)]) \
            and self.height != 0 and self.width != 0


if __name__ == '__main__':
    c = Circle(0, 1, 5)
    t = Triangle(1, 1, 3, 1, 2, 5)
    r = Rectangle(0, 0, 10, 10)
    engine = Engine2D()

    engine.add_shapes(c, t, r)
    engine.set_color('red')
    engine.draw()

    print('-' * 75)

    engine.add_shapes(c, t, r)
    engine.set_color('')
    engine.draw()

    print('-' * 75)

    engine.add_shapes(c, t, r)
    engine.set_color('black')
    engine.draw()
