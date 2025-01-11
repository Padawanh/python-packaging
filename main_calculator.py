
from udemycalculator.calculator import Calculator as calc

calc_machine = calc()

print(calc_machine.calculate_square_area(5))


print(calc_machine.calculate_triangle_area(5, 5))


print(calc_machine.calculate_trapezoid_area(5, 3, 2))


print(calc_machine.compare_squares(5, 5))
