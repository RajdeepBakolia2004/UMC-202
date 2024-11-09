from math import pow , sin

#define the function
def f(x : float):
    return pow(x,3) - 7*pow(x,2) + 14*x - 6

#the bisection method to return the answer
def bisection(a : float, b : float, n : int, TOL : float= 1e-4 ) -> float:
    i = 1
    fa,fb = f(a),f(b)
    while i <= n:
        p = a + (b-a)/2
        if f(p) == 0 or ((b-a)/2 < TOL):
            return p,i
        elif f(p)*fa > 0:
            a = p
        else:
            b = p
        i += 1
    else:
        return False,False


#main of the function
if __name__ == "__main__":
    res1,i1 = bisection(0,1,20)
    if res1: 
        print(f"The function have a solution in [0,1] and it is founded after {i1} iteration and is equal to {res1}")
    res2,i2 = bisection(1,3.2,20)
    if res2:
        print(f"The function have a solution in [0,1] and it is founded after {i2} iteration and is equal to {res2}")
    res3,i3 = bisection(3.2,4,20)
    if res3:
        print(f"The function have a solution in [0,1] and it is founded after {i3} iteration and is equal to {res3}")
   
