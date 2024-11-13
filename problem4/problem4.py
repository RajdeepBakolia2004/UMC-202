from math import sin,pi

def transform(x,a,b):
    return (b-a)/2*x + (b+a)/2

def one_point_gaussian(f,a,b):
    return (b-a)*f(transform(0,a,b))

def f(x):  
    return x*x*sin(x)
    
print(one_point_gaussian(f,0,pi/4))