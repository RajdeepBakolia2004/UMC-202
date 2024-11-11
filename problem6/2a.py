from math import log
def f(t : float, y : float) -> float:
    return y/t - y**2/t**2

def solution(t):
    return t/(1+log(t))
def rk2(a : float ,h : float,b : float, y0 : float):
    y = y0
    t = a
    while t < (b+h):
        print(f"t : {t} w : {y} y : {solution(t)} error : {abs(y - solution(t))}")
        y = y + h*f(t + h/2,y + h*f(t,y)/2)
        t = round(t+h,5)
if __name__ == "__main__":
    rk2(1,0.1,1.2,1)

