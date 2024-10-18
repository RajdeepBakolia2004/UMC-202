from math import sqrt, pow
# define the function
def g(x : float):
    return x - ((pow(x,2) - 6) / (2*x))

#newtons method
def newtons(p : float, TOL : float = 1e-6, n : int = 300):
    i = 1
    while i <= n:
        q = g(p)
        if abs(q*q-6) < TOL:
            return q,i
        i += 1
        p = q
    else:
        return False,False

if __name__ == "__main__":
    res,i = newtons(1)
    if res:
        print(f"found a solution to the function after {i} iteration and it is {res}")
