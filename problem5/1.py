from math import log


def f(x:float) -> float:
    """
    Calculate the natural logarithm of a number.

    Parameters:
    x (float): The number for which to compute the natural logarithm. Must be greater than zero.

    Returns:
    float: The natural logarithm of the input number.
    """
    return log(x)

def derivative_forward(a : float, h : float)->float:    
    """
    Calculate the forward difference approximation of the derivative of the function f at a point a.

    Parameters:
    a (float): The point at which to evaluate the derivative.
    h (float): The step size for the forward difference.

    Returns:
    tuple: A tuple containing the approximation of the derivative (float), the actual error (float),
           and the error bound (float).
    """
    result = (f(a+h) - f(a))/h
    actual_error = abs(result - 1/a)
    error_bound = h/(2*a*a)
    return result, actual_error, error_bound

result1 = derivative_forward(1.8, 0.1)
result2 = derivative_forward(1.8, 0.05)
result3 = derivative_forward(1.8, 0.01)

print(f"h = 0.1 Result: {result1[0]}, Actual Error: {result1[1]}, Error Bound: {result1[2]}")
print(f"h = 0.05 Result: {result2[0]}, Actual Error: {result2[1]}, Error Bound: {result2[2]}")
print(f"h = 0.01 Result: {result3[0]}, Actual Error: {result3[1]}, Error Bound: {result3[2]}")
