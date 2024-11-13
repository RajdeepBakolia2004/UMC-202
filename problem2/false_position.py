from math import pow,exp,log,e
def f(x : float) -> float:
    return  (230*pow(x,4)+18*pow(x,3)+9*pow(x,2)-221*x-9)
def false_position(x0 : float, x1 : float, tol : float, max_iter : int):
    iteration = 1
    for i in range(max_iter):
        x = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        if abs(x-x1) < tol:
            return x,iteration
        if f(x)*f(x1) < 0:
            x0 = x1
        x1 = x
        iteration += 1
    return x,iteration
res1,i= false_position(-1,0,1e-5,10000)
print(f"Result: {res1}, iterations: {i}")
res2,i = false_position(1,2,1e-5,10000)
print(f"Result: {res2} , iterations: {i}")