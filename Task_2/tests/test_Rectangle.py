import pytest
from Task_2.Engine import Rectangle, Shape


def test_rectangle_is_subclass_of_shape():
    """This test is needed to make sure that the class 'Rectangle' has a method draw()"""
    assert issubclass(Rectangle, Shape)


values = [(0, 0, 10, 10),
          (1, 2, -3, 2),
          (-1, 2, 3, -2),
          (-1.5, 2, 3.0, -2)]


@pytest.mark.parametrize('values', values)
def test_rectangle_good(values):
    """This test is needed to make sure the method draw() work with correct arguments"""
    x, y, height, width = values
    assert Rectangle(x, y, height, width).draw() is None


wrong_values = [('0', 0, 10, 10),
                (0.0, 0, 0, 0),
                (0, 0, '10', 10),
                (1, 5, 10, '10')]


@pytest.mark.parametrize('wrong_values', wrong_values)
def test_rectangle_wrong_values(wrong_values):
    """This test is needed to make sure the method draw() doesn't work with wrong arguments"""
    x, y, height, width = wrong_values
    with pytest.raises(ValueError):
        Rectangle(x, y, height, width).draw()
