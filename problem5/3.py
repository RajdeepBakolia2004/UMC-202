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
    result = (4*f(a+h) - (3*f(a)+f(a+2*h)))/(2*h)
    actual_error = abs(result - 1/a)
    error_bound = (2*h*h)/(3*a**3)
    return result, actual_error, error_bound

result7 = derivative_forward(1.8, 0.1)
result8 = derivative_forward(1.8, 0.05)
result9 = derivative_forward(1.8, 0.01)

print(f"h = 0.1 Result: {result7[0]}, Actual Error: {result7[1]}, Error Bound: {result7[2]}")
print(f"h = 0.05 Result: {result8[0]}, Actual Error: {result8[1]}, Error Bound: {result8[2]}")
print(f"h = 0.01 Result: {result9[0]}, Actual Error: {result9[1]}, Error Bound: {result9[2]}")

def derivative_backward(a : float, h : float)->float:    
    """
    Calculate the backward
 difference approximation of the derivative of the function f at a point a.

    Parameters:
    a (float): The point at which to evaluate the derivative.
    h (float): The step size for the backward
 difference.

    Returns:
    tuple: A tuple containing the approximation of the derivative (float), the actual error (float),
           and the error bound (float).
    """
    result = (4*f(a+h) - (3*f(a)+f(a+2*h)))/(2*h)
    actual_error = abs(result - 1/a)
    error_bound = (2*h*h)/(3*(a+h)**3)
    return result, actual_error, error_bound

result1 = derivative_backward(1.8, -0.1)
result2 = derivative_backward(1.8, -0.05)
result3 = derivative_backward(1.8, -0.01)

print(f"h = 0.1 Result: {result1[0]}, Actual Error: {result1[1]}, Error Bound: {result1[2]}")
print(f"h = 0.05 Result: {result2[0]}, Actual Error: {result2[1]}, Error Bound: {result2[2]}")
print(f"h = 0.01 Result: {result3[0]}, Actual Error: {result3[1]}, Error Bound: {result3[2]}")


def derivative_central(a,h):
    """
    Calculate the central difference approximation of the derivative of the function f at a point a.

    Parameters:
    a (float): The point at which to evaluate the derivative.
    h (float): The step size for the central difference.

    Returns:
    tuple: A tuple containing the approximation of the derivative (float), the actual error (float),
           and the error bound (float).
    """
    result = (f(a+h) - f(a-h))/(2*h)
    actual_error = abs(result - 1/a)
    error_bound = (h*h)/(3*a*a*a)
    return result, actual_error, error_bound

result4 = derivative_central(1.8, -0.1)
result5 = derivative_central(1.8, -0.05)
result6 = derivative_central(1.8, -0.01)

print(f"h = 0.1 Result: {result4[0]}, Actual Error: {result4[1]}, Error Bound: {result4[2]}")
print(f"h = 0.05 Result: {result5[0]}, Actual Error: {result5[1]}, Error Bound: {result5[2]}")
print(f"h = 0.01 Result: {result6[0]}, Actual Error: {result6[1]}, Error Bound: {result6[2]}")
