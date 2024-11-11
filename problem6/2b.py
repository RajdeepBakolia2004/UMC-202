def f(x : float, y : float) -> float:
    return (y**2 + y)/x
def solution(t):
    return (2*t) / (1 - 2*t)
def rk2(a : float ,h : float,b : float, y0 : float):
    y = y0
    t = a
    while t < (b+h):
        print(f"t : {t} w : {y} y : {solution(t)} error : {abs(y - solution(t))}")
        y = y + h*f(t + h/2,y + h*f(t,y)/2)
        t = round(t+h,5)
if __name__ == "__main__":
    rk2(1,0.5,3,-2)

