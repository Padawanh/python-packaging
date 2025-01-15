import numpy as np
# print(np.__version__)
class Calculator:
    @staticmethod
    def calculate_square_area(side: float) -> float:
        """
        Calculate the area of a square.

        :param side: Length of the side of the square.
        :type side: float
        :return: Area of the square.
        :rtype: float
        """
        return side**2

    @staticmethod
    def calculate_triangle_area(base: float, height: float) -> float:
        """
        Calculate the area of a triangle.

        :param base: Length of the base of the triangle.
        :type base: float
        :param height: Height of the triangle.
        :type height: float
        :return: Area of the triangle.
        :rtype: float
        """
        return 0.5 * base * height

    @staticmethod
    def calculate_trapezoid_area(base1: float, base2: float, height: float) -> float:
        """
        Calculate the area of a trapezoid.

        :param base1: Length of the first base of the trapezoid.
        :type base1: float
        :param base2: Length of the second base of the trapezoid.
        :type base2: float
        :param height: Height of the trapezoid.
        :type height: float
        :return: Area of the trapezoid.
        :rtype: float
        """
        return 0.5 * (base1 + base2) * height

    @staticmethod
    def compare_squares(side1: float, side2: float) -> bool:
        """
        Compare the areas of two squares.

        :param side1: Length of the side of the first square.
        :type side1: float
        :param side2: Length of the side of the second square.
        :type side2: float
        :return: True if the areas of the squares are equal, False otherwise.
        :rtype: bool
        """
        return side1**2 == side2**2
