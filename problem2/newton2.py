from math import pow,exp,log,e
def f(x : float) -> float:
    return x - ((x-exp(-x)))/(2*(1+exp(-x)))
def newton2(x0 : float, tol : float, max_iter : int):
    x = x0
    iteration = 1
    for i in range(max_iter):
        x = f(x)
        if abs(x-x0) < tol:
            return x,iteration
        x0 = x
        iteration += 1
    return x
res,i= newton2(0.5,1e-5,100)
print(f"Result: {res} , iterations: {i}")
