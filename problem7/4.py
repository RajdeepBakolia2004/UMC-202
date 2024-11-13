from math import exp
def f(t : float ,y : float):
    return y-t**2+1
def solution(t : float):
    return (t+1)**2-0.5*exp(t)

def runge_kutta(t0 : float,y0 : float,h : float):
    k1 = h*f(t0,y0)
    k2 = h*f(t0+h/2,y0+k1/2)
    k3 = h*f(t0+h/2,y0+k2/2)
    k4 = h*f(t0+h,y0+k3)
    y = y0 + 1/6*(k1+2*k2+2*k3+k4)
    return y


def fourth_predictor_corrector(t0 : float,y0 : float,h : float,b : float):
    y1 = runge_kutta(t0,y0,h)
    y2 = runge_kutta(t0 + h,y1,h)
    y3 = runge_kutta(t0+2*h,y2,h)
    t = t0 + 3*h
    print(f"t : {t0} w : {y0} y : {solution(t0)} error : {abs(y0-solution(t0))}")
    print(f"t : {t-2*h} w : {y1} y : {solution(t-2*h)} error : {abs(y1-solution(t-2*h))}")
    print(f"t : {t-h} w : {y2} y : {solution(t-h)} error : {abs(y2-solution(t-h))}")
    print(f"t : {t} w : {y3} y : {solution(t)} error : {abs(y3-solution(t))}")
    while t < b:
        result = y3 + (h/24)*(55*f(t,y3) - 59*f(t-h,y2) + 37*f(t - 2*h,y1) - 9*f(t - 3*h,y0))
        y = y3 + (h/24)*(9*f(t+h,result) + 19*f(t,y3) - 5*f(t-h,y2) + f(t - 2*h,y1))
        t = round(t + h,5)
        print(f"t : {t} w : {y} y : {solution(t)} error : {abs(y-solution(t))}")
        y0 = y1
        y1 = y2
        y2 = y3
        y3 = y

if __name__ == "__main__":
    fourth_predictor_corrector(0,0.5,0.2,2)