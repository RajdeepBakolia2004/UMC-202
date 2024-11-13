from math import e,pi,sin
def f(x):
    return 2/(x-4)
def g(x):
    return (e**(3*x))*sin(2*x)

def trapezoid(h,a,b):
    return (b-a)*(h(a)+h(b))/2 

    
def simpsons(h,a,b):
    return (b-a)*(h(a)+4*h((a+b)/2)+h(b))/6

print(simpsons(f,0,0.5))
print(simpsons(g,0,pi/4))
print(trapezoid(f,0,0.5))
print(trapezoid(g,0,pi/4))