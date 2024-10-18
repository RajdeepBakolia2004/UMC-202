from math import sqrt,cos
def f(x):
    return sqrt(x) - cos(x)
n = int(input("enter an integer: "))
i = 0 
a,b = 0,1
while i < n:
    sol = (a+b)/2
    if f(a)*f(sol) < 0:
        b = sol
    else:
        a = sol
    print(f"iteration {i+1}: f({sol}) = {f(sol)}")    
    i += 1

