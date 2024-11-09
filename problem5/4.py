from math import e,exp


def f(t:float,y:float)->float:
    """
    The function defining a first order ordinary differential equation.

    Parameters:
    t (float): The value of the independent variable.
    y (float): The value of the dependent variable.

    Returns:
    float: The value of the derivative of the dependent variable with respect to the independent variable.
    """
    return t*exp(3*t) - 2*y

def g(t:float)->float:
    """
    The exact solution to a first order ordinary differential equation.

    Parameters:
    t (float): The value of the independent variable.

    Returns:
    float: The exact value of the dependent variable.
    """
    return (1/5)*t*exp(3*t) - (1/25)*exp(3*t) + (1/25)*exp(-2*t)

def euler(t0:float, y0:float, h:float, n:int)->float:
    """
    Calculate the approximate solution to a first order ordinary differential equation using Euler's method.

    Parameters:
    t0 (float): The initial value of the independent variable.
    y0 (float): The initial value of the dependent variable.
    h (float): The step size.
    n (int): The number of steps to take.

    Returns:
    float: The approximate solution at the final step.
    """
    t = t0
    y = y0
    for i in range(n):
        actual_error = abs(y - g(t))
        error_bound = (exp(2*t)-1)*h
        print(f"t = {t}, y = {y}, Actual Error = {actual_error}, Error Bound = {error_bound}")
        y = y + h*f(t,y)
        t = round(t + h,5)
    else:
        actual_error = abs(y - g(t))
        error_bound = (exp(2*t)-1)*h
        print(f"t = {t}, y = {y}, Actual Error = {actual_error}, Error Bound = {error_bound}")
    return y
euler(0,0,0.5,2)