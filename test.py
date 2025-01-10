
import display as display

print("\n")
print("Hello Human!\n")

class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * self._length  + 2 * self._width

    def __str__(self):
        if self.is_square(self._length, self._width):
            return f"Square with side {self._length}"
        else:
            return f"Rectangle with side {self._length} and {self._width}"

    def __repr__(self):
        return f"Square({self.side})"
    
    @classmethod
    def unit_square(cls,length):
        return cls(length, length)
    @staticmethod
    def is_square(length, width):
        return length == width

recangulo = Rectangle(10, 20)
print(recangulo)
print(f" area: {recangulo.area()}")
print(f" perimeter: {recangulo.perimeter()}")

print("\n")
quadrado = Rectangle.unit_square(30)
print(quadrado)
print(f"unit_square: {quadrado._length} {quadrado._width}")
print(f" area: {quadrado.area()}")
print(f" perimeter: {quadrado.perimeter()}")
print("\n")

print(__name__)
print(display.__name__)