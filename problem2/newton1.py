from math import pow,exp,log,e
def f(x : float) -> float:
    return x - (pow(x,3)-2*pow(x,2)-5)/(3*pow(x,2)-4*x)

def newton1(x0 : float, tol : float, max_iter : int):
    x = x0
    iteration = 1
    for i in range(max_iter):
        x = f(x)
        if abs(x-x0) < tol:
            return x,iteration
        x0 = x
        iteration += 1
    return x

res,i = newton1(1.0,1e-5,100)
print(f"Result: {res}" , f"iterations: {i}")