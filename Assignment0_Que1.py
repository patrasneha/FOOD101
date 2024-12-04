def slope_of_cubic(coefficients: tuple, x: float) -> float:
    a, b, c, d = coefficients
    
    # Derivative of cubic polynomial ax^3 + bx^2 + cx + d is 3ax^2 + 2bx + c
    slope = 3 * a * x**2 + 2 * b * x + c
    
    return slope
