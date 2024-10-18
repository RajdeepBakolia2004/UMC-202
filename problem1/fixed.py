from math import pow

#def g(x) := (3*x**2+3)**0.25
def g(x : float) -> float:
    return pow(3*x**2+3, 0.25)

#fixed point iteration
def fixed(p : float, n: int , TOL : float = 1e-2) -> float:
    i = 1
    while i <= n:
        q = g(p)
        if abs(q - p) < TOL:
            return q,i
        else:
            p = q
        i += 1
    else:
        return False,False


#main part of the program
if __name__ == "__main__":
    res,i = fixed(1,20)
    if res:
        print(f"the solution to this problem in the range [1,2] exist with p = {res} founded after {i} iteration")

