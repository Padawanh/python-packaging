
from udemycalculator.calculator import Calculator as calc

machine = calc()

print(f"square_area : {machine.calculate_square_area(5)}")

print(f"triangle_area : {machine.calculate_triangle_area(5, 3)}")

print(f"trapezoid_area : {machine.calculate_trapezoid_area(5, 3, 2)}")

print(f"compare_squares : {machine.compare_squares(5, 3)}")
