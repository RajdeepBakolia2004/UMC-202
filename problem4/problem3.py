from math import e,pi,tan
def f(x):
    return (x**3)*e**x
def g(X):
    return tan(x)
def composite_trapezoidal(f,a,b,n,result):
    h = (b-a)/n
    
    s = 0
    for i in range(1,n):
        s += f(a+i*h)

    integral =  h*(f(a)+2*s+f(b))/2
    error = abs(integral - result)

    return integral, error
def composite_simpson(f,a,b,n,result):
    h = (b-a)/n
    
    s = 0
    for i in range(1,n):
        s += f(a+i*h)
    s *= 2

    t = 0
    for i in range(1,n+1):
        t += f(a+(i-0.5)*h)
    t *= 4

    integral =  h*(f(a)+s+t+f(b))/6
    error = abs(integral - result)

    return integral, error

print(composite_simpson(f,0,0.5,4,0.0233845))
print(composite_trapezoidal(f,0,0.5,4,0.0233845))

print(composite_simpson(f,0,3*pi/8,8,0.96055))
print(composite_trapezoidal(f,0,3*pi/8,8,0.96055))