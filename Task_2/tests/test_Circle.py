import pytest
from Task_2.Engine import Circle, Shape


def test_circle_is_subclass_of_shape():
    """This test is needed to make sure that the class 'Circle' has a method draw()"""
    assert issubclass(Circle, Shape)


values = [(0, 1, 5),
          (-1, 1, 2),
          (2, -2, 1)]


@pytest.mark.parametrize('values', values)
def test_circle_good(values):
    """This test is needed to make sure the method draw() work with correct arguments"""
    x, y, radius = values
    assert Circle(x, y, radius).draw() is None


wrong_values = [(0, 1, -5),
                (-1, 1, 0),
                ('0', 1, 5),
                (1, '1', 1),
                (2, -2, '5')]


@pytest.mark.parametrize('wrong_values', wrong_values)
def test_circle_wrong_values(wrong_values):
    """This test is needed to make sure the method draw() doesn't work with wrong arguments"""
    x, y, radius = values
    with pytest.raises(ValueError):
        Circle(x, y, radius).draw()
