from math import log,exp,sqrt
def f(t : float, y : float) -> float:
    return -t*y + 4*t/y

def df(t : float, y : float) -> float:
    return -y + 4/y + (-t - (4*y)/(y**2))*(-t*y + 4*t/y)

def solution(t):
    return sqrt(4 - 3 * exp(-(t**2)))
def taylor_order2(a : float ,h : float,b : float, y0 : float):
    y = y0
    t = a
    while t < (b+h):
        print(f"t : {t} w : {y} y : {solution(t)} error : {abs(y - solution(t))}")
        y = y + h*f(t,y) + (h*h*df(t,y))/2
        t = round(t+h,5)
if __name__ == "__main__":
    taylor_order2(0,0.25,1,1)

