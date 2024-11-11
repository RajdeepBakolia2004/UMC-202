from math import log,exp,sqrt
def f(t : float, y : float) -> float:
    return -t*y + 4*t/y
def solution(t):
    return sqrt(4 - 3 * exp(-(t**2)))
def rk2(a : float ,h : float,b : float, y0 : float):
    y = y0
    t = a
    while t < (b+h):
        print(f"t : {t} w : {y} y : {solution(t)} error : {abs(y - solution(t))}")
        y = y + h*f(t + h/2,y + h*f(t,y)/2)
        t = round(t+h,5)
if __name__ == "__main__":
    rk2(0,0.25,1,1)

