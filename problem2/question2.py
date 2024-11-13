from math import pow,exp,log,e
def f(x : float) -> float:
    return x - (230*pow(x,4)+18*pow(x,3)+9*pow(x,2)-221*x-9)/(920*pow(x,3)+54*pow(x,2)+18*x-221)
def newton(x0 : float, tol : float, max_iter : int):
    x = x0
    iteration = 1
    for i in range(max_iter):
        x = f(x)
        if abs(x-x0) < tol:
            return x,iteration
        x0 = x
        iteration += 1
    return x
res1,i= newton(1.0,1e-5,100)
print(f"Result: {res1} , iterations: {i}")
res2,i= newton(0.5,1e-5,100)
print(f"Result: {res2} , iterations: {i}")
