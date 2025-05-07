import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self._validate_sides(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def _validate_sides(self, a: float, b: float, c: float):
        if any(side <= 0 for side in (a, b, c)):
            raise ValueError("Длины сторон должны быть положительными")
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Недопустимые значения сторон треугольника")

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angled(self, tolerance: float = 1e-6) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < tolerance

class ShapeFactory:
    @staticmethod
    def create_shape(*args) -> Shape:
        if len(args) == 1:
            return Circle(args[0])
        elif len(args) == 3:
            return Triangle(*args)
        raise ValueError("Неподдерживаемый тип фигуры")
