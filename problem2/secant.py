from math import pow,exp,log,e
def f(x : float) -> float:
    return 230*pow(x,4)+18*pow(x,3)+9*pow(x,2)-221*x-9
def secant(x0 : float, x1 : float, tol : float, max_iter : int):
    iteration = 1
    for i in range(max_iter):
        x = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        if abs(x-x1) < tol:
            return x,iteration
        x0 = x1
        x1 = x
        iteration += 1
    return x
res1,i= secant(0,1,1e-5,10000)
print(f"Result: {res1} , iterations: {i}")
res2,i = secant(-1,0,1e-5,10000)
print(f"Result: {res2} , iterations: {i}")