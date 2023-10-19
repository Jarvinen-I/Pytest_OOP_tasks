import pytest
from Task_2.Engine import Engine2D, Shape, Circle, Triangle, Rectangle


engine = Engine2D()
c = Circle(0, 1, 5)
t = Triangle(1, 1, 3, 1, 2, 5)
r = Rectangle(0, 0, 10, 10)

shape = [c, t, r]


@pytest.mark.parametrize('shape', shape)
def test_add_shape(shape):
    """This test is needed to make sure the method add_shape() work with correct argument"""
    assert engine.add_shape(shape) is None


wrong_shape = [engine, 'Circle', object]


@pytest.mark.parametrize('wrong_shape', wrong_shape)
def test_add_wrong_shape(wrong_shape):
    """This test is needed to make sure the method add_shape() doesn't work with wrong argument"""
    with pytest.raises((TypeError, ValueError)):
        engine.add_shape(wrong_shape)


color = ['black', 'yellow', 'white']


@pytest.mark.parametrize('color', color)
def test_set_color(color):
    """This test is needed to make sure the method set_color() work with correct argument"""
    engine.set_color(color)
    assert engine.color == color


wrong_color = [111, None, Circle]


@pytest.mark.parametrize('wrong_color', wrong_color)
def test_set_wrong_color(wrong_color):
    """This test is needed to make sure the method set_color() doesn't work with wrong argument"""
    with pytest.raises(TypeError):
        engine.set_color(wrong_color)


def test_add_shapes():
    """This test is needed to make sure the method add_shapes() work with correct arguments"""
    assert engine.add_shapes(c, t, r) is None


wrong_shapes = [(c, t, Rectangle),
                (r, Engine2D, Shape),
                ('c', t, r)]


@pytest.mark.parametrize('wrong_shapes', wrong_shapes)
def test_add_wrong_shapes(wrong_shapes):
    """This test is needed to make sure the method add_shape() work with correct arguments"""
    with pytest.raises(ValueError):
        engine.add_shapes(wrong_shapes)


def test_draw():
    """This test is needed to make sure the method draw() work with correct arguments"""
    en = Engine2D()
    cc = Circle(0, 1, 5)
    tt = Triangle(1, 1, 3, 1, 2, 5)
    rr = Rectangle(0, 0, 10, 10)
    en.add_shapes(cc, tt, rr)
    assert en.draw() is None


wrong_values = [
    (c, t, 1),
    (t, r, Circle),
    ('c', t, r)
]


@pytest.mark.parametrize('wrong_values', wrong_values)
def test_draw_wrong_values(wrong_values):
    """This test is needed to make sure the method draw() doesn't work with wrong arguments"""
    engine.canvas = list(wrong_values)
    with pytest.raises(TypeError):
        engine.draw()
