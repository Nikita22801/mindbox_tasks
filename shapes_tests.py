import pytest
from shapes import Circle, Triangle, ShapeFactory

def test_circle_area():
    assert Circle(5).area() == math.pi * 25

def test_triangle_area():
    assert Triangle(3, 4, 5).area() == 6.0

def test_right_angled():
    assert Triangle(3, 4, 5).is_right_angled()

def test_factory_creation():
    assert isinstance(ShapeFactory.create_shape(5), Circle)
    assert isinstance(ShapeFactory.create_shape(3,4,5), Triangle)

def test_validation():
    with pytest.raises(ValueError):
        Circle(-1)
    with pytest.raises(ValueError):
        Triangle(1, 2, 5)
