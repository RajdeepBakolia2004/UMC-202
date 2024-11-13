from math import exp
def f(t : float ,y : float):
    return y-t**2+1
def solution(t : float):
    return (t+1)**2-0.5*exp(t)

def runge_kutta(t0 : float,y0 : float,h : float):
    y = y0 + h*(f(t0 + h/2,y0 + h/2*f(t0,y0)))
    return y

def adam_basforth_two_step(t0 : float,y0 : float,h : float,b : float):
    y1 = runge_kutta(t0,y0,h)
    t = t0 + h
    print(f"t : {t0} w : {y0} y : {solution(t0)} error : {abs(y0-solution(t0))}")
    print(f"t : {t} w : {y1} y : {solution(t)} error : {abs(y1-solution(t))}")
    while t < b:
        y = y1 + h/2*(3*f(t,y1)-f(t-h,y0))
        y0 = y1
        y1 = y
        t = round(t + h,5)
        print(f"t : {t} w : {y} y : {solution(t)} error : {abs(y-solution(t))}")

if __name__ == "__main__":
    adam_basforth_two_step(0,0.5,0.5,2)