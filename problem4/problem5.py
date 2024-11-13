from math import sqrt,sin,pi

def transform(x,a,b):
    return (b-a)/2*x + (b+a)/2

def two_point_gaussian(f,a,b):
    return (b-a)/2*(f(transform(-1/sqrt(3),a,b)) + f(transform(1/sqrt(3),a,b)))

def f(x):
    return x*x*sin(x)

print(two_point_gaussian(f,0,pi/2))