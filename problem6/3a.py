from math import log
def f(t : float, y : float) -> float:
    return y/t - y**2/t**2

def solution(t):
    return t/(1+log(t))
def fixed(t : float, y : float, h : float) -> float:
    result = y 
    while result != (y + (h*(f(t,y) + f(t+h,result)))/2):
        result = (y + (h*(f(t,y) + f(t+h,result)))/2)
    return result
def trapezoidal2(a : float ,h : float,b : float, y0 : float):
    y = y0
    t = a
    while t < (b+h):
        print(f"t : {t} w : {y} y : {solution(t)} error : {abs(y - solution(t))}")
        y = fixed(t,y,h)
        t = round(t+h,5)
if __name__ == "__main__":
    trapezoidal2(1,0.1,1.2,1)

