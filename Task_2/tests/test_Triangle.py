import pytest
from Task_2.Engine import Triangle, Shape


def test_Triangle_is_subclass_of_Shape():
    """This test is needed to make sure that the class 'Triangle' has a method draw()"""
    assert issubclass(Triangle, Shape)


coordinates = [(1, 1, 3, 1, 2, 5),
               (0, 0, 3, 1, 1, 3),
               (2.1, 0, -1, -3.3, 1, 4),
               (-2, -1, -1, 3, 0, 1)]


@pytest.mark.parametrize('coordinates', coordinates)
def test_triangle_good(coordinates):
    """This test is needed to make sure the method draw() works with correct arguments"""
    x1, y1, x2, y2, x3, y3 = coordinates
    assert Triangle(x1, y1, x2, y2, x3, y3).draw() is None


wrong_coordinates = [(1, 1, 3, 1, 2, '5'),
                     (0, 1, 0, 1, 3, 5),
                     (1, 1, None, 1, 2, 5),
                     (0, 0, 0, 0, 0, 0)]


@pytest.mark.parametrize('wrong_coordinates', wrong_coordinates)
def test_triangle_wrong_coordinates(wrong_coordinates):
    """This test is needed to make sure the method draw() doesn't work with wrong arguments"""
    x1, y1, x2, y2, x3, y3 = wrong_coordinates
    with pytest.raises(ValueError):
        Triangle(x1, y1, x2, y2, x3, y3).draw()
